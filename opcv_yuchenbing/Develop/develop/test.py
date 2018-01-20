# -*- coding: utf-8 -*-
"""

@author: Nice
"""
import cv2
from matplotlib import pyplot as plt
import numpy as np

im = cv2.imread('image/thumb.jpg')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
image = cv2.drawContours(image, contours, 2, (0,0,255), 3)
cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()