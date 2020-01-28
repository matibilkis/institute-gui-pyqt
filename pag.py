# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pagandobckp.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import comandos
import agregoalumnos
import comanditos

class HH(object):
    def __init__(self):
        super(HH,self).__init__()
        self.datos = comandos.Tablota("DATOS.db")
        MainWindow=QtWidgets.QMainWindow()
        MainWindow.resize(1509, 715)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verfichabuton = QtWidgets.QPushButton(self.centralwidget)
        self.verfichabuton.setGeometry(QtCore.QRect(779, 20, 151, 40))
        self.verfichabuton.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"border: 2px solid black;")
        self.verfichabuton.setObjectName("verfichabuton")
        self.buscanombre = QtWidgets.QLineEdit(self.centralwidget)
        self.buscanombre.setGeometry(QtCore.QRect(10, 20, 760, 90))
        self.buscanombre.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"border: 2px solid black;")
        self.buscanombre.setText("")
        self.buscanombre.setObjectName("buscanombre")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 130, 921, 301))
        self.scrollArea.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"border: 1px solid black;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 919, 299))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.scrollAreaWidgetContents)
        self.verticalScrollBar.setGeometry(QtCore.QRect(0, 0, 16, 300))
        self.verticalScrollBar.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"border: 1px solid black;")
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setGeometry(QtCore.QRect(40, 10, 250, 51))
        self.label_2.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"border: 2px solid black;\n"
"background-color: rgb(255, 255, 127);\n"
"")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setGeometry(QtCore.QRect(350, 12, 230, 49))
        self.label_3.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"border: 2px solid black;\n"
"background-color: rgb(255, 255, 127);\n"
"")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setGeometry(QtCore.QRect(620, 10, 230, 51))
        self.label_4.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"border: 2px solid black;\n"
"background-color: rgb(255, 255, 127);\n"
"")
        self.label_4.setObjectName("label_4")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pagarcuota_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pagarcuota_2.setGeometry(QtCore.QRect(980, 470, 240, 100))
        self.pagarcuota_2.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"border: 2px solid black;\n"
"border-right: 0px\n"
"")
        self.pagarcuota_2.setObjectName("pagarcuota_2")
        self.monto = QtWidgets.QLCDNumber(self.centralwidget)
        self.monto.setGeometry(QtCore.QRect(1190, 470, 300, 100))
        self.monto.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"border: 2px solid black;\n"
"border-left:0px")
        self.monto.setObjectName("monto")
        self.fotito = QtWidgets.QLabel(self.centralwidget)
        self.fotito.setGeometry(QtCore.QRect(980, 21, 510, 410))
        self.fotito.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"border: 2px solid black;")
        self.fotito.setText("")
        self.fotito.setObjectName("fotito")
        self.confirmar = QtWidgets.QPushButton(self.centralwidget)
        self.confirmar.setGeometry(QtCore.QRect(980, 580, 510, 90))
        self.confirmar.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"border: 2px solid black;")
        self.confirmar.setObjectName("confirmar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 470, 918, 201))
        self.label.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"border: 2px solid black;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 450, 230, 20))
        self.label_5.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"border: 2px solid black;\n"
"background-color: rgb(255, 255, 127);\n"
"border-bottom: 0px\n"
"")
        self.label_5.setObjectName("label_5")
        self.comentariosos = QtWidgets.QLineEdit(self.centralwidget)
        self.comentariosos.setGeometry(QtCore.QRect(12, 472, 914, 197))
        self.comentariosos.setStyleSheet("font: 75 18pt \"Courier 10 Pitch\";\n"
"")
        self.comentariosos.setObjectName("comentariosos")
        self.vercuota = QtWidgets.QPushButton(self.centralwidget)
        self.vercuota.setGeometry(QtCore.QRect(780, 70, 151, 40))
        self.vercuota.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"border: 2px solid black;")
        self.vercuota.setObjectName("vercuota")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1509, 19))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.hh = MainWindow
        self.activar()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.verfichabuton.setText(_translate("MainWindow", "Ver ficha"))
        self.label_2.setText(_translate("MainWindow", "¿Quienes pagan?"))
        self.label_3.setText(_translate("MainWindow", "Curso"))
        self.label_4.setText(_translate("MainWindow", "Monto"))
        self.pagarcuota_2.setText(_translate("MainWindow", "Total a pagar: "))
        self.confirmar.setText(_translate("MainWindow", "Confirmar Pago"))
        self.label_5.setText(_translate("MainWindow", "Comentarios"))
        self.vercuota.setText(_translate("MainWindow", "Ver cuota"))



    def activar(self):
        self.vercuota.clicked.connect(self.buscador)
        completer = QtWidgets.QCompleter()
        self.buscanombre.setCompleter(completer)
        self.model = QtCore.QStringListModel()
        completer.setModel(self.model)
        self.get_data(self.model)
        self.veoquienes()

    def get_data(self,model):
        datatod = []
        for data in self.datos.charly():
            datatod.append(str(data[1])+ ' ' +str(data[2])+' '+str(data[3]))
        model.setStringList(datatod)

    def buscador(self):
        encontrado=self.buscanombre.text().replace(" ", "")
        for data in self.datos.charly():
            todojunto=str(data[1]).replace(' ','')+str(data[2]).replace(' ','')+str(data[3]).replace(' ','')
            if encontrado==todojunto:
                ind=data[0]
                print(self.datos.juntoacademicos(ind)[0][1])


    def veoquienes(self):
        agregoalumnos.Agrego(self.scrollAreaWidgetContents)
