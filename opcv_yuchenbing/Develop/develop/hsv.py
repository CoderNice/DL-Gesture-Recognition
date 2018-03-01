# -*- coding: utf-8 -*-
"""

@author: Nice
"""
import cv2
import numpy as np

import time

#import imutils

#import imutils

cap=cv2.VideoCapture(0)
time.sleep(2)

import imutils
import time

cap=cv2.VideoCapture(0)
time.sleep(1)

while(1):
# 获取每一帧
    ret,frame=cap.read()

    #frame = imutils.resize(frame, width = 1000)

<<<<<<< HEAD
    #frame = imutils.resize(frame, width = 1000)
=======
    frame = imutils.resize(frame, width = 1000)
>>>>>>> 50505e320aed141a6084ddba0df59ef62fd62f43

    # 转换到HSV
    #print(frame)
    converted=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
<<<<<<< HEAD
=======

    #转换到gray
    imgray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

>>>>>>> 50505e320aed141a6084ddba0df59ef62fd62f43
    # 设定蓝色的阈值
    lower = np.array([0, 48, 80],dtype = "uint8")
    upper = np.array([20, 255, 255],dtype = "uint8")

    # 根据阈值构建掩模
    skinMask=cv2.inRange(converted,lower,upper)

    #自适应阈值
    #th2 = cv2.adaptiveThreshold(mask,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)

    # 对原图像和掩模进行位运算
    #res=cv2.bitwise_and(frame,frame,mask=mask)

    #kernel = np.ones((5,5),np.uint8)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))

    #方法1：开运算(相当于腐蚀膨胀)
    skinMask = cv2.morphologyEx(skinMask, cv2.MORPH_OPEN, kernel)

    #方法2：腐蚀膨胀
    #skinMask = cv2.erode(skinMask, kernel, iterations = 1)
    #skinMask = cv2.dilate(skinMask, kernel, iterations = 1)
    #dilation1 = cv2.dilate(skinMask,kernel,iterations = 1)
    #erosion1 = cv2.erode(dilation1,kernel,iterations = 1)


    #方法3：闭运算（噪声很大...）
    #skinMask = cv2.morphologyEx(skinMask, cv2.MORPH_CLOSE, kernel)


    skinMask = cv2.GaussianBlur(skinMask, (3, 3), 0)
    #skin = cv2.bitwise_and(frame, frame, mask = skinMask)


    ret,thresh = cv2.threshold(imgray,127,255,0)
    image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cnt = contours[0]
    rect = cv2.minAreaRect(cnt)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    im = cv2.drawContours(skinMask,[box],0,(255,0,255),2)
    cv2.imshow("images", skinMask)
    # 显示图像
    #cv2.imshow('frame',frame)
    #cv2.imshow('ero',erosion1)
    #cv2.imshow('dila',dilation1)
    #cv2.imshow('res',res)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
<<<<<<< HEAD
cv2.destroyAllWindows()

=======

cv2.destroyAllWindows()
>>>>>>> 50505e320aed141a6084ddba0df59ef62fd62f43
