# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'asociando.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import comandos
from functools import partial

class II(object):
    def __init__(self):
        super(II,self).__init__()
        self.datos = comandos.Tablota("DATOS.db")
        MainWindow=QtWidgets.QMainWindow()
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
#         self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
#         self.widget.setGeometry(QtCore.QRect(10, 10, 622, 41))
#         self.widget.setObjectName("widget")
#         self.gridLayout = QtWidgets.QGridLayout(self.widget)
#         self.gridLayout.setContentsMargins(0, 0, 0, 0)
#         self.gridLayout.setObjectName("gridLayout")
#         self.quit1 = QtWidgets.QPushButton(self.widget)
#         self.quit1.setStyleSheet("border-color: rgb(0, 0, 0);\n"
# "border-color: rgb(255, 255, 255);\n"
# "font: 75 18pt \"Courier 10 Pitch\";\n"
# "border: 2px solid black;\n"
# "background-color: rgb(255, 0, 0);\n"
# "color: rgb(255, 255, 255);")
#         self.quit1.setObjectName("quit1")
#         self.gridLayout.addWidget(self.quit1, 0, 1, 1, 1)
#         self.tipito1 = QtWidgets.QLabel(self.widget)
#         self.tipito1.setStyleSheet("border-color: rgb(0, 0, 0);\n"
# "border-color: rgb(255, 255, 255);\n"
# "font: 75 18pt \"Courier 10 Pitch\";\n"
# "border: 2px solid black;\n"
# "background-color: rgb(255, 255, 127);\n"
# "")
#         self.tipito1.setObjectName("tipito1")
#         self.gridLayout.addWidget(self.tipito1, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 670, 19))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.layoutWidget1=QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget2=QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget3=QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget4=QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget5=QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget6=QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget7=QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget8=QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget9=QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget10=QtWidgets.QWidget(self.scrollAreaWidgetContents)

        self.layouts=[self.layoutWidget1,self.layoutWidget2,self.layoutWidget3,self.layoutWidget4,self.layoutWidget5,self.layoutWidget6,self.layoutWidget7,self.layoutWidget8,self.layoutWidget9,self.layoutWidget10]


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.agreg.setText(_translate("MainWindow", "Agregar al grupo"))
        self.pushButton_2.setText(_translate("MainWindow", "Quitar del grupo"))
        # self.quit1.setText(_translate("MainWindow", "Quitar del grupo"))
        # self.tipito1.setText(_translate("MainWindow", "Tipito uno"))

        self.ii=MainWindow
        self.ii.move(100,100)
        self.activarse()



    def anotamelo(vars):
        for i in vars:
            self.ss=self.ss+50
