import time
import pyautogui as pyautogui
count = 0

circle = True

while circle:
    print(count)
    count += 1
    time.sleep(0.5)
    pyautogui.keyDown('ctrl')
    pyautogui.press('l')
    pyautogui.keyUp('ctrl')
    if count == 10:
        circle = False