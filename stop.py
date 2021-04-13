import numpy as np
from cv2 import cv2


fist = cv2.CascadeClassifier('aGest.xml')



cap = cv2.VideoCapture(0)

while 1:
    ret, img1= cap.read()
    img = cv2.flip(img1,1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    fists=fist.detectMultiScale(gray, 1.3, 5)
    if len(fists)!=0:
        print("stop")


    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()