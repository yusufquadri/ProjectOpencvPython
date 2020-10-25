import numpy as np
import cv2
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(1)

while True:
    _,frame = cap.read()
    hsv1 = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower_red = np.array([0,0,0])
    upper_red = np.arrray([255,255,255])

    mask = cv2.inRange(hsv1,lower_red,upeer_red)
    res = cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    k=cv2.waitKey(5) & 0xff
    if k == 27:
        break

cv2.destroyWindow()
cap.release()