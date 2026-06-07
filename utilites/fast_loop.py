"""
Opportunistically install a faster asyncio event loop on package import.

On Windows we try `winloop`; on Linux/macOS we try `uvloop`. If the matching
package isn't installed, we fall back to the stdlib asyncio loop — no disruption
to users who haven't opted in.

Disable explicitly by setting the environment variable
`PY_ASTEALTH_NO_FAST_LOOP=1` before importing `py_astealth`.
"""
import os
import sys

from py_astealth.utilites.logger import logger


def install() -> str | None:
    """Install the fastest available asyncio loop for this platform.

    Returns the name of the loop installed (`"winloop"`/`"uvloop"`), or
    `None` if the matching package isn't installed and the stdlib loop is in use.
    """
    if os.environ.get("PY_ASTEALTH_NO_FAST_LOOP") in (1, '1', True, 'True', 'TRUE'):
        logger.debug("Fast event loop: disabled via PY_ASTEALTH_NO_FAST_LOOP")
        return None

    pkg_name = "winloop" if sys.platform == "win32" else "uvloop"
    try:
        if sys.platform == "win32":
            import winloop as _impl
        else:
            import uvloop as _impl
        _impl.install()
    except ImportError:
        logger.debug("Fast event loop: %s not installed; using stdlib asyncio", pkg_name)
        return None
    except Exception as e:
        logger.warning("Fast event loop: %s install failed (%s); using stdlib asyncio", pkg_name, e)
        return None

    logger.info("Fast event loop: %s installed", pkg_name)
    return pkg_name
