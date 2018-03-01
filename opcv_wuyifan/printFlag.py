<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 15:19:50 2018

@author: Administrator
"""

=======
# -*- coding:utf-8 -*-
>>>>>>> parent of 78de438... Merge branch 'opencv' of https://github.com/CoderNice/DL-Gesture-Recognition into opencv
import cv2
import numpy as np

camera = cv2.VideoCapture(0) # 参数0表示第一个摄像头
# camera = cv2.VideoCapture("test.avi") # 从文件读取视频

# 判断视频是否打开
if (camera.isOpened()):
    print('Open')
else:
    print('Fail to open!')

# # 测试用,查看视频size
# size = (int(camera.get(cv2.CAP_PROP_FRAME_WIDTH)),
#        int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT)))
# print 'size:'+repr(size)

rectangleCols = 30
while True:
    grabbed, frame_lwpCV = camera.read() # 逐帧采集视频流
    if not grabbed:
        break
    gray_lwpCV = cv2.cvtColor(frame_lwpCV, cv2.COLOR_BGR2GRAY) # 转灰度图
    frame_data = np.array(gray_lwpCV)  # 每一帧循环存入数组
    box_data = frame_data[:, 400:400+rectangleCols] # 取矩形目标区域
    pixel_sum = np.sum(box_data, axis=1) # 行求和q
    length = len(gray_lwpCV)
    x = range(length)
    emptyImage = np.zeros((rectangleCols*10, length*2, 3), np.uint8)
    for i in x:
        cv2.rectangle(emptyImage, (i*2, (rectangleCols-pixel_sum[i]/255)*10), ((i+1)*2, rectangleCols*10), (255, 0, 0), 1)
    emptyImage = cv2.resize(emptyImage, (320, 240))

<<<<<<< HEAD
=======
import cv2
import numpy as np

>>>>>>> parent of 90c774f... 增加一个gui窗口
=======
import cv2
import numpy as np

>>>>>>> parent of 90c774f... 增加一个gui窗口
=======
import cv2
import numpy as np

>>>>>>> parent of 90c774f... 增加一个gui窗口
=======
import cv2
import numpy as np

>>>>>>> parent of 90c774f... 增加一个gui窗口
=======
import cv2
import numpy as np

>>>>>>> parent of 90c774f... 增加一个gui窗口
=======
import cv2
import numpy as np

>>>>>>> parent of 90c774f... 增加一个gui窗口
=======
import cv2
import numpy as np

>>>>>>> parent of 90c774f... 增加一个gui窗口
img=cv2.imread('00224.jpg',0)
img2=img[100:200,0:100]
print(type(img))
#cv2.imshow(img,'img')
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
#cv2.imshow(img2)
>>>>>>> parent of 90c774f... 增加一个gui窗口
=======
#cv2.imshow(img2)
>>>>>>> parent of 90c774f... 增加一个gui窗口
=======
#cv2.imshow(img2)
>>>>>>> parent of 90c774f... 增加一个gui窗口
=======
#cv2.imshow(img2)
>>>>>>> parent of 90c774f... 增加一个gui窗口
=======
#cv2.imshow(img2)
>>>>>>> parent of 90c774f... 增加一个gui窗口
=======
#cv2.imshow(img2)
>>>>>>> parent of 90c774f... 增加一个gui窗口
=======
#cv2.imshow(img2)
>>>>>>> parent of 90c774f... 增加一个gui窗口
=======
#cv2.imshow(img2)
>>>>>>> parent of 90c774f... 增加一个gui窗口
=======
    # 画目标区域
    lwpCV_box = cv2.rectangle(frame_lwpCV, (400, 0), (430, length), (0, 255, 0), 2)
    cv2.imshow('lwpCVWindow', frame_lwpCV) # 显示采集到的视频流
    cv2.imshow('sum', emptyImage)  # 显示画出的条形图
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
camera.release()
cv2.destroyAllWindows()
>>>>>>> parent of 78de438... Merge branch 'opencv' of https://github.com/CoderNice/DL-Gesture-Recognition into opencv
