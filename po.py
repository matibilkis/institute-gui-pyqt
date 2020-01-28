# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'backu.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import comandos
import os
import fichas_1
import cuc1
import pag


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Rainbow Institute")
        Form.resize(1423, 575)
        Form.move(0,0)
        self.datosup = comandos.Tablota("DATOS.db")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(20, 139, 921, 410))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 919, 408))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setGeometry(QtCore.QRect(0, 0, 230, 31))
        self.label.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"background-color: rgb(255, 255, 127);\n"
"border: 2px solid black;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setGeometry(QtCore.QRect(230, 0, 230, 31))
        self.label_2.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"background-color: rgb(255, 255, 127);\n"
"border: 2px solid black;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setGeometry(QtCore.QRect(460, 0, 230, 31))
        self.label_3.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"background-color: rgb(255, 255, 127);\n"
"border: 2px solid black;")
        self.label_3.setObjectName("label_3")
        self.monto1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.monto1.setGeometry(QtCore.QRect(0, 30, 230, 22))
        self.monto1.setObjectName("monto1")
        self.detalle1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.detalle1.setGeometry(QtCore.QRect(230, 30, 230, 22))
        self.detalle1.setObjectName("detalle1")
        self.horario1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.horario1.setGeometry(QtCore.QRect(460, 30, 230, 22))
        self.horario1.setObjectName("horario1")
        self.secre1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.secre1.setGeometry(QtCore.QRect(690, 30, 230, 22))
        self.secre1.setObjectName("secre1")
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setGeometry(QtCore.QRect(690, 0, 230, 31))
        self.label_4.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"background-color: rgb(255, 255, 127);\n"
"border: 2px solid black;")
        self.label_4.setObjectName("label_4")
        self.monto2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.monto2.setGeometry(QtCore.QRect(0, 50, 230, 22))
        self.monto2.setObjectName("monto2")
        self.detalle2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.detalle2.setGeometry(QtCore.QRect(230, 50, 230, 22))
        self.detalle2.setObjectName("detalle2")
        self.horario2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.horario2.setGeometry(QtCore.QRect(460, 50, 230, 22))
        self.horario2.setObjectName("horario2")
        self.secre2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.secre2.setGeometry(QtCore.QRect(690, 50, 230, 22))
        self.secre2.setObjectName("secre2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.buscanombre = QtWidgets.QLineEdit(Form)
        self.buscanombre.setGeometry(QtCore.QRect(20, 10, 750, 90))
        self.buscanombre.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"border: 2px solid black;")
        self.buscanombre.setText("")
        self.buscanombre.setObjectName("buscanombre")
        self.verficha = QtWidgets.QPushButton(Form)
        self.verficha.setGeometry(QtCore.QRect(790, 10, 150, 40))
        self.verficha.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"border: 2px solid black;")
        self.verficha.setObjectName("verficha")
        self.pagarcuota = QtWidgets.QPushButton(Form)
        self.pagarcuota.setGeometry(QtCore.QRect(790, 60, 150, 40))
        self.pagarcuota.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"border: 2px solid black;")
        self.pagarcuota.setObjectName("pagarcuota")
        self.actualizarcaja = QtWidgets.QPushButton(Form)
        self.actualizarcaja.setGeometry(QtCore.QRect(20, 120, 920, 20))
        self.actualizarcaja.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"border: 2px solid black;\n"
"border-bottom: 0px")
        self.actualizarcaja.setObjectName("actualizarcaja")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(960, 430, 421, 121))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.cajanum = QtWidgets.QLCDNumber(self.frame)
        self.cajanum.setGeometry(QtCore.QRect(231, 0, 190, 41))
        self.cajanum.setStyleSheet("font: 16pt \"Sans Serif\";")
        self.cajanum.setObjectName("cajanum")
        self.cajanum_2 = QtWidgets.QLCDNumber(self.frame)
        self.cajanum_2.setGeometry(QtCore.QRect(230, 40, 191, 41))
        self.cajanum_2.setStyleSheet("font: 16pt \"Sans Serif\";")
        self.cajanum_2.setObjectName("cajanum_2")
        self.cajanum_3 = QtWidgets.QLCDNumber(self.frame)
        self.cajanum_3.setGeometry(QtCore.QRect(230, 80, 191, 41))
        self.cajanum_3.setStyleSheet("font: 16pt \"Sans Serif\";")
        self.cajanum_3.setObjectName("cajanum_3")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 233, 40))
        self.label_5.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"background-color: rgb(255, 255, 127);\n"
"border: 2px solid black;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(0, 40, 233, 40))
        self.label_6.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"background-color: rgb(255, 255, 127);\n"
"border: 2px solid black;")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(0, 80, 233, 40))
        self.label_7.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"background-color: rgb(255, 255, 127);\n"
"border: 2px solid black;")
        self.label_7.setObjectName("label_7")
        self.actualizarcaja_2 = QtWidgets.QPushButton(Form)
        self.actualizarcaja_2.setGeometry(QtCore.QRect(960, 410, 421, 20))
        self.actualizarcaja_2.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"border: 2px solid black;\n"
