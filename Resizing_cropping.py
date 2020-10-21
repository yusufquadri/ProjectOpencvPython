import cv2



img = cv2.imread("Resources/yusuf.jpg")
print(img.shape)

imgResize = cv2.resize(img,(1000,500))
imgCropped = img[0:200,200:500]
cv2.imshow("IMAGE",img)

#cv2.imshow("IMAGE",imgResize)
#cv2.waitKey(1000)


cv2.imshow("IMAGE Cropped",imgCropped)
cv2.waitKey(0)