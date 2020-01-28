import pandas as pd
import sqlite3

db=sqlite3.connect("DATOS.db")
acl=pd.read_sql_query("select * from academicos",db)
al=pd.read_sql_query("select * from personales",db)
print(al)
print(acl)
