# -*- coding: utf-8 -*-
"""

@author: Nice
"""
import cv2
import numpy as np
cap=cv2.VideoCapture(0)
while(1):
# 获取每一帧
    ret,frame=cap.read()
    # 转换到HSV
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    #转换到GREY
    imgray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # 设定蓝色的阈值
    lower_blue = np.array([0, 50, 70])
    upper_blue = np.array([50, 200, 200])

    # 根据阈值构建掩模
    mask=cv2.inRange(hsv,lower_blue,upper_blue)

    #自适应阈值
    #th2 = cv2.adaptiveThreshold(mask,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)

    # 对原图像和掩模进行位运算
    #res=cv2.bitwise_and(frame,frame,mask=mask)

    kernel = np.ones((5,5),np.uint8)

    dilation1 = cv2.dilate(mask,kernel,iterations = 1)
    erosion1 = cv2.erode(dilation1,kernel,iterations = 1)



    # 显示图像
    #cv2.imshow('frame',frame)
    #cv2.imshow('ero',erosion1)
    cv2.imshow('dila',dilation1)
    #cv2.imshow('res',res)
    k=cv2.waitKey(5)&0xFF
    if k==27:
        break
# 关闭窗口
cv2.destroyAllWindows()