"border-bottom: 0px")
        self.actualizarcaja_2.setObjectName("actualizarcaja_2")
        self.cursosbuton = QtWidgets.QPushButton(Form)
        self.cursosbuton.setGeometry(QtCore.QRect(960, 0, 221, 141))
        self.cursosbuton.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"border: 2px solid black;")
        self.cursosbuton.setObjectName("cursosbuton")
        self.gastobuton = QtWidgets.QPushButton(Form)
        self.gastobuton.setGeometry(QtCore.QRect(960, 150, 221, 141))
        self.gastobuton.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"border: 2px solid black;")
        self.gastobuton.setObjectName("gastobuton")
        self.fichasbuton = QtWidgets.QPushButton(Form)
        self.fichasbuton.setGeometry(QtCore.QRect(1190, 0, 220, 141))
        self.fichasbuton.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"border: 2px solid black;")
        self.fichasbuton.setObjectName("fichasbuton")
        self.cuotabuton = QtWidgets.QPushButton(Form)
        self.cuotabuton.setGeometry(QtCore.QRect(1190, 150, 220, 141))
        self.cuotabuton.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"border: 2px solid black;")
        self.cuotabuton.setObjectName("cuotabuton")
        self.usbuton = QtWidgets.QPushButton(Form)
        self.usbuton.setGeometry(QtCore.QRect(960, 300, 451, 61))
        self.usbuton.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"border: 2px solid black;")
        self.usbuton.setObjectName("usbuton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.activo()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Monto"))
        self.label_2.setText(_translate("Form", "Detalle"))
        self.label_3.setText(_translate("Form", "Horario"))
        self.label_4.setText(_translate("Form", "Registrado por"))
        self.verficha.setText(_translate("Form", "Ver ficha"))
        self.pagarcuota.setText(_translate("Form", "Paga cuota"))
        self.actualizarcaja.setText(_translate("Form", "Movimientos de caja"))
        self.label_5.setText(_translate("Form", "Dinero en caja"))
        self.label_6.setText(_translate("Form", "Gastos de hoy"))
        self.label_7.setText(_translate("Form", "Ingresos de hoy"))
        self.actualizarcaja_2.setText(_translate("Form", "Números de la caja"))
        self.cursosbuton.setText(_translate("Form", "Cursos"))
        self.gastobuton.setText(_translate("Form", "Gasto"))
        self.fichasbuton.setText(_translate("Form", "Fichas"))
        self.cuotabuton.setText(_translate("Form", "Cuota"))
        self.usbuton.setText(_translate("Form", "Cambiar de usuario"))

    def activo(self):
        self.fichasbuton.clicked.connect(self.abrifichas)
        self.cursosbuton.clicked.connect(self.abricursos)
        self.verficha.clicked.connect(self.buscador)
        self.cuotabuton.clicked.connect(self.abrirpago)
        self.pagarcuota.clicked.connect(self.buscadorcuota)
        QtWidgets.QShortcut(QtGui.QKeySequence("Shift+Return"), self.buscanombre, self.buscador)
        QtWidgets.QShortcut(QtGui.QKeySequence("Shift+C"), self.buscanombre, self.abrirpago)
        completer = QtWidgets.QCompleter()
        self.buscanombre.setCompleter(completer)
        self.model = QtCore.QStringListModel()
        completer.setModel(self.model)
        self.get_data(self.model)

    def get_data(self,model):
        datatod = []
        for data in self.datosup.charly():
            datatod.append(str(data[1])+ ' ' +str(data[2])+' '+str(data[3]))
            # cursos_todos.append(str(data[1]))
            # teacher_todos.append(str[data[2]])
            # horarios_todos.append(str[data[3]])
        model.setStringList(datatod)


    def abrifichas(self):
        self.AAA=fichas_1.FF()
        self.AAA.ww.show()

    def abricursos(self):
        self.BB=cuc1.GG()
        self.BB.ww.show()

    def abrirpago(self):
        self.CC=pag.HH()
        self.CC.hh.show()

    def buscador(self):
        encontradoo=self.buscanombre.text().replace(" ", "")
        for data in self.datosup.charly():
        # mmm=self.datos.junto(int(data[3]))
            todojunto=str(data[1]).replace(' ','')+str(data[2]).replace(' ','')+str(data[3]).replace(' ','')
            if encontradoo==todojunto:
                self.enfichas=fichas_1.FF()
                self.enfichas.nombrebusca_entry.setText(self.buscanombre.text())
                self.enfichas.buscador()
                self.enfichas.ww.show()

    def buscadorcuota(self):
        encontradoo=self.buscanombre.text().replace(" ", "")
        for data in self.datosup.charly():
        # mmm=self.datos.junto(int(data[3]))
            todojunto=str(data[1]).replace(' ','')+str(data[2]).replace(' ','')+str(data[3]).replace(' ','')
            if encontradoo==todojunto:
                self.enfichas=pag.HH()
                self.enfichas.buscanombre.setText(self.buscanombre.text())
                self.enfichas.buscador()
                self.enfichas.hh.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
