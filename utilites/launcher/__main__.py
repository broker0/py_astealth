import runpy
import sys
import argparse
import traceback
import importlib
from pathlib import Path

try:
    import py_astealth.stealth as stealth
    from py_astealth.config import (
        ERROR_FILTER,
        USE_STEALTH_SYSTEM_JOURNAL,
        REMOVE_NEW_LINES
    )
except ImportError:
    current_dir = Path(__file__).resolve().parent
    sys.path.insert(0, str(current_dir.parent))

    import py_astealth.stealth as stealth
    from py_astealth.config import (
        ERROR_FILTER,
        USE_STEALTH_SYSTEM_JOURNAL,
        REMOVE_NEW_LINES
    )


class SysJournalOut:
    """Redirects stdout/stderr output to the Stealth log."""

    def __init__(self, original_stream=None):
        self._buffer: list[str] = []
        self.original_stream = original_stream

    def write(self, text: str):
        # Write to the original stream (console), if there is one
        if self.original_stream:
            self.original_stream.write(text)

        # Accumulate a buffer for sending to the Stealth log
        self._buffer.append(text)
        if '\n' in text:
            self.flush()

    def flush(self):
        if not self._buffer:
            return

        full_text = "".join(self._buffer)
        if REMOVE_NEW_LINES:
            full_text = full_text.replace('\n', '')

        if full_text:
            stealth.AddToSystemJournal(full_text)

        self._buffer.clear()


def setup_io_redirection():
    """Redirects print() and errors to the Stealth log."""
    if USE_STEALTH_SYSTEM_JOURNAL:
        sys.stdout = SysJournalOut(sys.stdout)
        sys.stderr = SysJournalOut(sys.stderr)


def print_clean_traceback(exc: Exception):
    """Nice traceback, excluding the library files themselves."""
    tb_list = traceback.extract_tb(exc.__traceback__)

    clean_tb = [
        frame for frame in tb_list
        if "py_astealth" not in str(frame.filename) and
           "py_stealth" not in str(frame.filename) and
           "runpy.py" not in str(frame.filename)
    ]

    print("Traceback (most recent call last):", file=sys.stderr)
    for frame in clean_tb:
        print(f'  File "{frame.filename}", line {frame.lineno}, in {frame.name}', file=sys.stderr)
        if frame.line:
            print(f'    {frame.line}', file=sys.stderr)

    print(f"{type(exc).__name__}: {exc}", file=sys.stderr)


def main():
    if len(sys.argv) < 2:
        error = 'CMD params must be: path_to_script [port] [func] [args]'
        print(error)
        sys.exit(4)

    script_arg = sys.argv[1]

    setup_io_redirection()

    # Add the script folder to the import path so that the script can see its files nearby
    script_path = Path(script_arg).resolve()
    sys.path.insert(0, str(script_path.parent))

    # Connecting to Stealth
    stealth.Wait(1)

    try:
        target_func_name = None
        if len(sys.argv) >= 4:
            # import script as module, so __main__ will not run
            target_func_name = sys.argv[3]

        if target_func_name:
            module_name = script_path.stem
            module = importlib.import_module(module_name)

            if hasattr(module, target_func_name):
                target_func = getattr(module, target_func_name)
                if callable(target_func):
                    target_func()
                else:
                    print(f"Error: '{target_func_name}' is not callable.")
            else:
                print(f"Error: Function '{target_func_name}' not found.")
        else:
            # Substitute sys.argv so the script can see its arguments
            # Before: ['launcher.py', 'myscript.py', ...]
            # Now: ['myscript.py', 'arg1', 'arg2'...]
            original_argv = sys.argv

            script_args = sys.argv[1:]
            sys.argv = [str(script_path)] + script_args

            try:
                runpy.run_path(str(script_path), run_name='__main__')
            finally:
                sys.argv = original_argv

    except SystemExit:
        pass
    except Exception as error:
        if not ERROR_FILTER:
            raise error
        else:
            print_clean_traceback(error)


if __name__ == '__main__':
    main()
