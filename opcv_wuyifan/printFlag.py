import cv2
import numpy as np

img=cv2.imread('00224.jpg',0)
img2=img[100:200,0:100]
print(type(img))
#cv2.imshow(img,'img')
#cv2.imshow(img2)