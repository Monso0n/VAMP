import pyautogui as pg
import time
width, height = pg.size()

#time.sleep(3)
print("go")

def screenshot():
    buyphase = pg.screenshot('buyPhaseCapture.png', region=(805, 135, 311, 145))
    return pg.screenshot('screenshot.png', region=(0,0,width, height))


def playpause():
    pg.press('playpause')



while True:
    time.sleep(.5)

