# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 14:40:10 2018

@author: Administrator
"""

import cv2
import numpy as np
import time
#import imutils

#import imutils

cap=cv2.VideoCapture(0)
time.sleep(3)
while(1):
# 获取每一帧
    ret,frame=cap.read()
    #print(frame)
    #frame = imutils.resize(frame, width = 1000)

    #frame = imutils.resize(frame, width = 1000)
    # 转换到HSV
    converted=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    #转换到gray
    imgray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

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
    skinMask = cv2.erode(skinMask, kernel, iterations = 2)
    skinMask = cv2.dilate(skinMask, kernel, iterations = 2)
    #dilation1 = cv2.dilate(skinMask,kernel,iterations = 1)
    #erosion1 = cv2.erode(dilation1,kernel,iterations = 1)
    skinMask = cv2.GaussianBlur(skinMask, (3, 3), 0)
    #skin = cv2.bitwise_and(frame, frame, mask = skinMask)

    
    ret,thresh = cv2.threshold(imgray,127,255,0)
    image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    #cnt = contours[0]
    '''
    #print(cnt)
    rect = cv2.minAreaRect(cnt)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    im = cv2.drawContours(skinMask,[box],0,(0,255,255),2)
    '''
    #x,y,w,h = cv2.boundingRect(cnt)
    #frame = cv2.rectangle(skinMask,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("images", skinMask)
    # 显示图像
    #cv2.imshow('frame',frame)
    #cv2.imshow('ero',erosion1)
    #cv2.imshow('dila',dilation1)
    #cv2.imshow('res',res)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()

cv2.destroyAllWindows()
