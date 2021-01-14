from PIL import ImageGrab
from win32gui import GetWindowText, GetForegroundWindow
from time import sleep
import win32api

class GameStateDetector():

    def __init__(self):
        self.curState = " "
        self.play = True


    def printState(self, newState):

        if self.curState is not newState:
            print(newState)
            self.curState=newState


    def testDeath(self):
        #white (140, 870) blue (136, 860) (Blue RGB: 170, 237, 225)

        #print(ImageGrab.grab().getpixel((140, 870)))
        #print(ImageGrab.grab().getpixel((136, 860)))

        if sum(ImageGrab.grab().getpixel((140, 870)))/3 > 250 and ImageGrab.grab().getpixel((136, 860)) == (170, 237, 225):
            self.printState("State: Death")
            self.play = True

            return True
        return False

    def testWinLoss(self):
        #(835, 137) and (1080, 273)

        #print(sum(ImageGrab.grab().getpixel((835, 137))))
        #print(sum(ImageGrab.grab().getpixel((1080, 274))))

        if sum(ImageGrab.grab().getpixel((835, 137))) > 755 and sum(ImageGrab.grab().getpixel((1080, 273))) > 755 :
            self.printState("State: Win/Loss")
            self.play = True

            return True
        return False

    def testScoreboard(self):
        #(583, 522) and (583, 554)

        if ImageGrab.grab().getpixel((583, 522)) == (255,255,255) and ImageGrab.grab().getpixel((583, 554)) == (252,252,252):
            self.printState("State: Scoreboard")
            self.play = True

            return True
        return False

    def testShop(self):
        pass

    def testBuyPhase(self):
        #(983, 200) and (850, 200)

       # print(sum(ImageGrab.grab().getpixel((983, 200))))
       # print(sum(ImageGrab.grab().getpixel((850, 200))))
       # print(sum(ImageGrab.grab().getpixel((1069, 200))))
       # print("\n")

        if (sum(ImageGrab.grab().getpixel((983, 200))) + sum(ImageGrab.grab().getpixel((850, 200))) + sum(ImageGrab.grab().getpixel((1069, 200))))/3 > 710:
            self.printState("State: Buy Phase")
            self.play = True

            return True
        return False


    def testSpikeRushSpawn(self):
        #(910,135) and (1000,135) and (755, 275) and (1165, 275)

        #print(sum(ImageGrab.grab().getpixel((910,135))))
        #print(sum(ImageGrab.grab().getpixel((1000,135))))
        #print(sum(ImageGrab.grab().getpixel((755, 275))))
        #print(sum(ImageGrab.grab().getpixel((1165, 275))))

        if sum(ImageGrab.grab().getpixel((910,135))) == 765 and sum(ImageGrab.grab().getpixel((1000,135))) == 765 and sum(ImageGrab.grab().getpixel((755, 275))) == 765 and sum(ImageGrab.grab().getpixel((1165, 275))) == 765:

            self.printState("State: Spike Rush Spawn")
            self.play = True

            return True
        return False


def play():
    win32api.keybd_event(0xB2, 0)
    sleep(.1)
    win32api.keybd_event(0xB3, 0)

def pause():
    win32api.keybd_event(0xB2, 0)

if __name__ == "__main__":
    buffer = [0] * 5

    print("Started")

    gsd = GameStateDetector()
    play = True

    while True:
        sleep(.25)

        currentProgram = GetWindowText(GetForegroundWindow())

        if currentProgram == "VALORANT  ":

            if gsd.testWinLoss() or gsd.testBuyPhase() or gsd.testDeath() or gsd.testSpikeRushSpawn():
                buffer.append(1)
                buffer.pop(0)
            else:
                buffer.append(0)
                buffer.pop(0)


            if sum(buffer) != 0 and play is False:
                play = True
                print("Playing Music\n")
                play()
            elif sum(buffer) == 0 and play is True:
                print("Pausing Music\n")
                play = False
                pause()
