from tkinter import *
import gameStateDetector as main
from win32gui import GetWindowText, GetForegroundWindow
from PIL import ImageGrab
from time import sleep

#variables
window = Tk()
loss, win, buyphase, death, spikerush, flawless, thrifty = StringVar(), StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()
bufferStr, playStr = StringVar(),StringVar()
prevCond = None

lossBool, winBool, buyphaseBool, deathBool, spikerushBool, flawlessBool, thriftyBool = None, None, None, None, None, None, None

#properties
darkgrey = "#27292b"

window.title("Valorant Automatic Music Player")
window.geometry("550x350")
window.config(bg=darkgrey)
window.resizable(0,0)


#components
Label(window, text="Make sure Valorant is running on primary monitor (Monitor #1 in Video Settings)", bg = darkgrey, fg = "red", font="Arial 10 bold", height = 2).grid(row=1, column=0, sticky=S)
Label(window, text="For best results, set UI quality to LOW or MEDIUM", bg = darkgrey, fg = "red", font="Arial 10 bold", height = 2).grid(row=0, column=0, sticky=S)
Label(window, text="Valorant MUST be running at 1920x1080 resolution", bg = darkgrey, fg = "red", font="Arial 10 bold", height = 2).grid(row=2, column=0, sticky=S)

Label(window, textvariable=loss, bg = darkgrey, fg = "white", font="Arial 10 bold", height = 1).grid(row=3, column=0, sticky=SW)
Label(window, textvariable=win, bg = darkgrey, fg = "white", font="Arial 10 bold", height = 1).grid(row=4, column=0, sticky=SW)
Label(window, textvariable=buyphase, bg = darkgrey, fg = "white", font="Arial 10 bold", height = 1).grid(row=5, column=0, sticky=SW)
Label(window, textvariable=death, bg = darkgrey, fg = "white", font="Arial 10 bold", height = 1).grid(row=6, column=0, sticky=SW)
Label(window, textvariable=spikerush, bg = darkgrey, fg = "white", font="Arial 10 bold", height = 1).grid(row=7, column=0, sticky=SW)
Label(window, textvariable=flawless, bg = darkgrey, fg = "white", font="Arial 10 bold", height = 1).grid(row=8, column=0, sticky=SW)
Label(window, textvariable=thrifty, bg = darkgrey, fg = "white", font="Arial 10 bold", height = 1).grid(row=9, column=0, sticky=SW)

Label(window, textvariable=playStr, bg = darkgrey, fg = "gray", font="Arial 10 bold", height = 1).grid(row=3, column=0, sticky=SE)
Label(window, textvariable=bufferStr, bg = darkgrey, fg = "gray", font="Arial 10 bold", height = 1).grid(row=4, column=0, sticky=SE)


skipNext = False
skipnextButton = Checkbutton(window, variable = skipNext, text = "Forward on play?", bg=darkgrey, activebackground = darkgrey, highlightcolor="black", fg="red", activeforeground="red", offvalue = False, onvalue = True, height = 5, width = 20)
skipnextButton.grid(row = 10, column = 0, sticky = W)


img = PhotoImage(file ="GUIassets/playbutton.png")
B = Button(window, image = img, command=main.playMusic)
B.grid(row = 10)

#mainloop
buffer = 0
play = False
musicPlaying = False
prevCond = " "


while True:
    currentProgram = GetWindowText(GetForegroundWindow())

    try:
        window.update_idletasks()
        window.update()
    except:
        pass

    if currentProgram == "VALORANT  ":

        screenshot = ImageGrab.grab()

        r1 = main.getRegion1(screenshot)
        r2 = main.getRegion2(screenshot)
        r3 = main.getRegion3(screenshot)

        lossBool = main.testLoss(r1, 'loss')
        loss.set(f"Loss: {lossBool}")

        winBool = main.testWin(r1, 'win')
        win.set(f"Win: {winBool}")

        buyphaseBool = main.testBuyPhase(r1, 'buyphase')
        buyphase.set(f"Buyphase: {buyphaseBool}")

        deathBool = main.testDeath(r2, 'death')
        death.set(f"Death: {deathBool}")

        spikerushBool = main.testSpikerush(r3, 'spikerush')
        spikerush.set(f"Spikerush: {spikerushBool}")

        flawlessBool = main.testFlawless(r1, 'flawless')
        flawless.set(f"Flawless: {flawlessBool}")

        thriftyBool = main.testThrifty(r1, 'thrifty')
        thrifty.set(f"Thrifty: {thriftyBool}")

        playStr.set(f"Should Music Be Playing?: {not(play)}")
        bufferStr.set(f"Buffer: {buffer}")

        if (lossBool or winBool or buyphaseBool or deathBool or spikerushBool or flawlessBool or thriftyBool) and buffer<10:
            buffer+=1

        elif not(lossBool or winBool or buyphaseBool or deathBool or spikerushBool or flawlessBool or thriftyBool) and buffer>0:
            buffer-=1


        if buffer == 10 and play == True:
            main.playMusic()
            play = False
        elif buffer == 0 and play == False:
            main.pauseMusic()
            play = True

    sleep(.20)
