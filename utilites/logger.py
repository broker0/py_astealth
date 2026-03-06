import logging
import sys

from py_astealth.utilites import config

# --- Logger Hierarchy ---

# Root logger for the entire package
logger = logging.getLogger("py_astealth")

# Specialized sub-loggers for different components
client_logger = logging.getLogger("py_astealth.client")
protocol_logger = logging.getLogger("py_astealth.protocol")
session_logger = logging.getLogger("py_astealth.session")


# --- Configuration ---

def setup_logging():
    """
    Initializes the logging system based on config.py settings.
    Mutually exclusive: File logging OR Console logging.
    """
    client_logger.setLevel(config.LOG_LEVEL_CLIENT)
    protocol_logger.setLevel(config.LOG_LEVEL_PROTOCOL)
    session_logger.setLevel(config.LOG_LEVEL_SESSION)

    # lowest level for the root logger
    logger.setLevel(min(client_logger.level, protocol_logger.level, session_logger.level))

    formatter = logging.Formatter(
        fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    if config.LOG_TO_FILE:
        log_file = config.LOG_FILE
        try:
            handler = logging.FileHandler(log_file, mode='w', encoding='utf-8')  # Overwrite log on start ('w')
        except Exception as e:
            print(f"Logging Error: Could not open {log_file} ({e}). Falling back to stdout.", file=sys.stderr)
            handler = logging.StreamHandler(sys.stdout)
    else:
        handler = logging.StreamHandler(sys.stdout)

    handler.setFormatter(formatter)
    logger.addHandler(handler)


# Auto-initialize on first import
setup_logging()
