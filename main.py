import pyautogui
import time
import getpixelcolor
import webbrowser

class Jump:
    def short_press(): 
        pyautogui.keyDown("space")
        pyautogui.keyUp("space") 
    def long_press():
        pyautogui.keyDown("space")
        time.sleep(0.001)
        pyautogui.keyUp("space")

class Crouch:
    def short_crouch():
        pyautogui.keyDown("down")
        time.sleep(0.1)
        pyautogui.keyUp("down")
    def long_crouch():
        pyautogui.keyDown("down")
        time.sleep(0.001)
        pyautogui.keyUp("down")

#To open the dino game

webbrowser.open("https://chromedino.com/#google_vignette")


BLACK = 83
WHITE = 247

time.sleep(3)
pyautogui.press('space')

x = 310
y = 425
x2 = 290
y2 = 385

dino_x = 148
dino_y = 428


while True:
    r, g, b = getpixelcolor.average(x2, y, 55, 1)
    r2, g2, b2, = getpixelcolor.average(x2, y2, 55, 1) 
    #r2, g2, b2 = getpixelcolor.pixel(x2, y)
    dino_r, dino_g, dino_b = getpixelcolor.pixel(dino_x, dino_y)
    game_over_r, game_over_g, game_over_b = getpixelcolor.pixel(423, 334)

    if r != WHITE:
        if dino_r != WHITE:
            Jump.short_press()
        else:
            time.sleep(0.1)
            Jump.short_press()  
    elif r2 != WHITE:
        Crouch.short_crouch()

    if game_over_r == BLACK:
        break

#Record: 611, Meeting Best: 201







