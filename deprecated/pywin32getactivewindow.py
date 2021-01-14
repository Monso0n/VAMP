from win32gui import GetWindowText, GetForegroundWindow, FindWindow, GetPixel
import time
import win32ui
from win32api import keybd_event


def pause():
    keybd_event(0xB2, 0)

def play():
    keybd_event(0xB2, 0)
    time.sleep(.1)
    keybd_event(0xB3, 0)


pause()