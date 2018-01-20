import cv2
import numpy as np
img = cv2.imread('thumb.jpg')

# 转换到HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 设定蓝色的阈值
lower_blue = np.array([0, 50, 70])
upper_blue = np.array([50, 200, 200])

# 根据阈值构建掩模
mask = cv2.inRange(hsv, lower_blue, upper_blue)

image, contours, hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]
x,y,w,h = cv2.boundingRect(cnt)
img = cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
difference=img-mask
cv2.imshow('mask',mask)
cv2.imshow('img',img)
cv2.imshow('diff',difference)
#cv2.imwrite('maskContour',mask)
#cv2.imwrite('maskContour',mask)
cv2.waitKey(0)
cv2.destroyAllWindows()