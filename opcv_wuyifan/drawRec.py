# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 10:20:56 2018

@author: Administrator
"""

import numpy as np
import cv2

frame = cv2.imread('test001.jpg')
hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
# 设定蓝色的阈值
#20 153 255
#lower_blue=np.array([110,50,50])
#upper_blue=np.array([130,255,255])
lower_blue=np.array([0,50,70])
upper_blue=np.array([50,200,200])
    
# 根据阈值构建掩模
mask=cv2.inRange(hsv,lower_blue,upper_blue)
    
# 对原图像和掩模进行位运算
res=cv2.bitwise_and(frame,frame,mask=mask)
    
# 显示图像
cv2.imshow('frame',frame)
cv2.imshow('mask',mask)
cv2.imshow('res',res)



