from .common import AddToSystemJournal

"""Utility functions: math helpers and EasyUO compatibility."""


# Math utilities
def Dist(x1: int, y1: int, x2: int, y2: int) -> int:
    """
    Calculate distance between two points (Chebyshev distance).
    
    Args:
        x1, y1: First point coordinates
        x2, y2: Second point coordinates
        
    Returns:
        Maximum of absolute differences (Chebyshev distance)
    """
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    return dx if dx > dy else dy


def CalcCoord(x: int, y: int, direction: int) -> tuple[int, int]:
    """
    Calculate new coordinates after moving one step in direction.
    
    Args:
        x, y: Current coordinates
        direction: Direction (0-7, where 0=North, 2=East, 4=South, 6=West)
        
    Returns:
        Tuple of (new_x, new_y)
    """
    if direction > 7:
        return x, y
    
    dirs = {
        0: (0, -1),   # North
        1: (1, -1),   # NE
        2: (1, 0),    # East
        3: (1, 1),    # SE
        4: (0, 1),    # South
        5: (-1, 1),   # SW
        6: (-1, 0),   # West
        7: (-1, -1)   # NW
    }
    dx, dy = dirs[direction]
    return x + dx, y + dy


def CalcDir(xfrom: int, yfrom: int, xto: int, yto: int) -> int:
    """
    Calculate direction from one point to another.
    
    Args:
        xfrom, yfrom: Starting coordinates
        xto, yto: Target coordinates
        
    Returns:
        Direction (0-7), or 100 if same position
    """
    dx = abs(xto - xfrom)
    dy = abs(yto - yfrom)
    
    if dx == dy == 0:
        return 100
    elif (dx / (dy + 0.1)) >= 2:
        return 6 if xfrom > xto else 2  # West or East
    elif (dy / (dx + 0.1)) >= 2:
        return 0 if yfrom > yto else 4  # North or South
    elif xfrom > xto:
        return 7 if yfrom > yto else 5  # NW or SW
    elif xfrom < xto:
        return 1 if yfrom > yto else 3  # NE or SE
    
    return 100


# EasyUO compatibility (Windows only)
def SetEasyUO(num: int, value: str) -> None:
    """
    Set EasyUO registry variable (Windows only).
    
    Args:
        num: Variable number
        value: Value to set
    """
    try:
        import winreg
    except ImportError:
        raise OSError('SetEasyUO is only supported on Windows')
    
    key = winreg.HKEY_CURRENT_USER
    sub_key = 'Software\\EasyUO'
    access = winreg.KEY_WRITE
    
    with winreg.OpenKey(key, sub_key, 0, access) as easyuo_key:
        winreg.SetValueEx(easyuo_key, '*' + str(num), 0, winreg.REG_SZ, value)


def GetEasyUO(num: int) -> str:
    """
    Get EasyUO registry variable (Windows only).
    
    Args:
        num: Variable number
        
    Returns:
        Variable value
    """
    try:
        import winreg
    except ImportError:
        raise OSError('GetEasyUO is only supported on Windows')
    
    key = winreg.HKEY_CURRENT_USER
    sub_key = 'Software\\EasyUO'
    access = winreg.KEY_READ
    
    with winreg.OpenKey(key, sub_key, 0, access) as easyuo_key:
        type_, data = winreg.QueryValueEx(easyuo_key, '*' + str(num))
    return data


def EUO2StealthType(euo: str) -> int:
    """
    Convert EasyUO type string to Stealth type ID.
    
    Args:
        euo: EasyUO type string
        
    Returns:
        Stealth type ID, or 0 if result > 0xFFFF
    """
    res = 0
    multi = 1
    for char in euo:
        tmp = int.from_bytes(char.encode(), 'little')
        res += multi * (tmp - 65)
        multi *= 26
    res = (res - 7) ^ 0x0045
    return 0 if res > 0xFFFF else res


def EUO2StealthID(euo: str) -> int:
    """
    Convert EasyUO ID string to Stealth object ID.
    
    Args:
        euo: EasyUO ID string
        
    Returns:
        Stealth object ID
    """
    res = 0
    multi = 1
    for char in euo:
        tmp = int.from_bytes(char.encode(), 'little')
        res += multi * (tmp - 65)
        multi *= 26
    return (res - 7) ^ 0x0045


def PlayWav(FileName: str) -> None:
    """Play a WAV file on Windows.

    Args:
        FileName: Path to a .wav file.
    """
    import platform
    if platform.system() != "Windows":
        try:
            AddToSystemJournal('PlayWav supports only Windows.')
        except Exception:
            pass
        return
    try:
        import winsound
        winsound.PlaySound(FileName, winsound.SND_FILENAME)
    except Exception as e:
        try:
            AddToSystemJournal(f'PlayWav error: {e}')
        except Exception:
            pass

__all__ = [
    'Dist', 'CalcCoord', 'CalcDir',
    'SetEasyUO', 'GetEasyUO', 'EUO2StealthType', 'EUO2StealthID',
    'PlayWav',
]
