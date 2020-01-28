import sqlite3
from numpy import random
import pandas as pd
import os

class Tablota:
    def __init__(self,db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS personales (id INTEGER PRIMARY KEY, nombre text, apellidop text, apellidom text, fechanac date, domicilio text, tel1 text, tel2 text, tel3 text, mail text, comments text)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS academicos (id INTEGER PRIMARY KEY, curso text, teacher text, libro text, horario text, colegio text, grado text, libcolegio text, npago text)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS historialpagos (id INTEGER PRIMARY KEY, marzo text, abril text, mayo text, junio text, julio text, agosto text, septiembre text, octubre text, noviembre text, diciembre text, detmarzo text, detabril text, detmayo text, detjunio text, detjulio text, detagosto text, detseptiembre text, detoctubre text, detnoviembre text, detdiciembre text)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS cursosrainbow (id INTEGER PRIMARY KEY, curso text, teacher text, valor real, libro text, horario text)")
        self.conn.commit()
#, reglamento text, exaoral text, exacrito text, exaint text, inter text)")

    def getid(self,nombre="",apellidop="",apelidom=""):
        self.cur.execute("SELECT id FROM personales WHERE nombre=? OR apellido=? OR apellido_materno=?", (nombre,apellidop,apellidom))
        idd=self.cur.fetchall()
        return idd

    def getid(self,nombre="",apellidop="",apelidom=""):
        self.cur.execute("SELECT id FROM personales WHERE nombre=? OR apellido=? OR apellido_materno=?", (nombre,apellidop,apellidom))
        idd=self.cur.fetchall()
        return idd

    def doynum(self,id=""):
        self.cur.execute("SELECT npago FROM academicos WHERE id=?",(id,))
        nn=self.cur.fetchall()
        return nn[0][0]

    def charly(self):
        self.cur.execute("SELECT * FROM personales")
        rows = self.cur.fetchall()
        return rows

    def junto(self,idn):
        self.cur.execute("SELECT * FROM personales WHERE id=?", (idn,))
        rows = self.cur.fetchall()
        return rows

    def juntoacademicos(self,idn):
        self.cur.execute("SELECT * FROM academicos WHERE id=?", (idn,))
        rows = self.cur.fetchall()
        return rows

    def juntomeses(self,idn):
        self.cur.execute("SELECT * FROM historialpagos WHERE id=?", (idn,))
        rows = self.cur.fetchall()
        return rows

    def buscar(nombre="",apellido="",apellidom=""):
        self.cur.execute("SELECT * FROM personales WHERE nombre=? OR apellido=? OR apellido_materno=?", (nombre,apellidop,apellidom))
        row=self.cur.fetchall()
        idnum= row['id']
        self.cur.execute("SELECT * FROM personales WHERE id=?",(idnum))
        rpersonales = self.cur.techall()
        self.cur.execute("SELECT * FROM academicos WHERE id=?",(idnum))
        racademicos = self.cur.techall()
        self.cur.execute("SELECT * FROM historialpagos WHERE id=?",(idnum))
        rhistorialpagos = self.cur.techall()
        return [rpersonales, racademicos, rhistorialpagos]

    def insertpersonales(self,xx):
        self.cur.execute("INSERT INTO personales (nombre, apellidop, apellidom, fechanac, domicilio, tel1 ,tel2 ,tel3, mail, comments) VALUES (?,?,?,?,?,?,?,?,?,?)",xx)
        self.conn.commit()
        self.cur.execute("SELECT * FROM personales")
        rows1=self.cur.fetchall()
        return rows1

    def nprandom(self,id):
        self.leo = pd.read_csv('npagos.csv')['npagos'].tolist()
        self.a = random.randint(1,10E10)
        while self.a in self.leo:
            self.a = random.randint(1,10E10)
        self.leo.append(self.a)
        self.cur.execute("UPDATE academicos SET npago=? WHERE id=?",(self.a,id[0],))
        self.conn.commit()

    def tepongonumerodeel(self,idini,id):
        nn=self.numerito(idini)[0]
        print(nn)
        self.cur.execute("UPDATE academicos SET npago=? WHERE id=? ",(nn,id,))
        self.conn.commit()

    def numerito(self,id):
        self.cur.execute("SELECT npago FROM academicos WHERE id=? ",(id,))
        self.conn.commit()
        return self.cur.fetchall()[0]

    def tedevuelvoimportante(self,num):
        self.cur.execute("SELECT id FROM academicos WHERE npago=?",(num,))
        self.conn.commit()
        ids=self.cur.fetchall()
        nombres=[]
        cursos=[]
        valores=[]
        idds=[]
        for id in ids:
            idd=id[0]
            self.cur.execute("SELECT nombre,apellidop,apellidom FROM personales WHERE id=?", (idd,))
            self.conn.commit()
            nombre_completo=self.cur.fetchall()[0]
            idds.append(id)
            self.cur.execute("SELECT curso FROM academicos WHERE id=?", (idd,))
            self.conn.commit()
            cc=self.cur.fetchall()
            self.cur.execute("SELECT valor FROM cursosrainbow WHERE curso=?", (cc[0][0],))
            self.conn.commit()
            vv=self.cur.fetchall()
            nombres.append(str(nombre_completo[0])+" "+str(nombre_completo[1])+" "+str(nombre_completo[2]))
            cursos.append(cc[0])
            #valores.append(vv[0])
        return [idds,nombres,cursos,valores]


    def insertacademicos(self,yy):
        self.cur.execute("INSERT INTO academicos (curso,teacher,libro,horario,colegio,grado,libcolegio,npago) VALUES (?,?,?,?,?,?,?,?)", yy)
        self.conn.commit()
        rows2=self.cur.fetchall()
        return rows2

    def insertpagos(self,zz):
        self.cur.execute("INSERT INTO historialpagos (marzo, abril, mayo, junio, julio, agosto, septiembre, octubre, noviembre, diciembre, detmarzo, detabril, detmayo, detjunio, detjulio, detagosto, detseptiembre, detoctubre, detnoviembre, detdiciembre) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", zz)
        self.conn.commit()
        rows3=self.cur.fetchall()
        return rows3

    def actualiza_personales(self,xx,id):
        self.cur.execute("UPDATE personales SET nombre=?, apellidop=?, apellidom=?, fechanac=?, domicilio=?, tel1=? ,tel2=? ,tel3=?, mail=?, comments=? WHERE id=?", (xx[0],xx[1],xx[2],xx[3],xx[4],xx[5],xx[6],xx[7],xx[8],xx[9],id))
        self.conn.commit()
        self.cur.execute("SELECT * FROM personales")
        rows=self.cur.fetchall()
        return rows

    def actualiza_academicos(self,xx,id):
        self.cur.execute("UPDATE academicos SET curso=?,teacher=?,libro=?,horario=?,colegio=?,grado=?,libcolegio=? WHERE id=?", (xx[0],xx[1],xx[2],xx[3],xx[4],xx[5],xx[6],id))
        self.conn.commit()
        self.cur.execute("SELECT * FROM academicos")
        rows=self.cur.fetchall()
        return rows

    def actualiza_historialpagos(self,xx,id):
        self.cur.execute("UPDATE historialpagos SET marzo=?, abril=?, mayo=?, junio=?, julio=?, agosto=?, septiembre=?, octubre=?, noviembre=?, diciembre=?, detmarzo=?, detabril=?, detmayo=?, detjunio=?, detjulio=?, detagosto=?, detseptiembre=?, detoctubre=?, detnoviembre=?, detdiciembre=? WHERE id=?", (xx[0],xx[1],xx[2],xx[3],xx[4],xx[5],xx[6],xx[7],xx[8],xx[9],xx[10],xx[11],xx[12],xx[13],xx[14],xx[15],xx[16],xx[17],xx[18],xx[19],id))
        self.conn.commit()
        self.cur.execute("SELECT * FROM historialpagos")
        rows=self.cur.fetchall()
        return rows

    def mueran(self,num_id):
        self.cur.execute("DELETE FROM personales WHERE id=?", (num_id,))
        self.conn.commit()
        self.cur.execute("DELETE FROM academicos WHERE id=?", (num_id,))
        self.conn.commit()
        self.cur.execute("DELETE FROM historialpagos WHERE id=?", (num_id,))
        self.conn.commit()


    def __del__(self):
        self.conn.close()
