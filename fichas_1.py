import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
import comandos
import os
import cam2
from numpy import random
import pandas as pd
import os
import ass

class FF(object):
    def __init__(self):
        super(FF,self).__init__()
        self.datos = comandos.Tablota("DATOS.db")
        MainWindow=QtWidgets.QMainWindow()

#####################################
######################################
#####################################
######################################
#####################################
######################################
#####################################
######################################
#####################################
#####################################
######################################
#####################################
#####################################
#####################################
######################################
#####################################
######################################
#####################################
######################################
#####################################
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1539, 849)


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(6, 90, 811, 551))
        self.tabWidget.setStyleSheet("border-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 255), stop:0.19397 rgba(0, 0, 0, 255), stop:0.202312 rgba(122, 97, 0, 255), stop:0.495514 rgba(76, 58, 0, 255), stop:0.504819 rgba(255, 255, 255, 255), stop:0.79 rgba(255, 255, 255, 255), stop:1 rgba(255, 158, 158, 255));\n"
"\n"
"border: 2px solid black\n"
"")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(30, 20, 201, 40))
        self.label_2.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"background-color: rgb(255, 255, 127);\n"
"border: 2px solid black;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(30, 80, 201, 40))
        self.label_3.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Courier 10 Pitch\";\n"
"background-color: rgb(255, 255, 127);\n"
"border: 2px solid black;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(30, 200, 201, 40))
        self.label_4.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Courier 10 Pitch\";\n"
"background-color: rgb(255, 255, 127);\n"
"border: 2px solid black;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(30, 140, 201, 40))
        self.label_5.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Courier 10 Pitch\";\n"
"background-color: rgb(255, 255, 127);\n"
"border: 2px solid black;")
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(30, 260, 201, 40))
        self.label_7.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Courier 10 Pitch\";\n"
"background-color: rgb(255, 255, 127);\n"
"border: 2px solid black;")
        self.label_7.setObjectName("label_7")
        self.frame_2 = QtWidgets.QFrame(self.tab)
        self.frame_2.setGeometry(QtCore.QRect(30, 320, 771, 141))
        self.frame_2.setStyleSheet("border 0px solid black")
        self.frame_2.setObjectName("frame_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(590, 70, 141, 20))
        self.lineEdit_3.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 8pt \"Sans Serif\";\n"
"background-color: rgb(255, 255, 127);\n"
"border: 2px solid black;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(250, 70, 141, 20))
        self.lineEdit.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 8pt \"Sans Serif\";\n"
"background-color: rgb(255, 255, 127);\n"
"border: 2px solid black;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(420, 70, 141, 20))
        self.lineEdit_2.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 8pt \"Sans Serif\";\n"
"background-color: rgb(255, 255, 127);\n"
"border: 2px solid black;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(10, 30, 161, 30))
        self.label_6.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Courier 10 Pitch\";\n"
"background-color: rgb(255, 255, 127);\n"
"border: 2px solid black;")
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(10, 100, 161, 30))
        self.label_8.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 15pt \"Courier 10 Pitch\";\n"
"background-color: rgb(255, 255, 127);\n"
"border: 2px solid black;")
        self.label_8.setObjectName("label_8")
        self.tel1_entry = QtWidgets.QLineEdit(self.frame_2)
        self.tel1_entry.setGeometry(QtCore.QRect(250, 30, 140, 30))
        self.tel1_entry.setText("")
        self.tel1_entry.setObjectName("tel1_entry")
        self.tel2_entry = QtWidgets.QLineEdit(self.frame_2)
        self.tel2_entry.setGeometry(QtCore.QRect(420, 30, 140, 30))
        self.tel2_entry.setObjectName("tel2_entry")
        self.tel3_entry = QtWidgets.QLineEdit(self.frame_2)
        self.tel3_entry.setGeometry(QtCore.QRect(590, 30, 140, 30))
        self.tel3_entry.setObjectName("tel3_entry")
        self.mail_entry = QtWidgets.QLineEdit(self.frame_2)
        self.mail_entry.setGeometry(QtCore.QRect(250, 100, 480, 30))
        self.mail_entry.setText("")
        self.mail_entry.setObjectName("mail_entry")
        self.label_16 = QtWidgets.QLabel(self.tab)
        self.label_16.setGeometry(QtCore.QRect(480, 200, 80, 40))
        self.label_16.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Courier 10 Pitch\";\n"
"background-color: rgb(255, 255, 127);\n"
"border: 2px solid black;")
        self.label_16.setObjectName("label_16")
        self.edad = QtWidgets.QLabel(self.tab)
        self.edad.setGeometry(QtCore.QRect(590, 200, 51, 40))
        self.edad.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 16pt \"Sans Serif\";\n"
