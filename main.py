import pyautogui
import time
import getpixelcolor
w, h = pyautogui.size()
class Jump:
    def short_press():
        pyautogui.keyDown("space")
        time.sleep(0.1)
        pyautogui.keyUp("space")
    def long_press():
        pyautogui.keyDown("space")
        time.sleep(0.75)
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

print(w, h)
print(getpixelcolor.pixel(156, 227))





