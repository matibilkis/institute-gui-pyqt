import sqlite3

class Tablota:
    def __init__(self,db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS cursosrainbow (id INTEGER PRIMARY KEY, curso text, teacher text, valor real, libro text, horario text)")
        self.conn.commit()

    def todos(self):
        self.cur.execute("SELECT * FROM cursosrainbow")
        rows = self.cur.fetchall()
        return rows

    def buscar(self,id):
        self.cur.execute("SELECT * FROM cursosrainbow WHERE id=?", (id))
        rows=self.cur.fetchall()
        return rows

    def buscabruto(self,curso,teacher,valor,horario,libro):
        self.cur.execute("SELECT * FROM cursosrainbow WHERE curso=? OR teacher=? OR valor=? OR libro=? OR horario=?", (curso,teacher,valor,libro,horario))
        rows=self.cur.fetchall()
        return rows


    def update(self,id,curso,teacher,valor,libro,horario):
        self.cur.execute("UPDATE cursosrainbow SET curso=?, teacher=?, valor=?, libro=?, horario=? WHERE id=?", (curso,teacher,valor,libro,horario,id))
        self.conn.commit()
        self.cur.execute("SELECT * FROM cursosrainbow")
        rows=self.cur.fetchall()
        return rows

    def getid(self,curso,teacher,valor,libro,horario):
        self.cur.execute("SELECT id FROM cursosrainbow WHERE curso=? OR teacher=? OR valor=? OR libro=? OR horario=?", (curso,teacher,valor,libro,horario))
        idd=self.cur.fetchall()
        return idd


    def insert(self,curso,teacher,valor,libro,horario):
        self.cur.execute("INSERT INTO cursosrainbow VALUES (NULL,?,?,?,?,?)",(curso,teacher,valor,libro,horario))
        self.conn.commit()
        self.cur.execute("SELECT * FROM cursosrainbow")
        rows1=self.cur.fetchall()
        return rows1

    def die(self,num_id):
        self.cur.execute("DELETE FROM cursosrainbow WHERE id=?", (num_id,))
        self.conn.commit()
        self.cur.execute("SELECT * FROM cursosrainbow")
        rows1=self.cur.fetchall()
        return rows1


    # def update(self,nombre,apellido,curso,documento):
    #     self.cur.execute("UPDATE fichas SET curso=?, documento=? WHERE nombre=? OR apellido=?",(curso,documento,nombre,apellido))
    #     self.conn.commit()
    #     self.cur.execute("SELECT * FROM fichas")
    #     rows=self.cur.fetchall()
    #     return rows

    def __del__(self):
        self.conn.close()
