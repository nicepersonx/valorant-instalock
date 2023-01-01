import keyboard
import win32api, win32con
import pyautogui
import time
import colored
import os
from random import randint
from screeninfo import get_monitors


white = colored.fg(15)
pink = colored.fg(219)
lime = colored.fg(46)


def lc():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep((randint(48,72)/1000))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


def setup():
    os.system('cls')
    print('Open valorant and go into a custom game by yourself.')
    print("Don't press space unless instructed during this process.")
    print('Once ready, press space to continue...')
    keyboard.wait('space')
    os.system('cls')
    print('Hold your mouse over the lock in button and press space...')
    keyboard.wait('space')
    f = open("config.txt", "a")
    f.write(str(pyautogui.position()[0]) + "," + str(pyautogui.position()[1]))
    f.close()
    print("Done.")
    print("Press space to continue.")
    keyboard.wait('space')
    run()


def run():
    os.system('cls')
    print(colored.fg(14) + "nicepersonx instalock v2")
    print(pink + "Script running. Instalock: " + lime + "ON")
    white + ("To turn it off just close this terminal.")
    f = open("config.txt", "r")
    config = str(f.read())
    tpval = (int(config.split(',')[0]),int(config.split(',')[1]))
    for m in get_monitors():
        if m.is_primary:
            placey = int((int(m.height)*0.8149))
            leny = int((int(m.height))*0.1537037038)
            placex = int((int(m.width))*0.28125)
            lenx = int((int(m.width))*0.43489583334)
        count = 0
    while True:
        n = pyautogui.locateOnScreen('agent.png', region=(placex,placey,lenx,leny))
        if n != None:
            win32api.SetCursorPos((n[0],n[1]))
            time.sleep(0.015)
            lc()
            time.sleep(0.01)
            win32api.SetCursorPos(tpval)
            time.sleep(0.015)
            lc()
            count+=1
            os.system('cls')
            print(colored.fg(14) + "nicepersonx instalock v2\n\n")
            print(pink + "Script running. Instalock: " + lime + "ON")
            print(white + "Instalocked " + lime + str(count) + white + " times.")
            time.sleep(8)


f = open("config.txt", "r")
if f.read() == "":
    setup()
else:
    run()