"border: 2px solid black;")
        self.edad.setText("")
        self.edad.setObjectName("edad")
        self.nombre_entry = QtWidgets.QLineEdit(self.tab)
        self.nombre_entry.setGeometry(QtCore.QRect(280, 20, 480, 41))
        self.nombre_entry.setStyleSheet("font: 14pt \"cmr10\";\n"
"")
        self.nombre_entry.setText("")
        self.nombre_entry.setObjectName("nombre_entry")
        self.apellidop_entry = QtWidgets.QLineEdit(self.tab)
        self.apellidop_entry.setGeometry(QtCore.QRect(280, 80, 480, 41))
        self.apellidop_entry.setStyleSheet("font: 14pt \"cmr10\";\n"
"")
        self.apellidop_entry.setObjectName("apellidop_entry")
        self.nac_entry = QtWidgets.QLineEdit(self.tab)
        self.nac_entry.setGeometry(QtCore.QRect(280, 200, 151, 41))
        self.nac_entry.setStyleSheet("font: 14pt \"cmr10\";\n"
"")
        self.nac_entry.setObjectName("nac_entry")
        self.dom_entry = QtWidgets.QLineEdit(self.tab)
        self.dom_entry.setGeometry(QtCore.QRect(280, 260, 480, 41))
        self.dom_entry.setStyleSheet("font: 14pt \"cmr10\";\n"
"")
        self.dom_entry.setObjectName("dom_entry")
        self.apellidom_entry = QtWidgets.QLineEdit(self.tab)
        self.apellidom_entry.setGeometry(QtCore.QRect(280, 140, 480, 41))
        self.apellidom_entry.setStyleSheet("font: 14pt \"cmr10\";\n"
"")
        self.apellidom_entry.setObjectName("apellidom_entry")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(32, 307, 200, 15))
        self.label_9.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Courier 10 Pitch\";\n"
"background-color: rgb(255, 255, 127);\n"
"border: 2px solid black;")
        self.label_9.setObjectName("label_9")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_18 = QtWidgets.QLabel(self.tab_2)
        self.label_18.setGeometry(QtCore.QRect(20, 200, 161, 40))
        self.label_18.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"background-color: rgb(255, 255, 127);\n"
"border: 2px solid black;")
        self.label_18.setObjectName("label_18")
        self.label_20 = QtWidgets.QLabel(self.tab_2)
        self.label_20.setGeometry(QtCore.QRect(20, 80, 161, 40))
        self.label_20.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"background-color: rgb(255, 255, 127);\n"
"border: 2px solid black;")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.tab_2)
        self.label_21.setGeometry(QtCore.QRect(20, 140, 161, 40))
        self.label_21.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"background-color: rgb(255, 255, 127);\n"
"border: 2px solid black;")
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.tab_2)
        self.label_22.setGeometry(QtCore.QRect(20, 20, 161, 40))
        self.label_22.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"background-color: rgb(255, 255, 127);\n"
"border: 2px solid black;")
        self.label_22.setObjectName("label_22")
        self.label_25 = QtWidgets.QLabel(self.tab_2)
        self.label_25.setGeometry(QtCore.QRect(440, 80, 161, 40))
        self.label_25.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"background-color: rgb(255, 255, 127);\n"
"border: 2px solid black;")
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.tab_2)
        self.label_26.setGeometry(QtCore.QRect(440, 140, 161, 40))
        self.label_26.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Courier 10 Pitch\";\n"
"background-color: rgb(255, 255, 127);\n"
"border: 2px solid black;")
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.tab_2)
        self.label_27.setGeometry(QtCore.QRect(440, 20, 161, 40))
        self.label_27.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"background-color: rgb(255, 255, 127);\n"
"border: 2px solid black;")
        self.label_27.setObjectName("label_27")
        self.curso_entry = QtWidgets.QLineEdit(self.tab_2)
        self.curso_entry.setGeometry(QtCore.QRect(220, 20, 151, 41))
        self.curso_entry.setStyleSheet("font: 14pt \"cmr10\";\n"
"")
        self.curso_entry.setText("")
        self.curso_entry.setObjectName("curso_entry")
        self.teacher_entry = QtWidgets.QLineEdit(self.tab_2)
        self.teacher_entry.setGeometry(QtCore.QRect(220, 80, 151, 41))
        self.teacher_entry.setStyleSheet("font: 14pt \"cmr10\";\n"
"")
        self.teacher_entry.setObjectName("teacher_entry")
        self.horario_entry = QtWidgets.QLineEdit(self.tab_2)
        self.horario_entry.setGeometry(QtCore.QRect(220, 200, 151, 41))
        self.horario_entry.setStyleSheet("font: 14pt \"cmr10\";\n"
"")
        self.horario_entry.setObjectName("horario_entry")
        self.lib_entry = QtWidgets.QLineEdit(self.tab_2)
        self.lib_entry.setGeometry(QtCore.QRect(220, 140, 151, 41))
        self.lib_entry.setStyleSheet("font: 14pt \"cmr10\";\n"
"")
        self.lib_entry.setObjectName("lib_entry")
        self.cole_entry = QtWidgets.QLineEdit(self.tab_2)
        self.cole_entry.setGeometry(QtCore.QRect(620, 20, 151, 41))
        self.cole_entry.setStyleSheet("font: 14pt \"cmr10\";\n"
"")
        self.cole_entry.setObjectName("cole_entry")
        self.grado_entry = QtWidgets.QLineEdit(self.tab_2)
        self.grado_entry.setGeometry(QtCore.QRect(620, 80, 151, 41))
        self.grado_entry.setStyleSheet("font: 14pt \"cmr10\";\n"
"")
        self.grado_entry.setObjectName("grado_entry")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_13.setGeometry(QtCore.QRect(610, 540, 151, 41))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.libcole_entry = QtWidgets.QLineEdit(self.tab_2)
        self.libcole_entry.setGeometry(QtCore.QRect(620, 140, 151, 41))
        self.libcole_entry.setStyleSheet("font: 14pt \"cmr10\";\n"
"")
        self.libcole_entry.setObjectName("libcole_entry")
        self.frame_21 = QtWidgets.QFrame(self.tab_2)
        self.frame_21.setGeometry(QtCore.QRect(20, 269, 400, 170))
        self.frame_21.setStyleSheet("border: 2px solid black;")
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.exwritten_entry = QtWidgets.QTextEdit(self.frame_21)
        self.exwritten_entry.setGeometry(QtCore.QRect(230, 130, 140, 31))
        self.exwritten_entry.setStyleSheet("font: 14pt \"cmr10\";\n"
"")
        self.exwritten_entry.setObjectName("exwritten_entry")
        self.label_23 = QtWidgets.QLabel(self.frame_21)
        self.label_23.setGeometry(QtCore.QRect(8, 70, 161, 30))
        self.label_23.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"background-color: rgb(255, 255, 127);\n"
