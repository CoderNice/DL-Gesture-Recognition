import sys
from PyQt5.QtWidgets import QWidget, QApplication, QGroupBox, QPushButton, QLabel,  QVBoxLayout,  QHBoxLayout, QTextEdit

class GUI(QWidget):
    def __init__(self):
        super(GUI,self).__init__()
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
        nameLabel = QLabel("放图片o oooooooooooooo")
        #QLabel.setPicture(nameLabel,'thumb.jpg')
        layout.addWidget(nameLabel)
        self.hboxGroupBox.setLayout(layout)
        self.setWindowTitle('Basic Layout')

    def creatVboxGroupBox(self):
        self.vboxGroupBox = QGroupBox("Vbox layout")
        layout = QVBoxLayout()
        start = QPushButton('开始', self)
        start.setCheckable(True)
        end = QPushButton('结束', self)
        end.setCheckable(True)
        nameLabel = QLabel("输出：")
        bigEditor = QTextEdit()
        bigEditor.setPlainText("...")
        layout.addWidget(nameLabel)
        layout.addWidget(bigEditor)
        layout.addWidget(start)
        layout.addWidget(end)
        self.vboxGroupBox.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GUI()
    ex.show()
    sys.exit(app.exec_())