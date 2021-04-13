from cv2 import cv2
import numpy as np
import pynput
from pynput.mouse import Button, Controller
import pyautogui
import time

mouse = Controller()
h, w = pyautogui.size()
mouse.position = (h/2, w/2)
print((h/2, w/2))
cap = cv2.VideoCapture(0)
kernel1 = np.ones((2,2),np.uint8)
kernel2 = np.ones((10,10),np.uint8)
kernel3 = np.ones((5,5),np.uint8)
watch=cv2.CascadeClassifier('haarcascade_eye.xml')
xref = 300

while(1):
    _, frame = cap.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    eyes = watch.detectMultiScale(gray,1.3,5)
    try:
        mid = (eyes[0][0]+eyes[1][0])/2
        if(mid>xref+20):
            print("left")
            time.sleep(0.01)
            mouse.move(-10, 0)
        elif(mid<xref-20):
            print("right")
            time.sleep(0.01)
            mouse.move(10, 0)
        else:
            print("front")
            time.sleep(0.01)
            mouse.position = (h/2, w/2)
    except:
        continue
    height, width = frame.shape[:2]
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_red = np.array([255,255,0])
    upper_red = np.array([255,255,150])
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame,frame, mask= mask)
    dilation = cv2.erode(mask,kernel1,iterations = 3)
    smoothed = cv2.filter2D(dilation,-1,kernel2)
    opening = cv2.morphologyEx(smoothed, cv2.MORPH_OPEN, kernel3)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel1)
    if cv2.countNonZero(closing)>80:
        print("stop")
    

    # cv2.imshow('frame',mask)
    cv2.imshow('opening',closing)
    # cv2.imshow('res',res)
    

    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
