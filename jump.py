import cv2
import numpy as np

cap = cv2.VideoCapture(0)
kernel1 = np.ones((2,2),np.uint8)
kernel2 = np.ones((10,10),np.uint8)
kernel3 = np.ones((5,5),np.uint8)
watch=cv2.CascadeClassifier('haarcascade_eye.xml')
for i in range(1):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    eyes = watch.detectMultiScale(gray,1.3,5)
    xref=(eyes[0][0]+eyes[1][0])/2

while(1):
    _, frame = cap.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    eyes = watch.detectMultiScale(gray,1.3,5)
    try:
        mid = (eyes[0][0]+eyes[1][0])/2
        if(mid>xref+20):
            print("left")
        if(mid<xref-20):
            print("right")
        else:
            print("front")
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