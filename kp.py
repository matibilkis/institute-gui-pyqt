# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'asociandosc.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(670, 526)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.buscanombre = QtWidgets.QLineEdit(self.centralwidget)
        self.buscanombre.setGeometry(QtCore.QRect(20, 20, 310, 50))
        self.buscanombre.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"border: 2px solid black;")
        self.buscanombre.setText("")
        self.buscanombre.setObjectName("buscanombre")
        self.agreg = QtWidgets.QPushButton(self.centralwidget)
        self.agreg.setGeometry(QtCore.QRect(360, 20, 280, 50))
        self.agreg.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"border: 2px solid black;\n"
"")
        self.agreg.setObjectName("agreg")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, -50, 659, 33))
        self.pushButton_2.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"border: 2px solid black;\n"
"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 80, 650, 321))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 648, 319))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget.setGeometry(QtCore.QRect(10, 10, 622, 41))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.quit1 = QtWidgets.QPushButton(self.widget)
        self.quit1.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"border: 2px solid black;\n"
"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.quit1.setObjectName("quit1")
        self.gridLayout.addWidget(self.quit1, 0, 1, 1, 1)
        self.tipito1 = QtWidgets.QLabel(self.widget)
        self.tipito1.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"border: 2px solid black;\n"
"background-color: rgb(255, 255, 127);\n"
"")
        self.tipito1.setObjectName("tipito1")
        self.gridLayout.addWidget(self.tipito1, 0, 0, 1, 1)
        self.layoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 51, 622, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.quit2 = QtWidgets.QPushButton(self.layoutWidget)
        self.quit2.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"border: 2px solid black;\n"
"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.quit2.setObjectName("quit2")
        self.gridLayout_2.addWidget(self.quit2, 0, 1, 1, 1)
        self.tip2 = QtWidgets.QLabel(self.layoutWidget)
        self.tip2.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"border: 2px solid black;\n"
"background-color: rgb(255, 255, 127);\n"
"")
        self.tip2.setObjectName("tip2")
        self.gridLayout_2.addWidget(self.tip2, 0, 0, 1, 1)
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 670, 19))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.agreg.setText(_translate("MainWindow", "Agregar al grupo"))
        self.pushButton_2.setText(_translate("MainWindow", "Quitar del grupo"))
        self.quit1.setText(_translate("MainWindow", "Quitar del grupo"))
        self.tipito1.setText(_translate("MainWindow", "Tipito uno"))
        self.quit2.setText(_translate("MainWindow", "Quitar del grupo"))
        self.tip2.setText(_translate("MainWindow", "Tipito dos"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

