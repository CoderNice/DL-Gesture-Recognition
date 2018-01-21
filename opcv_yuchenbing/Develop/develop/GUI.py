import sys
<<<<<<< HEAD
from PyQt5.QtGui import QPixmap
=======
import time
import cv2
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtGui import QIcon, QPixmap
>>>>>>> 2b1941d50a6121878bb1e6911df05db15167db76
from PyQt5.QtWidgets import QWidget, QApplication, QGroupBox, QPushButton, QLabel,  QVBoxLayout,  QHBoxLayout, QTextEdit


'''
类说明:
1.
2.
3.
'''


class Communicate(QObject):
    closeApp = pyqtSignal() 

class cameraControl:
    def __init__(self):
        self.flagCyc=True
        
    def startCamera(self):
        #print('可以调用摄像头函数了')
        time.sleep(1)
        self.flagCyc=True
        camera = cv2.VideoCapture(0)
        if camera is None:
            print('请先连接摄像头')
            exit()
 
        fps = 5 # 帧率
        pre_frame = None  # 总是取前一帧做为背景（不用考虑环境影响）
 
        play_music = False
        count=0 
        print('我在地方1死掉了')
        
        while self.flagCyc:
            print('我在地方2死掉了')
            start = time.time()
            res, cur_frame = camera.read()
            if not res:
                print('我要跳出循环啦')
            if res != True:break
            end = time.time()
            seconds = end - start
            if seconds < 1.0/fps:
                time.sleep(1.0/fps - seconds)
            #print('读取了一帧')
            gray_img = cv2.cvtColor(cur_frame, cv2.COLOR_BGR2GRAY)
            gray_img = cv2.resize(gray_img, (500, 500))
            gray_img = cv2.GaussianBlur(gray_img, (21, 21), 0)
            
            print('我在地方3死掉了')
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
                print('我在地方4死掉了')
                
            camera.release()
            cv2.destroyAllWindows()
        
    def endCamera(self):
            self.flagCyc=False


class GUI(QWidget):
    def __init__(self):
        super(GUI,self).__init__()
        self.cameraCon=cameraControl()
        self.initUi()
        

    def initUi(self):
        self.creatVboxGroupBox()
        self.creatHboxGroupBox()
        mainLayout = QHBoxLayout()
        mainLayout.addWidget(self.hboxGroupBox)
        mainLayout.addWidget(self.vboxGroupBox)
        self.setLayout(mainLayout)

    def creatHboxGroupBox(self):
        self.hboxGroupBox = QGroupBox("Hbox layout")
        layout = QHBoxLayout()
<<<<<<< HEAD
        nameLabel = QLabel("视频")
        pixmap = QPixmap('thumb.jpg')
        nameLabel.setPixmap(pixmap)
        nameLabel.show()
        layout.addWidget(nameLabel)
=======
        vedioLabel = QLabel("放图片o oooooooooooooo")
        pixmap = QPixmap('thumb.jpg')
        vedioLabel.setPixmap(pixmap)
        vedioLabel.show()
        #nameLabel.setPicture(self,)
        #QLabel.setPicture(nameLabel,'thumb.jpg')
        layout.addWidget(vedioLabel)
>>>>>>> 2b1941d50a6121878bb1e6911df05db15167db76
        self.hboxGroupBox.setLayout(layout)
        self.setWindowTitle('Basic Layout')

    def creatVboxGroupBox(self):
        #信号和槽
        self.cStart = Communicate()
        self.cStart.closeApp.connect(lambda: self.cameraCon.startCamera())
        self.cEnd = Communicate()
        self.cEnd.closeApp.connect(lambda: self.cameraCon.endCamera())
        
        self.vboxGroupBox = QGroupBox("Vbox layout")
        layout = QVBoxLayout()
        start = QPushButton('开始', self)
        start.setCheckable(True)
        end = QPushButton('结束', self)
        end.setCheckable(True)
        start.clicked.connect(lambda: self.cStart.closeApp.emit())
        end.clicked.connect(lambda: self.cEnd.closeApp.emit())
        
        outputLabel = QLabel("输出：")
        text = QTextEdit()
        text.setPlainText("...")
        #layout.addWidget(vedioLabel)
        layout.addWidget(text)
        layout.addWidget(start)
        layout.addWidget(end)
        self.vboxGroupBox.setLayout(layout)
        

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GUI()
    ex.show()
    sys.exit(app.exec_())