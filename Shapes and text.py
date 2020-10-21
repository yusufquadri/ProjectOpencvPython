import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
#print(img)

#cv2.line(img,(0,0),(300,300),(0,255,0),4)
cv2.line(img,(0,0),(img.shape[0],img.shape[1]),(0,255,255),4)
cv2.rectangle(img,(0,60),(250,350),(255,255,14),cv2.FILLED)
cv2.circle(img,(400,50),30,(255,233,145),5)
cv2.putText(img," Size and Shape ",(30,100),cv2.FONT_ITALIC,1,(0,150,0),5)
#img[200:300,100:300]=255,0,0
cv2.imshow("Black Image",img)
cv2.waitKey(0)