"border: 2px solid black;")
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.frame_21)
        self.label_24.setGeometry(QtCore.QRect(8, 130, 161, 30))
        self.label_24.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"background-color: rgb(255, 255, 127);\n"
"border: 2px solid black;")
        self.label_24.setObjectName("label_24")
        self.exoral_entry = QtWidgets.QTextEdit(self.frame_21)
        self.exoral_entry.setGeometry(QtCore.QRect(230, 70, 140, 31))
        self.exoral_entry.setStyleSheet("font: 14pt \"cmr10\";\n"
"")
        self.exoral_entry.setObjectName("exoral_entry")
        self.label_29 = QtWidgets.QLabel(self.frame_21)
        self.label_29.setGeometry(QtCore.QRect(230, 10, 140, 30))
        self.label_29.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"background-color: rgb(255, 255, 127);\n"
"border: 2px solid black;")
        self.label_29.setObjectName("label_29")
        self.label_28 = QtWidgets.QLabel(self.tab_2)
        self.label_28.setGeometry(QtCore.QRect(30, 280, 160, 30))
        self.label_28.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Courier 10 Pitch\";\n"
"background-color: rgb(255, 255, 127);\n"
"border: 2px solid black;")
        self.label_28.setObjectName("label_28")
        self.frame_4 = QtWidgets.QFrame(self.tab_2)
        self.frame_4.setGeometry(QtCore.QRect(440, 270, 321, 170))
        self.frame_4.setStyleSheet("border: 2px solid black;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.inter_entry = QtWidgets.QTextEdit(self.frame_4)
        self.inter_entry.setGeometry(QtCore.QRect(0, 20, 321, 150))
        self.inter_entry.setStyleSheet("font: 14pt \"cmr10\";\n"
"")
        self.inter_entry.setObjectName("inter_entry")
        self.label_44 = QtWidgets.QLabel(self.frame_4)
        self.label_44.setGeometry(QtCore.QRect(0, 0, 320, 20))
        self.label_44.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Courier 10 Pitch\";\n"
"background-color: rgb(255, 255, 127);\n"
"border: 2px solid black;")
        self.label_44.setObjectName("label_44")
        self.reglamento_entry = QtWidgets.QCheckBox(self.tab_2)
        self.reglamento_entry.setGeometry(QtCore.QRect(440, 200, 331, 41))
        self.reglamento_entry.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"background-color: rgb(255, 255, 127);\n"
"border: 2px solid black;")
        self.reglamento_entry.setObjectName("reglamento_entry")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.frame_3 = QtWidgets.QFrame(self.tab_3)
        self.frame_3.setGeometry(QtCore.QRect(10, 20, 791, 501))
        self.frame_3.setStyleSheet("border: 2px solid black;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.abril_entry = QtWidgets.QTextEdit(self.frame_3)
        self.abril_entry.setGeometry(QtCore.QRect(230, 100, 140, 30))
        self.abril_entry.setStyleSheet("border-top: 0px")
        self.abril_entry.setObjectName("abril_entry")
        self.label_30 = QtWidgets.QLabel(self.frame_3)
        self.label_30.setGeometry(QtCore.QRect(8, 70, 161, 30))
        self.label_30.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 16pt \"Sans Serif\";\n"
"background-color: rgb(255, 255, 127);\n"
"border: 2px solid black;\n"
"")
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.frame_3)
        self.label_31.setGeometry(QtCore.QRect(8, 100, 161, 30))
        self.label_31.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-top-color: rgb(85, 255, 127);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 16pt \"Sans Serif\";\n"
"background-color: rgb(255, 255, 127);\n"
"border: 2px solid black;\n"
"border-top: 0 px solid black\n"
"")
        self.label_31.setObjectName("label_31")
        self.marzo_entry = QtWidgets.QTextEdit(self.frame_3)
        self.marzo_entry.setGeometry(QtCore.QRect(230, 70, 140, 31))
        self.marzo_entry.setObjectName("marzo_entry")
        self.label_32 = QtWidgets.QLabel(self.frame_3)
        self.label_32.setGeometry(QtCore.QRect(10, 10, 160, 40))
        self.label_32.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"font: 75 26pt \"Courier 10 Pitch\";\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 127);\n"
"border: 2px solid black;")
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.frame_3)
        self.label_33.setGeometry(QtCore.QRect(230, 10, 150, 40))
        self.label_33.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 26pt \"Courier 10 Pitch\";\n"
