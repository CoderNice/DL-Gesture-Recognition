import cv2

img=cv2.imread('black.jpg',0)
img1=img[100:200,100:300]
cv2.imshow('img1',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()