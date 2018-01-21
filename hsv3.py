# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 15:12:53 2018

@author: Administrator
"""

import cv2
import time
 
camera = cv2.VideoCapture(0)
if camera is None:
    print('请先连接摄像头')
    exit()
 
fps = 5 # 帧率
pre_frame = None  # 总是取前一帧做为背景（不用考虑环境影响）
 
play_music = False
count=0 

while True:
    start = time.time()
    res, cur_frame = camera.read()
    if res != True:break
    end = time.time()
    seconds = end - start
    if seconds < 1.0/fps:
        time.sleep(1.0/fps - seconds)
    """
    cv2.imshow('img', cur_frame)
    key = cv2.waitKey(30) & 0xff
    if key == 27:
        break
    """
    
    #print('读取了一帧')
    gray_img = cv2.cvtColor(cur_frame, cv2.COLOR_BGR2GRAY)
    gray_img = cv2.resize(gray_img, (500, 500))
    gray_img = cv2.GaussianBlur(gray_img, (21, 21), 0)
 
    if pre_frame is None:
        pre_frame = gray_img
    else:
        img_delta = cv2.absdiff(pre_frame, gray_img)
        thresh = cv2.threshold(img_delta, 25, 255, cv2.THRESH_BINARY)[1]
        thresh = cv2.dilate(thresh, None, iterations=2)
        image, contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        flag=True
        for c in contours:
            if cv2.contourArea(c) > 1000: # 设置敏感度
                print('动了')
                flag=False
                count=0
                continue
            else:
                #print(cv2.contourArea(c))
                #print("前一帧和当前帧一样了, 有什么东西不动!")
                play_music = True
                break
        if flag:
            count+=1
        if count==10:
            count=0
            print('调用了神经网络')
        pre_frame = gray_img
 
camera.release()
cv2.destroyAllWindows()