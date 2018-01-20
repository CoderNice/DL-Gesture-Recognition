# -*- coding: utf-8 -*-
"""

@author: Nice
"""
import cv2
from matplotlib import pyplot as plt
import numpy as np

im = cv2.imread('thumb.jpg')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
image = cv2.drawContours(image, contours, 2, (0,0,255), 3)
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(image,kernel,iterations = 1)
dilation = cv2.dilate(erosion,kernel,iterations = 1)
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