"background-color: rgb(255, 255, 127);\n"
"border: 2px solid black;")
        self.label_33.setObjectName("label_33")
        self.mayo_entry = QtWidgets.QTextEdit(self.frame_3)
        self.mayo_entry.setGeometry(QtCore.QRect(230, 130, 140, 31))
        self.mayo_entry.setStyleSheet("border-top: 0px")
        self.mayo_entry.setObjectName("mayo_entry")
        self.junio_entry = QtWidgets.QTextEdit(self.frame_3)
        self.junio_entry.setGeometry(QtCore.QRect(230, 160, 140, 30))
        self.junio_entry.setStyleSheet("border-top: 0px")
        self.junio_entry.setObjectName("junio_entry")
        self.label_34 = QtWidgets.QLabel(self.frame_3)
        self.label_34.setGeometry(QtCore.QRect(9, 160, 160, 30))
        self.label_34.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-top-color: rgb(85, 255, 127);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 16pt \"Sans Serif\";\n"
"background-color: rgb(255, 255, 127);\n"
"border: 2px solid black;\n"
"border-top: 0 px solid black\n"
"")
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(self.frame_3)
        self.label_35.setGeometry(QtCore.QRect(9, 130, 160, 30))
        self.label_35.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 16pt \"Sans Serif\";\n"
"background-color: rgb(255, 255, 127);\n"
"border: 2px solid black;\n"
"border-top: 0px\n"
"")
        self.label_35.setObjectName("label_35")
        self.julio_entry = QtWidgets.QTextEdit(self.frame_3)
        self.julio_entry.setGeometry(QtCore.QRect(230, 190, 140, 31))
        self.julio_entry.setStyleSheet("border-top: 0px")
        self.julio_entry.setObjectName("julio_entry")
        self.agosto_entry = QtWidgets.QTextEdit(self.frame_3)
        self.agosto_entry.setGeometry(QtCore.QRect(230, 220, 140, 30))
        self.agosto_entry.setStyleSheet("border-top: 0px")
        self.agosto_entry.setObjectName("agosto_entry")
        self.octubre_entry = QtWidgets.QTextEdit(self.frame_3)
        self.octubre_entry.setGeometry(QtCore.QRect(230, 280, 140, 30))
        self.octubre_entry.setStyleSheet("border-top: 0px")
        self.octubre_entry.setObjectName("octubre_entry")
        self.label_36 = QtWidgets.QLabel(self.frame_3)
        self.label_36.setGeometry(QtCore.QRect(9, 250, 160, 30))
        self.label_36.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 16pt \"Sans Serif\";\n"
"background-color: rgb(255, 255, 127);\n"
"border: 2px solid black;\n"
"border-top: 0px\n"
"")
        self.label_36.setObjectName("label_36")
        self.septiembre_entry = QtWidgets.QTextEdit(self.frame_3)
        self.septiembre_entry.setGeometry(QtCore.QRect(230, 250, 140, 31))
        self.septiembre_entry.setStyleSheet("border-top: 0px")
        self.septiembre_entry.setObjectName("septiembre_entry")
        self.label_37 = QtWidgets.QLabel(self.frame_3)
        self.label_37.setGeometry(QtCore.QRect(9, 220, 160, 30))
        self.label_37.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-top-color: rgb(85, 255, 127);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 16pt \"Sans Serif\";\n"
"background-color: rgb(255, 255, 127);\n"
"border: 2px solid black;\n"
"border-top: 0 px solid black\n"
"")
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.frame_3)
        self.label_38.setGeometry(QtCore.QRect(9, 280, 160, 30))
        self.label_38.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-top-color: rgb(85, 255, 127);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 16pt \"Sans Serif\";\n"
"background-color: rgb(255, 255, 127);\n"
"border: 2px solid black;\n"
"border-top: 0 px solid black\n"
"")
        self.label_38.setObjectName("label_38")
        self.label_39 = QtWidgets.QLabel(self.frame_3)
        self.label_39.setGeometry(QtCore.QRect(9, 190, 160, 30))
        self.label_39.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 16pt \"Sans Serif\";\n"
"background-color: rgb(255, 255, 127);\n"
"border: 2px solid black;\n"
"border-top: 0px")
        self.label_39.setObjectName("label_39")
        self.label_40 = QtWidgets.QLabel(self.frame_3)
        self.label_40.setGeometry(QtCore.QRect(9, 310, 160, 30))
        self.label_40.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 16pt \"Sans Serif\";\n"
"background-color: rgb(255, 255, 127);\n"
"border: 2px solid black;\n"
"border-top: 0px\n"
"")
        self.label_40.setObjectName("label_40")
        self.label_41 = QtWidgets.QLabel(self.frame_3)
        self.label_41.setGeometry(QtCore.QRect(9, 340, 160, 30))
        self.label_41.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-top-color: rgb(85, 255, 127);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 16pt \"Sans Serif\";\n"
