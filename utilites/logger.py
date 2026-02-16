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
    Initializes or updates the logging system.
    """
    client_logger.setLevel(config.LOG_LEVEL_CLIENT)
    protocol_logger.setLevel(config.LOG_LEVEL_PROTOCOL)
    session_logger.setLevel(config.LOG_LEVEL_SESSION)

    # Synchronize parent logger level
    logger.setLevel(min(client_logger.level, protocol_logger.level, session_logger.level))

    # Ensure we have at least one handler emitting to stdout
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)


# Auto-initialize on first import
setup_logging()
