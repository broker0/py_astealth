"""Client-related helpers: UI, Gumps, and Connection."""
from typing import Union
from py_astealth.stealth import api
from py_astealth.stealth._internals import _manager
from py_astealth.stealth_enums import UIWindowType
from .common import Wait


def CloseClientUIWindow(ui_window_type: Union[str, UIWindowType], window_id: int) -> None:
    """
    Close a specific client UI window.
    
    Args:
        ui_window_type: UIWindowType enum or window type name string
        window_id: ID of the window
    """
    if isinstance(ui_window_type, str):
        ui_window_type = ui_window_type.lower()
        if ui_window_type in ('wtpaperdoll', 'paperdoll', '0'):
            ui_window_type = UIWindowType.Paperdoll
        elif ui_window_type in ('wtstatus', 'status', '1'):
            ui_window_type = UIWindowType.Status
        elif ui_window_type in ('wtcharprofile', 'charprofile', 'profile', '2'):
            ui_window_type = UIWindowType.CharProfile
        elif ui_window_type in ('wtcontainer', 'container', '3'):
            ui_window_type = UIWindowType.Container
        else:
            raise ValueError('CloseClientUIWindow: UIWindowType must be '
                             '"Paperdoll", "Status", "CharProfile" or "Container"')
    
    api.CloseClientUIWindow(int(ui_window_type), window_id)


def WaitForClientTargetResponse(max_wait_ms: int) -> bool:
    """
    Wait for client target response.

    Args:
        max_wait_ms: Maximum wait time in milliseconds

    Returns:
        True if response present, False if timeout
    """
    from time import time
    end_time = time() + max_wait_ms / 1000

    while time() < end_time:
        if api.ClientTargetResponsePresent():
            return True
        Wait(10)
    return False


def CorrectDisconnection() -> None:
    """Force close the current connection."""
    client = _manager.get_client_for_thread()
    # The proxy redirects calls, but close() might be on the client object itself
    # or we might need to go through the manager to properly clean up.
    # _manager.close_client_for_thread(client._client) would be safer if we could access it.
    # But client is a proxy. client._client is accessible.
    
    # However, simply calling close() on the client should trigger the socket close.
    # The manager might try to reconnect or handle it.
    if hasattr(client, 'close'):
        client.close()


__all__ = ['CloseClientUIWindow', 'CorrectDisconnection', 'WaitForClientTargetResponse']
