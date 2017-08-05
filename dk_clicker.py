# -*- coding: utf-8 -*-
import pyautogui, time
from pynput import keyboard

# ----------------------------------------------------------------
# Список переменных
img01 = "img\\but1_edit.png"
img02 = "img\\but2_panoram.png"
img03 = "img\\but3_onroad.png"
img04 = "img\\but4_cancel.png"
img05 = "img\\but5_save_add.png"
img06 = "C:\\a2projects\\python\\dkjob\\img\\but6_create.png"
img07 = "img\\but7_finddot.png"
img08 = "img\\but8_otmetit.png"
img09 = "img\\but9_done.png"
img10 = "img\\loginpic.png"
img11 = "img\\but10_closepanoram.png"


# ----------------------------------------------------------------
# Список функции
def dk_click(img, i1=0, k1=0, i2=1920, k2=1080, x=0, y=0):
    try:
        # pyautogui.screenshot('my_screenshot.png')
        mouseX, mouseY = pyautogui.position()
        buttonlocation = pyautogui.locateOnScreen(img, region=(i1, k1, i2, k2), grayscale=True)
        buttonX, buttonY = pyautogui.center(buttonlocation)
        pyautogui.click(buttonX + x, buttonY + y)
        pyautogui.moveTo(mouseX, mouseY, 0, 1)
        del buttonX, buttonY, img, i1, k1, i2, k2, x, y
        print("Ура! Нашел!")
    except TypeError:
        #    """ Do something to handle the fact that the image was not found"""
        print("Блять!Сука! Снова не работает!")
        pass


def dk_login():
    try:
        buttonx, buttony = pyautogui.locateCenterOnScreen(img10)
        pyautogui.click(buttonx, buttony - 20)
        pyautogui.typewrite('u43')
        pyautogui.click(buttonx, buttony + 20)
        pyautogui.typewrite('t29g')
        pyautogui.press('enter')
    except TypeError:
        print("No Exit")
        pass


# ----------------------------------------------------------------
# Код, чо
def on_press(key):
    try:
        button = '{0}'.format(key.char)
        if button == 'q':
            dk_click(img01, 10, 190, 70, 290)
        elif button == 'w':
            dk_click(img08, 10, 200, 120, 500)
        elif button == 'e':
            dk_click(img09, 10, 80, 250, 900)
        elif button == 'r':
            dk_click(img05, 5, 80, 250, 1000)
        elif button == 't':
            pyautogui.screenshot('screenshot_' + str(time.time()) + '.png')
        # pass
        elif button == 'a':
            dk_click(img02, 5, 80, 250, 900)
        elif button == 's':
            dk_click(img03, 5, 80, 250, 900)
        elif button == 'd':
            dk_click(img07, 376, 311, 1698, 1079)
        elif button == 'f':
            dk_click(img07, 376, 311, 1698, 1079, y=40)
            # dk_click(img11, 920, 520, 1300, 670)
        elif button == 'z':
            dk_click(img06, 10, 10, 291, 242)
        elif button == 'x':
            dk_click(img04, 5, 80, 250, 900)
        # elif button == 'c':
        #    pass
        # elif button == 'v':
        #    pass
        elif button == '0':
            dk_login()
            # dk_click(img01, 635, 79, 1331, 515)
    except AttributeError:
        # print('special key {0} pressed'.format(key))
        pass


def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False


# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
