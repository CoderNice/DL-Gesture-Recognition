# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 23:13:26 2018

@author: Administrator
"""

import cv2
import numpy as np

<<<<<<< HEAD
img = cv2.imread('test001.jpg')
print(img.shape)
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 127, 255,0)
image, contours, hierarchy = cv2.findContours(thresh,2,1)
=======
im = cv2.imread('test001.jpg')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255,0)
img,contours,hierarchy = cv2.findContours(thresh,2,1)
>>>>>>> 2a8d9f0342419fb3b8ecb8e4b53b5808cb387ac9
cnt = contours[0]
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
