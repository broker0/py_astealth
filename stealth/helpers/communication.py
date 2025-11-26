"""Communication helpers: journal and messengers."""
from datetime import datetime, timedelta
from typing import Union

from py_astealth.stealth import api
from py_astealth.stealth_enums import Messenger
from ._converters import _get_messenger_id
from .common import Wait


# Journal helper functions
def _wait_journal_line_internal(start_time: datetime, text: str, max_wait_ms: int, check_system: bool) -> bool:
    """Internal helper for waiting journal lines."""
    if max_wait_ms:
        stop_time = start_time + timedelta(milliseconds=max_wait_ms)
    else:
        stop_time = datetime.max
    
    while datetime.now() <= stop_time:
        if api.InJournalBetweenTimes(text, start_time, stop_time) >= 0:
            if not check_system or api.GetLineName() == 'System':
                return True
        Wait(10)
    return False


def WaitJournalLine(start_time: datetime, text: str, max_wait_ms: int = 0) -> bool:
    """
    Wait for a journal line containing the specified text.
    
    Args:
        start_time: Starting time for the search window (datetime object)
        text: Text to search for in journal
        max_wait_ms: Maximum wait time in milliseconds (0 = wait indefinitely)
        
    Returns:
        True if text was found, False if timeout
    """
    return _wait_journal_line_internal(start_time, text, max_wait_ms, check_system=False)


def WaitJournalLineSystem(start_time: datetime, text: str, max_wait_ms: int = 0) -> bool:
    """
    Wait for a system journal line containing the specified text.
    
    Args:
        start_time: Starting time for the search window (datetime object)
        text: Text to search for in journal
        max_wait_ms: Maximum wait time in milliseconds (0 = wait indefinitely)
        
    Returns:
        True if system message with text was found, False if timeout
    """
    return _wait_journal_line_internal(start_time, text, max_wait_ms, check_system=True)


# Messenger helpers
def MessengerGetConnected(messenger: Union[str, int, Messenger]) -> bool:
    """
    Check if messenger is connected.
    
    Args:
        messenger: Messenger name (str), ID (int), or Messenger enum
        
    Returns:
        True if connected, False otherwise
    """
    return api.Messenger_GetConnected(_get_messenger_id(messenger))


def MessengerSetConnected(messenger: Union[str, int, Messenger], value: bool) -> None:
    """
    Set messenger connection status.
    
    Args:
        messenger: Messenger name (str), ID (int), or Messenger enum
        value: Connection status
    """
    api.Messenger_SetConnected(_get_messenger_id(messenger), value)


def MessengerGetToken(messenger: Union[str, int, Messenger]) -> str:
    """
    Get messenger token.
    
    Args:
        messenger: Messenger name (str), ID (int), or Messenger enum
        
    Returns:
        Messenger token
    """
    return api.Messenger_GetToken(_get_messenger_id(messenger))


def MessengerSetToken(messenger: Union[str, int, Messenger], token: str) -> None:
    """
    Set messenger token.
    
    Args:
        messenger: Messenger name (str), ID (int), or Messenger enum
        token: Authentication token
    """
    api.Messenger_SetToken(_get_messenger_id(messenger), token)


def MessengerGetName(messenger: Union[str, int, Messenger]) -> str:
    """
    Get messenger name.
    
    Args:
        messenger: Messenger name (str), ID (int), or Messenger enum
        
    Returns:
        Messenger name
    """
    return api.Messenger_GetName(_get_messenger_id(messenger))


def MessengerSendMessage(messenger: Union[str, int, Messenger], msg: str, user_id: str) -> None:
    """
    Send a message via messenger.
    
    Args:
        messenger: Messenger name (str), ID (int), or Messenger enum
        msg: Message text
        user_id: Recipient user ID
    """
    api.Messenger_SendMessage(_get_messenger_id(messenger), msg, user_id)


__all__ = [
    'WaitJournalLine', 'WaitJournalLineSystem',
    'MessengerGetConnected', 'MessengerSetConnected', 'MessengerGetToken',
    'MessengerSetToken', 'MessengerGetName', 'MessengerSendMessage',
]
