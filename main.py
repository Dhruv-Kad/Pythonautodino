import pyautogui
import time
import getpixelcolor
import keyboard
import os
import webbrowser

class Jump:
    def short_press():
        pyautogui.keyDown("space")
        time.sleep(0.001)
        pyautogui.keyUp("space")
    def long_press():
        pyautogui.keyDown("space")
        time.sleep(0.01)
        pyautogui.keyUp("space")

class Crouch:
    def short_crouch():
        pyautogui.keyDown("down")
        time.sleep(0.1)
        pyautogui.keyUp("down")
    def long_crouch():
        pyautogui.keyDown("down")
        time.sleep(0.75)
        pyautogui.keyUp("down")

def clear_terminal():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS and Linux
    else:
        os.system('clear')

#To open the dino game

#webbrowser.open("https://chromedino.com/#google_vignette")


BLACK = 83
WHITE = 247

time.sleep(5)
pyautogui.press('space')

while True:
    x = 248
    y = 420
    r, g, b = getpixelcolor.pixel(x, y)
    if r != WHITE:
        Jump.short_press()
    else:
        pass

    if keyboard.is_pressed('s'):
        break

    #This is to find the mouse position
    '''
    clear_terminal()
    x, y = pyautogui.position()
    print(x, y)
    if keyboard.is_pressed('s'):
        break '''







