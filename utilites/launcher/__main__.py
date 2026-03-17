import threading
import runpy
import sys
import traceback
import importlib
import builtins

from pathlib import Path


# find the path to the py_astealth module
current_dir_path = Path(__file__).absolute().parent         # current file parent directory
stealth_path = str(current_dir_path.parent)                 # next parent directory
if stealth_path not in sys.path:
    sys.path.insert(0, stealth_path)


try:
    from py_astealth.utilites.config import ERROR_FILTER, USE_STEALTH_SYSTEM_JOURNAL, REMOVE_NEW_LINES
    from py_astealth.utilites import config
except ImportError as e:
    print(f"Critical Error: Could not import py_astealth. Checked path: {stealth_path}")
    raise e


class SysJournalOut:
    """Redirects stdout/stderr output to the Stealth log."""

    def __init__(self, stealth_module, original_stream=None):
        self.stealth = stealth_module
        self.original_stream = original_stream
        self._lock = threading.Lock()

    def write(self, text: str):
        with self._lock:
            # Write to the original stream (console), if there is one
            if self.original_stream:
                self.original_stream.write(text)

            if REMOVE_NEW_LINES:
                text = text.replace('\n', '')
            try:
                if text:
                    self.stealth.AddToSystemJournal(text.rstrip())
            except Exception as e:
                self.original_stream.write(f"error while stealth.AddToSystemJournal({text}) - {e}")

    def flush(self):
        pass


def setup_io_redirection(stealth_module):
    """Redirects print() and errors to the Stealth log."""
    if USE_STEALTH_SYSTEM_JOURNAL:
        sys.stdout = SysJournalOut(stealth_module, sys.stdout)
        sys.stderr = SysJournalOut(stealth_module, sys.stderr)


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


def inject_stealth_to_builtins(stealth_module):
    for name in dir(stealth_module):   # iterate over stealth module exports
        if not name.startswith('_'):    # skip private exports
            obj = getattr(stealth_module, name)
            setattr(builtins, name, obj)


def main():
    if len(sys.argv) < 2:
        error = 'CMD params must be: path_to_script [port] [func] [args] [--profile=profile]'
        print(error)
        sys.exit(4)

    # script arguments
    script_args = sys.argv[1:]

    # set script name
    script_path = Path(sys.argv[1]).resolve()
    config.STEALTH_SCRIPT_NAME = str(script_path)

    # set script port
    if len(sys.argv) >= 3 and sys.argv[2].isdigit():
        config.STEALTH_SCRIPT_PORT = int(sys.argv[2])

    # set profile name
    for arg in sys.argv:
        if arg.startswith('--profile='):
            config.STEALTH_PROFILE = arg.split('=', 1)[1]

    sys.path.insert(0, str(script_path.parent))
    # replace sys.argv[0] (py_stealth) with the script name
    sys.argv = [str(script_path)] + script_args

    # import stealth module and setup script environment
    import py_astealth.stealth as stealth_module

    stealth_module.Self()   # initialize connections
    inject_stealth_to_builtins(stealth_module)
    setup_io_redirection(stealth_module)

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
            try:
                runpy.run_path(str(script_path), run_name='__main__')
            finally:
                pass

    except SystemExit:
        pass
    except Exception as error:
        if not ERROR_FILTER:
            raise error
        else:
            print_clean_traceback(error)


if __name__ == '__main__':
    main()
