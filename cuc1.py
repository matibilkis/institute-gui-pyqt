# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cursos_edit.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import comanditos



class GG(object):
    def __init__(self):
        super(GG,self).__init__()
        MainWindow = QtWidgets.QMainWindow()
        self.tablite = comanditos.Tablota("DATOS.db")
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 459)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.nombrebusca_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.nombrebusca_entry.setGeometry(QtCore.QRect(20, 10, 510, 60))
        self.nombrebusca_entry.setStyleSheet("border: 2px solid black;\n"
"font: 18pt \"Gargi\";")
        self.nombrebusca_entry.setText("")
        self.nombrebusca_entry.setObjectName("nombrebusca_entry")
        self.editar = QtWidgets.QPushButton(self.centralwidget)
        self.editar.setGeometry(QtCore.QRect(570, 200, 140, 70))
        self.editar.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"")
        self.editar.setObjectName("editar")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(20, 150, 161, 40))
        self.label_20.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"background-color: rgb(255, 255, 127);\n"
"border: 2px solid black;")
        self.label_20.setObjectName("label_20")
        self.teacher_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.teacher_entry.setGeometry(QtCore.QRect(220, 150, 311, 41))
        self.teacher_entry.setStyleSheet("font: 14pt \"Gargi\";")
        self.teacher_entry.setObjectName("teacher_entry")
        self.curso_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.curso_entry.setGeometry(QtCore.QRect(220, 90, 311, 41))
        self.curso_entry.setStyleSheet("font: 14pt \"Gargi\";")
        self.curso_entry.setText("")
        self.curso_entry.setObjectName("curso_entry")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(20, 90, 161, 40))
        self.label_22.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"background-color: rgb(255, 255, 127);\n"
"border: 2px solid black;")
        self.label_22.setObjectName("label_22")
        self.buscar = QtWidgets.QPushButton(self.centralwidget)
        self.buscar.setGeometry(QtCore.QRect(570, 10, 140, 70))
        self.buscar.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"")
        self.buscar.setObjectName("buscar")
        self.subir = QtWidgets.QPushButton(self.centralwidget)
        self.subir.setGeometry(QtCore.QRect(570, 100, 140, 70))
        self.subir.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"")
        self.subir.setObjectName("subir")
        self.valor_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.valor_entry.setGeometry(QtCore.QRect(220, 210, 311, 41))
        self.valor_entry.setStyleSheet("font: 14pt \"Gargi\";")
        self.valor_entry.setText("")
        self.valor_entry.setObjectName("valor_entry")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(20, 210, 161, 40))
        self.label_23.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"background-color: rgb(255, 255, 127);\n"
"border: 2px solid black;")
        self.label_23.setObjectName("label_23")
        self.borrar = QtWidgets.QPushButton(self.centralwidget)
        self.borrar.setGeometry(QtCore.QRect(570, 300, 140, 70))
        self.borrar.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"")
        self.borrar.setObjectName("borrar")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(20, 330, 161, 40))
        self.label_24.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"background-color: rgb(255, 255, 127);\n"
"border: 2px solid black;")
        self.label_24.setObjectName("label_24")
        self.book_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.book_entry.setGeometry(QtCore.QRect(220, 330, 311, 41))
        self.book_entry.setStyleSheet("font: 14pt \"Gargi\";")
        self.book_entry.setText("")
        self.book_entry.setObjectName("book_entry")
        self.horario_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.horario_entry.setGeometry(QtCore.QRect(220, 270, 311, 41))
        self.horario_entry.setStyleSheet("font: 14pt \"Gargi\";")
        self.horario_entry.setText("")
        self.horario_entry.setObjectName("horario_entry")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(20, 270, 161, 40))
        self.label_25.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Courier 10 Pitch\";\n"
"background-color: rgb(255, 255, 127);\n"
"border: 2px solid black;")
        self.label_25.setObjectName("label_25")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 750, 19))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)




