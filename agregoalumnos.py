from PyQt5 import QtCore, QtGui, QtWidgets
import comandos

class Agrego(object):
    def __init__(self,nas,SCROLL):
        self.scrollAreaWidgetContents = SCROLL
        asociados=grupodepago.quienes(nas)
        [self.sx,self.sy,self.inialx,self.inicurx,self.inimonx,self.alturaini]=[250,40,40,350,620,80]

        for i in asociados:
            self.alumno = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
            self.curso = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            self.monto = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            self.alumno.setGeometry(QtCore.QRect(self.inialx,self.alturaini, self.sx, self.sy))
            self.curso.setGeometry(QtCore.QRect(self.inicurx,self.alturaini, self.sx, self.sy))
            self.monto.setGeometry(QtCore.QRect(self.inimonx, self.alturaini, self.sx, self.sy))

            self.alumno.setText(i[0])
            self.curso.setTexto(i[1])
            self.monto.setText(i[2])

            self.style(self.alumno)
            self.style(self.curso)
            self.style(self.monto)




    def style(self,obj):
        obj.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"border: 2px solid black;")
