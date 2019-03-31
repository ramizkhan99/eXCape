import cv2
import numpy as np

cap = cv2.VideoCapture(0)
kernel1 = np.ones((2,2),np.uint8)
kernel2 = np.ones((10,10),np.uint8)
kernel3 = np.ones((5,5),np.uint8)
for i in range(1):
    _, frame = cap.read()
    height, width = frame.shape[:2]
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_red = np.array([30,150,50])
    upper_red = np.array([255,255,180])
    
    
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame,frame, mask= mask)
    dilation = cv2.erode(mask,kernel1,iterations = 3)
    smoothed = cv2.filter2D(dilation,-1,kernel2)
    opening = cv2.morphologyEx(smoothed, cv2.MORPH_OPEN, kernel3)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel1)
    M = cv2.moments(closing)
    try:
        cXref = int(M["m10"] / M["m00"])
        cYref = int(M["m01"] / M["m00"])
    except:
        i-=1

while(1):
    _, frame = cap.read()
    height, width = frame.shape[:2]
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_red = np.array([30,150,50])
    upper_red = np.array([255,255,180])
    
    
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame,frame, mask= mask)
    dilation = cv2.erode(mask,kernel1,iterations = 3)
    smoothed = cv2.filter2D(dilation,-1,kernel2)
    opening = cv2.morphologyEx(smoothed, cv2.MORPH_OPEN, kernel3)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel1)
    M = cv2.moments(closing)
    
 
    try:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        if(cY>cYref+10):
            print("fire")
    except:
        continue;
    
    # if cv2.countNonZero(closing)>500:
    #     print("stop")
    cv2.imshow('opening',closing)
    cv2.imshow('frame',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
cap.release()