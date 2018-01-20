# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 14:19:29 2014
@author: duan
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('thumb.jpg',0)
# 中值滤波
img = cv2.medianBlur(img,5)
ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
#11 为Block size, 2 为C 值

th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
#阈值取自相邻区域的平均值

th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
cv2.THRESH_BINARY,11,2)
#阈值取值相邻区域的加权和，权重为一个高斯窗口。

titles = ['Original Image', 'Global Thresholding (v = 127)',
'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]
for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()