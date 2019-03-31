from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import numpy as np
import cv2

keyboard = KeyboardController()
mouse = MouseController()

fist = cv2.CascadeClassifier('aGest.xml')



cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    fists=fist.detectMultiScale(gray, 1.3, 5)
    if len(fists)!=0:
        print("stop")
        mouse.position = (50, 70)
        mouse.press(Button.left)
        mouse.release(Button.left)
        keyboard.press('s')
        keyboard.release('s')



    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()