"background-color: rgb(255, 255, 127);\n"
"border: 2px solid black;\n"
"border-top: 0 px solid black\n"
"")
        self.label_41.setObjectName("label_41")
        self.diciembre_entry = QtWidgets.QTextEdit(self.frame_3)
        self.diciembre_entry.setGeometry(QtCore.QRect(230, 340, 140, 30))
        self.diciembre_entry.setStyleSheet("border-top: 0px")
        self.diciembre_entry.setObjectName("diciembre_entry")
        self.noviembre_entry = QtWidgets.QTextEdit(self.frame_3)
        self.noviembre_entry.setGeometry(QtCore.QRect(230, 310, 140, 31))
        self.noviembre_entry.setStyleSheet("border-top: 0px")
        self.noviembre_entry.setObjectName("noviembre_entry")
        self.marzo_comentarios_entry = QtWidgets.QTextEdit(self.frame_3)
        self.marzo_comentarios_entry.setGeometry(QtCore.QRect(450, 70, 310, 31))
        self.marzo_comentarios_entry.setObjectName("marzo_comentarios_entry")
        self.abril_comentarios_entry = QtWidgets.QTextEdit(self.frame_3)
        self.abril_comentarios_entry.setGeometry(QtCore.QRect(450, 100, 310, 30))
        self.abril_comentarios_entry.setStyleSheet("border-top: 0px")
        self.abril_comentarios_entry.setObjectName("abril_comentarios_entry")
        self.noviembre_comentarios_entry = QtWidgets.QTextEdit(self.frame_3)
        self.noviembre_comentarios_entry.setGeometry(QtCore.QRect(450, 310, 310, 31))
        self.noviembre_comentarios_entry.setStyleSheet("border-top: 0px")
        self.noviembre_comentarios_entry.setObjectName("noviembre_comentarios_entry")
        self.label_42 = QtWidgets.QLabel(self.frame_3)
        self.label_42.setGeometry(QtCore.QRect(450, 10, 310, 40))
        self.label_42.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 26pt \"Courier 10 Pitch\";\n"
"background-color: rgb(255, 255, 127);\n"
"border: 2px solid black;")
        self.label_42.setObjectName("label_42")
        self.junio_comentarios_entry = QtWidgets.QTextEdit(self.frame_3)
        self.junio_comentarios_entry.setGeometry(QtCore.QRect(450, 160, 310, 30))
        self.junio_comentarios_entry.setStyleSheet("border-top: 0px")
        self.junio_comentarios_entry.setObjectName("junio_comentarios_entry")
        self.diciembre_comentarios_entry = QtWidgets.QTextEdit(self.frame_3)
        self.diciembre_comentarios_entry.setGeometry(QtCore.QRect(450, 340, 310, 30))
        self.diciembre_comentarios_entry.setStyleSheet("border-top: 0px")
        self.diciembre_comentarios_entry.setObjectName("diciembre_comentarios_entry")
        self.octubre_comentarios_entry = QtWidgets.QTextEdit(self.frame_3)
        self.octubre_comentarios_entry.setGeometry(QtCore.QRect(450, 280, 310, 30))
        self.octubre_comentarios_entry.setStyleSheet("border-top: 0px")
        self.octubre_comentarios_entry.setObjectName("octubre_comentarios_entry")
        self.mayo_comentarios_entry = QtWidgets.QTextEdit(self.frame_3)
        self.mayo_comentarios_entry.setGeometry(QtCore.QRect(450, 130, 310, 31))
        self.mayo_comentarios_entry.setStyleSheet("border-top: 0px")
        self.mayo_comentarios_entry.setObjectName("mayo_comentarios_entry")
        self.julio_comentarios_entry = QtWidgets.QTextEdit(self.frame_3)
        self.julio_comentarios_entry.setGeometry(QtCore.QRect(450, 190, 310, 31))
        self.julio_comentarios_entry.setStyleSheet("border-top: 0px")
        self.julio_comentarios_entry.setObjectName("julio_comentarios_entry")
        self.septiembre_comentarios_entry = QtWidgets.QTextEdit(self.frame_3)
        self.septiembre_comentarios_entry.setGeometry(QtCore.QRect(450, 250, 310, 31))
        self.septiembre_comentarios_entry.setStyleSheet("border-top: 0px")
        self.septiembre_comentarios_entry.setObjectName("septiembre_comentarios_entry")
        self.agosto_comentarios_entry = QtWidgets.QTextEdit(self.frame_3)
        self.agosto_comentarios_entry.setGeometry(QtCore.QRect(450, 220, 310, 30))
        self.agosto_comentarios_entry.setStyleSheet("border-top: 0px")
        self.agosto_comentarios_entry.setObjectName("agosto_comentarios_entry")
        self.asociados_entry = QtWidgets.QPushButton(self.frame_3)
        self.asociados_entry.setGeometry(QtCore.QRect(230, 390, 531, 91))
        self.asociados_entry.setStyleSheet("font: 18pt \"cmr10\";\n"
"")
        self.asociados_entry.setObjectName("asociados_entry")
        self.label_43 = QtWidgets.QLabel(self.frame_3)
        self.label_43.setGeometry(QtCore.QRect(9, 390, 210, 91))
        self.label_43.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"font: 75 26pt \"Courier 10 Pitch\";\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 127);\n"
