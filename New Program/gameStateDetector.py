from win32gui import GetWindowText, GetForegroundWindow
from time import sleep
from PIL import ImageGrab, Image
import cv2
import numpy as np
import win32api

#for win, loss, thrifty, ace, teamace, clutch, flawless
def getRegion1(screenshot):
    tx = 891
    ty = 160
    bx = 1028
    by = 231

    imgCrop = screenshot.crop((tx, ty, bx, by))
    return imgCrop

#for death
def getRegion2(screenshot):
    tx = 134
    ty = 851
    bx = 273
    by = 874

    imgCrop = screenshot.crop((tx, ty, bx, by))
    return imgCrop

def getRegion3(screenshot):
    tx = 920
    ty = 130
    bx = 1000
    by = 140

    imgCrop = screenshot.crop((tx, ty, bx, by))
    return imgCrop

def matchTemplate(image, name):
    opencv_img = np.array(image.convert('RGB'))
    opencv_img = opencv_img[:, :, ::-1].copy()

    img_gray = cv2.cvtColor(opencv_img, cv2.COLOR_BGR2GRAY)


    opencv_template = cv2.imread('templates/'+name+".png", 0)

    #print(opencv_template.shape)
    w, h = opencv_template.shape[::-1]

#    cv2.imshow('output', opencv_img)
#    cv2.imshow("output2", opencv_template)
#    cv2.waitKey(0)

    #print(type(img_gray))
    #print(type(opencv_template))

    res = cv2.matchTemplate(img_gray, opencv_template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.85
    loc = np.where(res >= threshold)

    for pos in zip(*loc[::-1]):
        return True
    return False

def testBuyPhase(region,template):
    #if matchTemplate(region, template): print("State: Buy Phase")
    return matchTemplate(region, template)

def testWin(region,template):
    #if matchTemplate(region, template): print("State: Round Win")
    return matchTemplate(region, template)

def testLoss(region,template):
    #if matchTemplate(region, template): print("State: Round Loss")
    return matchTemplate(region, template)

def testThrifty(region,template):
    #if matchTemplate(region, template): print("State: Thrifty")
    return matchTemplate(region, template)

def testAce(region, template):
    pass

def testFlawless(region, template):
    #if matchTemplate(region, template): print("State: Flawless")
    return matchTemplate(region, template)

def testDeath(region, template):
    #if matchTemplate(region, template): print("State: Death Spectate")
    return matchTemplate(region, template)

def testSpikerush(region, template):
    #if matchTemplate(region, template): print("State: Spike Rush Spawn")
    return matchTemplate(region, template)


def testScoreboard(region, template):
    pass

def playMusic():
    win32api.keybd_event(0xB2, 0)
    sleep(.2)
    win32api.keybd_event(0xB3, 0)

def pauseMusic():
    win32api.keybd_event(0xB2, 0)
    sleep(.1)

if __name__=="__main__":

    buffer = 0
    play = False
    prevCond = " "

    while True:
        currentProgram = GetWindowText(GetForegroundWindow())

        if currentProgram == "VALORANT  ":

            screenshot = ImageGrab.grab()

            r1 = getRegion1(screenshot)
            r2 = getRegion2(screenshot)
            r3 = getRegion3(screenshot)

            loss = testLoss(r1, "loss")
            win = testWin(r1, "win")
            buyphase = testBuyPhase(r1, "buyphase")
            death = testDeath(r2, "death")
            spikerush = testSpikerush(r3, "spikerush")
            flawless = testFlawless(r1, "flawless")
            thrifty = testThrifty(r1, "thrifty")

            conditions = {
                "loss": loss,
                "win": win,
                "buyphase": buyphase,
                "death": death,
                "spikerush": spikerush,
                "flawless": flawless,
                "thrifty": thrifty
            }

            for k,v in conditions.items():
                if v is True and k != prevCond:
                    prevCond = k
                    print(f"Current State: {k}")
                    break

            if (loss or win or buyphase or death or spikerush or flawless or thrifty) and buffer <6 :
                buffer+=1
            elif not(loss or win or buyphase or death or spikerush or flawless or thrifty and buffer) and buffer > 0:
                buffer-=1

            if buffer == 6 and play == False:
                print("Playing Music\n")
                play = True
                playMusic()
            elif buffer == 0 and play == True:
                print("Pausing Music\n")
                play = False
                pauseMusic()
            else:
                print(f"Buffer: {buffer}")
                print(f"Play: {play}\n")

        sleep(.20)
