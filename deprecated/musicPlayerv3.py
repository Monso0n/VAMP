import pyautogui as pg
import time

width, height = pg.size()

pg.FAILSAFE = False

def testRoundEnd(): #tests for buy phase, round loss, and round win
    #print(pg.pixel(806, 137))

    if pg.pixelMatchesColor(806, 137, (255,255,255)):
        print("Detected Round Won/Loss")
        return True
    elif pg.pixelMatchesColor(140, 870, (255,255,255)):
        print("Detected Death")
        return True
    elif pg.pixelMatchesColor(919, 133, (255,255,255)):
        print("Detected Spawn Phase (Spike Rush)")
        return True

    return False

def testDeath():
    #print(pg.pixel(1612, 376))


    if pg.pixelMatchesColor(1612, 376, (255,255,255)) or pg.pixelMatchesColor(140, 876, (255,255,255)) :
        print("detected Death")
        #print("Detected White")

        return True

    return False


def playpause():
    pg.press('playpause')



if __name__=="__main__":

    play = False
    buffer = [0]*5

    print("Started")

    while True:
        time.sleep(.2)

        if testRoundEnd() or testDeath():
            buffer.append(1)
            buffer.pop(0)
        else:
            buffer.append(0)
            buffer.pop(0)

        if sum(buffer)!=0 and play==True:
            print("Round Start")
            print("Stopping Music\n")
            play = False
            playpause()
        elif sum(buffer)==0 and play==False:
            print("Round End Detected")
            print("Playing Music\n")
            play = True
            playpause()





