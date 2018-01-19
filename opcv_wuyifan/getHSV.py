# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 15:37:45 2018

@author: Administrator
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 20:34:29 2014
@author: duan
"""
import cv2
import numpy as np

green=np.uint8([[[47,70,104]]])
hsv_green=cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
print(hsv_green)
