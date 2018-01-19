# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 20:49:42 2018

@author: Administrator
"""

import numpy as np
import cv2

img = cv2.imread('test001.jpg')
#转换成灰度图
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#cv2.imwrite('messigray.png',imgray)
#区分？
ret,thresh = cv2.threshold(imgray,127,255,0)
cv2.imwrite('thresh127 0.png',thresh)
kernel = np.ones((5,5),np.uint8)
thresh = cv2.erode(thresh,kernel,iterations = 1)
cv2.imwrite('thresh127 1.png',thresh)
#cv2.imwrite('thresh127.png',thresh)

image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE )
#cv2.imwrite('image_find2.png',image)
#img = cv2.drawContour(img, contours, -1, (0,255,0), 3)
cnt = contours[0]
'''
cnt = contours[0]
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
img = cv2.drawContours(img,[box],0,(0,0,255),2)
'''
#img = cv2.drawContours(im, contours, 3, (0,255,0), 3)


hull = cv2.convexHull(cnt,returnPoints = False)
defects = cv2.convexityDefects(cnt,hull)
for i in range(defects.shape[0]):
    s,e,f,d = defects[i,0]
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    cv2.line(img,start,end,[0,255,0],2)
    cv2.circle(img,far,5,[0,0,255],-1)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#cv2.imshow('image-grey',imgray)
#cv2.imshow('image',img)















