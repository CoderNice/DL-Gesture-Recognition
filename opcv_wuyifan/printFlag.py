<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 15:19:50 2018

@author: Administrator
"""

import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while(1):
    # 获取每一帧
    ret,frame=cap.read()
    
    # 转换到 HSV
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    # 设定蓝色的阈值
    #20 153 255
    #lower_blue=np.array([110,50,50])
    #upper_blue=np.array([130,255,255])
    lower_blue=np.array([0,50,70])
    upper_blue=np.array([50,200,200])
    
    # 根据阈值构建掩模
    mask=cv2.inRange(hslower = np.array([0, 48, 80])
    upper = np.array([20, 255, 255])v,lower_blue,upper_blue)
    kernel = np.ones((5,5),np.uint8)
    erosion = cv2.dilate(mask,kernel,iterations = 1)
    dilation = cv2.erode(erosion,kernel,iterations = 1)
    
    # 对原图像和掩模进行位运算
    res=cv2.bitwise_and(frame,frame,mask=mask)
    #cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('erosion',erosion)
    #cv2.imshow('dilati
    
    # 显示图像on',dilation)
    #cv2.imshow('res',res)
    k=cv2.waitKey(5)&0xFF
    if k==27:
        break
    
# 关闭窗口
cv2.destroyAllWindows()
=======
import cv2
import numpy as np

img=cv2.imread('00224.jpg',0)
img2=img[100:200,0:100]
print(type(img))
#cv2.imshow(img,'img')
#cv2.imshow(img2)
>>>>>>> parent of 90c774f... 增加一个gui窗口