"border: 2px solid black;")
        self.label_43.setObjectName("label_43")
        self.tabWidget.addTab(self.tab_3, "")
        self.comen_entry = QtWidgets.QGroupBox(self.centralwidget)
        self.comen_entry.setGeometry(QtCore.QRect(10, 650, 1511, 171))
        self.comen_entry.setStyleSheet("font: 75 16pt \"Courier 10 Pitch\";\n"
"\n"
"")
        self.comen_entry.setObjectName("comen_entry")
        self.comentarios_entry = QtWidgets.QLineEdit(self.comen_entry)
        self.comentarios_entry.setGeometry(QtCore.QRect(2, 31, 1509, 121))
        self.comentarios_entry.setText("")
        self.comentarios_entry.setObjectName("comentarios_entry")
        self.nombrebusca_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.nombrebusca_entry.setGeometry(QtCore.QRect(10, 20, 641, 41))
        self.nombrebusca_entry.setStyleSheet("border: 2px solid black;")
        self.nombrebusca_entry.setText("")
        self.nombrebusca_entry.setObjectName("nombrebusca_entry")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(830, 20, 150, 41))
        self.pushButton.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(1200, 20, 140, 41))
        self.pushButton_4.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(1380, 20, 140, 41))
        self.pushButton_5.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(830, 90, 691, 571))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.subirfoto_boton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.subirfoto_boton.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"")
        self.subirfoto_boton.setObjectName("subirfoto_boton")
        self.gridLayout.addWidget(self.subirfoto_boton, 4, 0, 1, 1)
        self.foto_entry = QtWidgets.QLabel(self.gridLayoutWidget)
        self.foto_entry.setText("")
        self.foto_entry.setObjectName("foto_entry")
        self.gridLayout.addWidget(self.foto_entry, 0, 0, 1, 1)
        self.tomarfoto_boton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.tomarfoto_boton.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"")
        self.tomarfoto_boton.setObjectName("tomarfoto_boton")
        self.gridLayout.addWidget(self.tomarfoto_boton, 5, 0, 1, 1)
        self.subir_buton = QtWidgets.QPushButton(self.centralwidget)
        self.subir_buton.setGeometry(QtCore.QRect(1020, 20, 141, 41))
        self.subir_buton.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"")
        self.subir_buton.setObjectName("subir_buton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1539, 19))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.meses =(self.marzo_entry,self.abril_entry,self.mayo_entry,self.junio_entry,self.julio_entry,self.agosto_entry,self.septiembre_entry,self.octubre_entry,self.noviembre_entry,self.diciembre_entry,self.marzo_comentarios_entry,self.abril_comentarios_entry,self.mayo_comentarios_entry,self.junio_comentarios_entry,self.julio_comentarios_entry,self.agosto_comentarios_entry,self.septiembre_comentarios_entry,self.octubre_comentarios_entry,self.noviembre_comentarios_entry,self.diciembre_comentarios_entry)

        self.personales=(self.nombre_entry,self.apellidop_entry,self.apellidom_entry,self.nac_entry,self.dom_entry,self.tel1_entry,self.tel2_entry,self.tel3_entry,self.mail_entry,self.comentarios_entry)
        self.academicos = (self.curso_entry,self.teacher_entry,self.lib_entry,self.horario_entry,self.cole_entry,self.grado_entry,self.libcole_entry,"NPAGO")
        #,self.reglamento_entry,self.exoral_entry,self.exwritten_entry,self.inter_entry)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Nombre"))
        self.label_3.setText(_translate("MainWindow", "Apellido Paterno"))
        self.label_4.setText(_translate("MainWindow", "Fecha de Nac."))
        self.label_5.setText(_translate("MainWindow", "Apellido Materno"))
        self.label_7.setText(_translate("MainWindow", "Domicilio"))
        self.lineEdit_3.setText(_translate("MainWindow", "Detalle de teléfono 3"))
        self.lineEdit.setText(_translate("MainWindow", "Detalle de teléfono 1"))
        self.lineEdit_2.setText(_translate("MainWindow", "Detalle de teléfono 2"))
        self.label_6.setText(_translate("MainWindow", "Teléfonos"))
        self.label_8.setText(_translate("MainWindow", "Mail"))
        self.label_16.setText(_translate("MainWindow", "Edad"))
        self.nombre_entry.setToolTip(_translate("MainWindow", "<html><head/><body><p>Insterte nombre</p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "Contacto"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.label_18.setText(_translate("MainWindow", "Horario"))
        self.label_20.setText(_translate("MainWindow", "Teacher"))
        self.label_21.setText(_translate("MainWindow", "Libro"))
        self.label_22.setText(_translate("MainWindow", "Curso"))
        self.label_25.setText(_translate("MainWindow", "Grado"))
        self.label_26.setText(_translate("MainWindow", "Libro colegio"))
        self.label_27.setText(_translate("MainWindow", "Colegio"))
        self.label_23.setText(_translate("MainWindow", "Oral"))
        self.label_24.setText(_translate("MainWindow", "Escrito"))
        self.label_29.setText(_translate("MainWindow", "Nota"))
        self.label_28.setText(_translate("MainWindow", "Examen final"))
        self.label_44.setText(_translate("MainWindow", "¿Examenes internacionales?"))
        self.reglamento_entry.setText(_translate("MainWindow", " Reglamento leído"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.label_30.setText(_translate("MainWindow", "Marzo"))
        self.label_31.setText(_translate("MainWindow", "Abril"))
        self.label_32.setText(_translate("MainWindow", "Mes"))
        self.label_33.setText(_translate("MainWindow", "¿Pagó?"))
        self.label_34.setText(_translate("MainWindow", "Junio"))
        self.label_35.setText(_translate("MainWindow", "Mayo"))
        self.label_36.setText(_translate("MainWindow", "Septiembre"))
        self.label_37.setText(_translate("MainWindow", "Agosto"))
        self.label_38.setText(_translate("MainWindow", "Octubre"))
        self.label_39.setText(_translate("MainWindow", "Julio"))
        self.label_40.setText(_translate("MainWindow", "Noviembre"))
        self.label_41.setText(_translate("MainWindow", "Diciembre"))
        self.label_42.setText(_translate("MainWindow", "Comentarios"))
        self.label_43.setText(_translate("MainWindow", "Asociados"))
        self.asociados_entry.setText(_translate("MainWindow", "Haga click para asociar alumnos"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Page"))
        self.comen_entry.setTitle(_translate("MainWindow", "Comentarios"))
        self.nombrebusca_entry.setToolTip(_translate("MainWindow", "<html><head/><body><p>Escriba nombre completo</p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Buscar"))
        self.pushButton_4.setText(_translate("MainWindow", "Actualizar"))
        self.pushButton_5.setText(_translate("MainWindow", "Eliminar"))
        self.subirfoto_boton.setText(_translate("MainWindow", "Subir foto"))
        self.foto_entry.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>Acá va la fotito!</p></body></html>"))
        self.tomarfoto_boton.setText(_translate("MainWindow", "Tomar foto"))
        self.subir_buton.setText(_translate("MainWindow", "Subir"))



#####################################
###########################################################################
###########################################################################
###########################################################################
###########################################################################
###########################################################################
###########################################################################
#####################################
######################################
#####################################
######################################
#####################################
######################################
#####################################
######################################
#####################################
######################################
#####################################
######################################
#####################################
######################################
#####################################
######################################
#####################################
######################################
###########################################################################
######################################

        self.te_activo(MainWindow)


    def tomofoto(self):
        nombre=str(self.nombre_entry.text().replace(" ", ""))+str(self.apellidop_entry.text().replace(" ", ""))+str(self.apellidom_entry.text().replace(" ", ""))+".png"
        if nombre == '':
            print('Escribí algo amigo!')
        else:
            cam2.tomofoto(nombre)
            os.chdir("imagenes")
            image = cv2.imread(nombre)
            os.chdir("..")
            r = 700.0 / image.shape[1]
            dim = (700, int(image.shape[0] * r))
            resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
            coloreada = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)
            height, width, channel = coloreada.shape
            bytesPerLine = 3 * width
            convertida = QtGui.QImage(coloreada.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
            conv = QtGui.QPixmap(convertida)
            self.foto_entry.setPixmap(conv)

    def subo_foto(self):
        nombre=str(self.nombre_entry.text().replace(" ", ""))+str(self.apellidop_entry.text().replace(" ", ""))+str(self.apellidom_entry.text().replace(" ", ""))+".png"
        if nombre =='':
            print('Escribí algo amigo!')
        else:
            options = QtWidgets.QFileDialog.Options()
            options = QtWidgets.QFileDialog.DontUseNativeDialog
            fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self.ww,'Open File', '.')

            if fileName:
                image = cv2.imread(fileName)
                os.chdir("imagenes")
                cv2.imwrite(nombre,image)
                os.chdir("..")
                r = 700.0 / image.shape[1]
                dim = (700, int(image.shape[0] * r))
                resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
                coloreada = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)
                height, width, channel = coloreada.shape
                bytesPerLine = 3 * width
                convertida = QtGui.QImage(coloreada.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
                conv = QtGui.QPixmap(convertida)
                self.foto_entry.setPixmap(conv)

    def cargar_foto(self):
        nombre=str(self.nombre_entry.text().replace(" ", ""))+str(self.apellidop_entry.text().replace(" ", ""))+str(self.apellidom_entry.text().replace(" ", ""))+".png"
        if nombre =='':
            print('Escribí algo amigo!')
        else:
            os.chdir("imagenes")
            image = cv2.imread(nombre)
            os.chdir("..")
            try:
                r = 700.0 / image.shape[1]
                dim = (700, int(image.shape[0] * r))
                resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
                coloreada = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)
                height, width, channel = coloreada.shape
                bytesPerLine = 3 * width
                convertida = QtGui.QImage(coloreada.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
                conv = QtGui.QPixmap(convertida)
                self.foto_entry.setPixmap(conv)
            except AttributeError:
                pass

    def subirficha(self):
        xx=[]
        yy=[]
        zz=[]
        for i in self.personales:
            xx.append(i.text())
        for j in self.academicos:
            if j=="NPAGO":
                if os.path.isfile('npagos.csv') == False:
                    abba = [0]
                    self.df = pd.DataFrame({'npagos' : abba})
                    self.df.to_csv('npagos.csv')

                self.leo = pd.read_csv('npagos.csv')['npagos'].tolist()
                self.a = random.randint(1,10E10)
                while self.a in self.leo:
                    self.a = random.randint(1,10E10)
                self.leo.append(self.a)
                yy.append(self.a)
                self.df = pd.DataFrame({'npagos' : self.leo})
                self.df.to_csv('npagos.csv')
            else:
                yy.append(j.text())
        for k in self.meses:
            try:
                zz.append(k.text())
            except AttributeError:
                zz.append(k.toPlainText())
        self.datos.insertpersonales(xx)
        self.datos.insertacademicos(yy)
        self.datos.insertpagos(zz)
        self.get_data(self.model)
        for i in self.personales:
            i.setText('')
        for j in self.academicos:
            if j=="NPAGO":
                pass
            else:
                try:
                    j.setText('')
                except AttributeError:
                    k.setPlainText('')
        for j in self.meses:
            try:
                j.setText('')
            except AttributeError:
                k.setPlainText('')
        print('Subí una ficha :)')
        self.monsterinc()

    def actualizoficha(self):
        ind=self.indiceposta
        print(ind)
        xx=[]
        yy=[]
        zz=[]
        for i in self.personales:
            xx.append(i.text())
        for j in self.academicos:
            if j=="NPAGO":
                pass
            else:
                yy.append(j.text())
        for k in self.meses:
            try:
                zz.append(k.text())
            except AttributeError:
                zz.append(k.toPlainText())
        self.datos.actualiza_personales(xx,ind)
        self.datos.actualiza_academicos(yy,ind)
        self.datos.actualiza_historialpagos(zz,ind)
        self.get_data(self.model)
        for i in self.personales:
            i.setText('')
        for j in self.academicos:
            try:
                j.setText('')
            except AttributeError:
                k.setPlainText('')
        for j in self.meses:
            try:
                j.setText('')
            except AttributeError:
                k.setPlainText('')
        self.monsterinc()



    def monsterinc(self):
        image = cv2.imread('plus.jpg')
        r = 700.0 / image.shape[1]
        dim = (700, int(image.shape[0] * r))
        resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
        coloreada = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)
        height, width, channel = coloreada.shape
        bytesPerLine = 3 * width
        convertida = QtGui.QImage(coloreada.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
        conv = QtGui.QPixmap(convertida)
        self.foto_entry.setPixmap(conv)



    def get_data(self,model):
        datatod = []
        for data in self.datos.charly():
            datatod.append(str(data[1])+ ' ' +str(data[2])+' '+str(data[3]))
        model.setStringList(datatod)


    def buscador(self):
        encontrado=self.nombrebusca_entry.text().replace(" ", "")
        self.monsterinc()
        for data in self.datos.charly():
            todojunto=str(data[1]).replace(' ','')+str(data[2]).replace(' ','')+str(data[3]).replace(' ','')
            if encontrado==todojunto:
                ind=data[0]
                self.indiceposta=ind
                cucu=0
                for i in self.personales:
                    cucu=cucu+1
                    i.setText(data[cucu])
                cucu=0
                for i in self.academicos:
                    if i=="NPAGO":
                        pass
                    else:
                        cucu=cucu+1
                        i.setText(self.datos.juntoacademicos(ind)[0][cucu])
                cucu=0
                for i in self.meses:
                    cucu=cucu+1
                    try:
                        try:
                            i.setText(self.datos.juntomeses(ind)[0][cucu])
                        except IndexError:
                            pass
                    except AttributeError:
                        i.setPlainText(self.datos.juntomeses(ind)[0][cucu])
                self.cargar_foto()

    def matador(self):
        self.datos.mueran(self.indiceposta)
        self.get_data(self.model)
        for i in self.personales:
            i.setText('')
        for j in self.academicos:
            if j=="NPAGO":
                pass
            else:
                try:
                    j.setText('')
                except AttributeError:
                    k.setPlainText('')
        for j in self.meses:
            try:
                j.setText('')
            except AttributeError:
                k.setPlainText('')
        self.monsterinc()

    def mono(self):
        encontrado=self.nombrebusca_entry.text().replace(" ", "")
        self.monsterinc()
        self.DD=ass.II()
        for data in self.datos.charly():
            todojunto=str(data[1]).replace(' ','')+str(data[2]).replace(' ','')+str(data[3]).replace(' ','')
            if encontrado==todojunto:
                ind=data[0]
                nn=self.datos.doynum(ind)
                vars=self.datos.tedevuelvoimportante(nn)
                # self.DD.tipito1.setText(self.nombrebusca_entry.text())
                # print(vars[0])
                print(vars)
                self.DD.anotamelosnombres(vars[0],vars[1])
                self.DD.datainicial=data[0]
            self.DD.ii.show()


    def te_activo(self,MainWindow):
        self.subirfoto_boton.clicked.connect(self.subo_foto)
        self.subir_buton.clicked.connect(self.subirficha)
        self.pushButton.clicked.connect(self.buscador)
        self.pushButton_5.clicked.connect(self.matador)
        self.pushButton_4.clicked.connect(self.actualizoficha)
        self.tomarfoto_boton.clicked.connect(self.tomofoto)
        self.ww = MainWindow
        self.ww.move(0,0)
        completer = QtWidgets.QCompleter()
        self.nombrebusca_entry.setCompleter(completer)
        self.model = QtCore.QStringListModel()
        completer.setModel(self.model)
        self.get_data(self.model)
        self.asociados_entry.clicked.connect(self.mono)
        self.monsterinc()
        # self.asociados_entry.mouseClickevent=self.mono()
        QtWidgets.QShortcut(QtGui.QKeySequence("Shift+Return"), self.nombrebusca_entry, self.buscador)
    #    QtWidgets.QShortcut(QtGui.QKeySequence("Return"), self.asociados_entry, self.mono)



#####################################
#####################################
#####################################
#####################################
#####################################
