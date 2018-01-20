# -*- coding: utf-8 -*-
"""

@author: Nice
"""
import cv2
from matplotlib import pyplot as plt
import numpy as np

im = cv2.imread('thumb.jpg')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
<<<<<<< HEAD
ret,th1 = cv2.threshold(imgray,127,255,cv2.THRESH_BINARY)
#image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
th2 = cv2.adaptiveThreshold(imgray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
#阈值取自相邻区域的平均值

th3 = cv2.adaptiveThreshold(imgray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
cv2.THRESH_BINARY,11,2)
#阈值取值相邻区域的加权和，权重为一个高斯窗口。
#11 为Block size, 2 为C 值



#image = cv2.drawContours(image, contours, 2, (0,255,0), 3)


#腐蚀#膨胀
kernel = np.ones((5,5),np.uint8)


erosion1 = cv2.erode(th1,kernel,iterations = 1)
dilation1 = cv2.dilate(erosion1,kernel,iterations = 1)
erosion2 = cv2.erode(th2,kernel,iterations = 1)
dilation2 = cv2.dilate(erosion2,kernel,iterations = 1)
erosion3 = cv2.erode(th3,kernel,iterations = 1)
dilation3 = cv2.dilate(erosion3,kernel,iterations = 1)
titles = ['original','erosion1','dilation1','erosion2','dilation2','erosion3','dilation3']
images = [imgray, erosion1, dilation1,erosion2, dilation2,erosion3, dilation3]

for i in range(7):

    plt.subplot(1,7,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()

=======
ret,thresh = cv2.threshold(imgray,127,255,1)
image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
image = cv2.drawContours(image, contours, 2, (0,0,255), 3)
kernel = np.ones((5,5),np.uint8)
erosion = cv2.dilate(image,kernel,iterations = 1)
dilation = cv2.erode(erosion,kernel,iterations = 1)
titles = ['Original Image','erosion','dilation']
images = [image, erosion, dilation]
cv2.imshow('orginal',image)
cv2.imshow('erosion',erosion)
cv2.imshow('dilation',dilation)
#for i in range(3):

 #   plt.subplot(1,3,i+1),plt.imshow(images[i],'gray')
#    plt.title(titles[i])
#    plt.xticks([]),plt.yticks([])
#plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
>>>>>>> 8669cbf1baaeddfdfc45b8d0b3e56f501edee2fa
