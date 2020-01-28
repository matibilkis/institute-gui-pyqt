import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

s=0
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Ay ay ay!'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.initUI()


    def initUI(self):

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)





        self.button = QPushButton('Recibirse!!', self)
        self.button.setToolTip('This is an example button')
        self.button.move(100,70)
        self.button.clicked.connect(self.on_click)
        self.grid=QGridLayout()
        self.setLayout(self.grid)
        self.grid.addWidget(self.button,0,0)
        self.show()

    def on_click(self):
        global s
        s=s+1
        self.button1=QPushButton("OTRO MAS!",self)
        self.button1.clicked.connect(self.baba)
        self.grid.addWidget(self.button1,s,0)
        self.grid.setRowStretch(1)
        print(s)

    def baba(self):
        sender = self.sender()
        print(sender.text())

if __name__ == '__main__':
    s=0
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