#             self.tip = QtWidgets.QLabel(self.centralwidget)
#             self.tip.setGeometry(QtCore.QRect(10, 130, 400, 49))
#             self.tip.setStyleSheet("border-color: rgb(0, 0, 0);\n"
# "border-color: rgb(255, 255, 255);\n"
# "font: 75 18pt \"Courier 10 Pitch\";\n"
# "border: 2px solid black;\n"
# "background-color: rgb(255, 255, 127);\n"
# "")
#             self.push = QtWidgets.QPushButton(self.centralwidget)
#             self.push.setGeometry(QtCore.QRect(440, 180, 240, 50))
#             self.push.setStyleSheet("border-color: rgb(0, 0, 0);\n"
# "border-color: rgb(255, 255, 255);\n"
# "font: 75 18pt \"Courier 10 Pitch\";\n"
# "border: 2px solid black;\n"
# "background-color: rgb(255, 0, 0);\n"
# "color: rgb(255, 255, 255);")
#             self.push.setObjectName("push"+str(self.ss))
#             self.tip.setObjectName("tip"+str(self.ss))
#             self.tip.setText(i[0])





    def agregoun(self):
        encontrado=self.buscanombre.text().replace(" ", "")
        for data in self.datos.charly():
            todojunto=str(data[1]).replace(' ','')+str(data[2]).replace(' ','')+str(data[3]).replace(' ','')
            if encontrado==todojunto:
                indice=data[0]
                self.layouts[self.count].setGeometry(QtCore.QRect(10, 10+self.ss, 622, 40))
                self.layouts[self.count].setObjectName("layoutWidget")
                self.gridLayout_2 = QtWidgets.QGridLayout(self.layouts[self.count])
                self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
                self.gridLayout_2.setObjectName("gridLayout_2")
                self.quit2 = QtWidgets.QPushButton(self.layouts[self.count])
                self.quit2.setStyleSheet("border-color: rgb(0, 0, 0);\n"
                "border-color: rgb(255, 255, 255);\n"
                "font: 75 18pt \"Courier 10 Pitch\";\n"
                "border: 2px solid black;\n"
                "background-color: rgb(255, 0, 0);\n"
                "color: rgb(255, 255, 255);")
                self.quit2.setObjectName("quit2")
                self.gridLayout_2.addWidget(self.quit2, 0, 1, 1, 1)
                self.tip2 = QtWidgets.QLabel(self.layouts[self.count])
                self.tip2.setStyleSheet("border-color: rgb(0, 0, 0);\n"
                "border-color: rgb(255, 255, 255);\n"
                "font: 75 18pt \"Courier 10 Pitch\";\n"
                "border: 2px solid black;\n"
                "background-color: rgb(255, 255, 127);\n"
                "")
                self.tip2.setObjectName("tip2")
                self.gridLayout_2.addWidget(self.tip2, 0, 0, 1, 1)
                self.layouts[self.count].raise_()
                # self.layoutWidget.raise_()
                self.tip2.setText(str(data[0])+" "+str(data[1])+" "+str(data[2]))
                self.quit2.setText("Quitar del grupo")
                print(data[0])
                self.quit2.clicked.connect(partial(self.quitar,[data[0]]))
                self.count=self.count+1
                self.datos.tepongonumerodeel(self.datainicial,data[0])
                self.ss=self.ss+40


    def anotamelosnombres(self,ids,nombres):
        for i,j in zip(nombres,ids):
            self.layouts[self.count].setGeometry(QtCore.QRect(10, 10+self.ss, 622, 40))
            self.layouts[self.count].setObjectName("layoutWidget")
            self.gridLayout_2 = QtWidgets.QGridLayout(self.layouts[self.count])
            self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
            self.gridLayout_2.setObjectName("gridLayout_2")
            self.quit2 = QtWidgets.QPushButton(self.layouts[self.count])
            self.quit2.setStyleSheet("border-color: rgb(0, 0, 0);\n"
            "border-color: rgb(255, 255, 255);\n"
            "font: 75 18pt \"Courier 10 Pitch\";\n"
            "border: 2px solid black;\n"
            "background-color: rgb(255, 0, 0);\n"
            "color: rgb(255, 255, 255);")
            self.quit2.setObjectName("quit2")
            self.gridLayout_2.addWidget(self.quit2, 0, 1, 1, 1)
            self.tip2 = QtWidgets.QLabel(self.layouts[self.count])
            self.tip2.setStyleSheet("border-color: rgb(0, 0, 0);\n"
            "border-color: rgb(255, 255, 255);\n"
            "font: 75 18pt \"Courier 10 Pitch\";\n"
            "border: 2px solid black;\n"
            "background-color: rgb(255, 255, 127);\n"
            "")
            self.tip2.setObjectName("tip2")
            self.gridLayout_2.addWidget(self.tip2, 0, 0, 1, 1)
            self.layouts[self.count].raise_()
            # self.layoutWidget.raise_()
            self.tip2.setText(i)
            self.quit2.setText("Quitar del grupo")
            # print(nombres[0])
            self.quit2.clicked.connect(partial(self.quitar,j))
            self.count=self.count+1
            self.ss=self.ss+40



    def quitar(self,id):
        print(id)
        self.datos.nprandom(id)
        self.tip2.deleteLater()
        self.quit2.deleteLater()


    def get_data(self,model):
        datatod = []
        for data in self.datos.charly():
            datatod.append(str(data[1])+ ' ' +str(data[2])+' '+str(data[3]))
        model.setStringList(datatod)


    def activarse(self):
        self.ss=0
        self.count=0
        self.pushs=[]
        self.tips=[]
        completer = QtWidgets.QCompleter()
        self.buscanombre.setCompleter(completer)
        self.model = QtCore.QStringListModel()
        self.agreg.clicked.connect(self.agregoun)
        completer.setModel(self.model)
        self.get_data(self.model)