##############################################################
        self.subir.clicked.connect(self.subir_fun)
        self.borrar.clicked.connect(self.borrar_fun)
        self.editar.clicked.connect(self.editar_fun)
        self.buscar.clicked.connect(self.buscar_fun)
        self.buscar.clicked.connect(self.buscorad)

        completer = QtWidgets.QCompleter()
        self.nombrebusca_entry.setCompleter(completer)
        self.model = QtCore.QStringListModel()
        completer.setModel(self.model)
        self.get_data(self.model)


        self.escrito = (self.curso_entry,self.teacher_entry,self.valor_entry,self.book_entry,self.horario_entry)
        QtWidgets.QShortcut(QtGui.QKeySequence("Shift+Return"), self.nombrebusca_entry, self.buscorad)

        self.teactiv(MainWindow)
#########################

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.nombrebusca_entry.setToolTip(_translate("MainWindow", "<html><head/><body><p>Escriba nombre completo</p></body></html>"))
        self.editar.setText(_translate("MainWindow", "Editar"))
        self.label_20.setText(_translate("MainWindow", "Teacher"))
        self.label_22.setText(_translate("MainWindow", "Curso"))
        self.buscar.setText(_translate("MainWindow", "Buscar"))
        self.subir.setText(_translate("MainWindow", "Subir"))
        self.label_23.setText(_translate("MainWindow", "Valor"))
        self.borrar.setText(_translate("MainWindow", "Borrar"))
        self.label_24.setText(_translate("MainWindow", "Book(s)"))
        self.label_25.setText(_translate("MainWindow", "Horario"))


    def get_data(self,model):
        datatod = []
        for data in self.tablite.todos():
            datatod.append(str(data[1])+ ' ' +str(data[2])+' '+str(data[5]))
            # cursos_todos.append(str(data[1]))
            # teacher_todos.append(str[data[2]])
            # horarios_todos.append(str[data[3]])
        model.setStringList(datatod)
        print(datatod)

    def buscorad(self):
        encontrado=self.nombrebusca_entry.text().replace(" ", "")
        toditos = []
        indice_indicado=[]
        cucu=0
        for data in self.tablite.todos():
            cucu=cucu+1
            #toditos.append(str(data[1])+str(data[2])+str(data[3]))
            #indice_indicado[cucu] = data[0]
            momentaneo = [str(data[1]),str(data[2]),str(data[3]),str(data[4]),str(data[5])]
            mmm=str(data[1])+str(data[2])+str(data[5])
            mmmm=mmm.replace(" ", "")
            if encontrado==mmmm:
                for i in range(0,5):
                    self.escrito[i].setText(momentaneo[i])
            else:
                pass

    def gid(self):
        id = self.tablite.getid(self.curso_entry.text(),self.teacher_entry.text(),self.valor_entry.text(),self.book_entry.text(),self.horario_entry.text())
        return id[0][0]

    def subir_fun(self):
        self.tablite.insert(self.curso_entry.text(),self.teacher_entry.text(),self.valor_entry.text(),self.book_entry.text(),self.horario_entry.text())
        for i in range(0,5):
            self.escrito[i].setText('')
        self.get_data(self.model)
        self.nombrebusca_entry.setText('')


    def borrar_fun(self):
        print(self.gid())
        self.tablite.die(self.gid())
        self.get_data(self.model)
        for i in range(0,5):
            self.escrito[i].setText('')
        self.nombrebusca_entry.setText('')

    def editar_fun(self):

        self.tablite.update(self.gid(),self.curso_entry.text(),self.teacher_entry.text(),self.valor_entry.text(),self.book_entry.text(),self.horario_entry.text())
        for i in range(0,5):
            self.escrito[i].setText('')
        self.get_data(self.model)
        self.nombrebusca_entry.setText('')

    def buscar_fun(self):
        buscado = self.tablite.buscabruto(self.curso_entry.text(),self.teacher_entry.text(),self.valor_entry.text(),self.book_entry.text(),self.horario_entry.text())
        if buscado==[]:
            pass
        else:
            for i in range(0,5):
                self.escrito[i].setText(str(buscado[0][i+1]))

    def teactiv(self,MainWindow):
        self.ww = MainWindow
        self.ww.move(0,0)



# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     ui = GG()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
