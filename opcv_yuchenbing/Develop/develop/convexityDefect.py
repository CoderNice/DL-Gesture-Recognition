# -*- coding: utf-8 -*-
"""

@author: Nice
"""
import cv2
import numpy as np
img_gray = cv2.imread('thumb.jpg')
img_gray = cv2.cvtColor(img_gray,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 127, 255,0)
image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]
x,y,w,h = cv2.boundingRect(cnt)
img = cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)

'''
hull = cv2.convexHull(cnt,returnPoints = False)
defects = cv2.convexityDefects(cnt,hull)
for i in range(defects.shape[0]):
    s,e,f,d = defects[i,0]
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    cv2.line(img_gray,start,end,(255,255,0),2)
    cv2.circle(img_gray,far,5,(0,0,255),5)
'''

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

