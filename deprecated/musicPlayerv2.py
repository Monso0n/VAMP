import pyautogui as pg
import time
width, height = pg.size()



def screenshot():
    try:
        a = pg.pixel(806, 137)
    except:
        a = pg.pixel(806, 137)

    print(a)

    buyphase = pg.screenshot('buyPhaseCapture.png', region=(805, 135, 311, 145))
    return pg.screenshot('screenshot.png', region=(0,0,width, height))

def testRoundEnd(): #tests for buy phase, round loss, and round win
    print(pg.pixel(806, 137))
    if pg.pixelMatchesColor(806, 137, (255,255,255)):
        print("Detected White")
        return True
    return False

def testDeath():
    print(pg.pixel(1612, 376))
    if pg.pixelMatchesColor(1612, 376, (255,255,255)):
        print("Detected White")
        return True
    return False


def playpause():
    pg.press('playpause')

time.sleep(3)
print("go")
screenshot()

while True:
    time.sleep(.2)

    if testRoundEnd() or testDeath():
        playpause()

