#!/usr/bin/python
import pymysql
db = pymysql.connect("localhost", "root", "", "users")
cursor = db.cursor()

#wrzucamy komendę dla SQLa
sql = "SELECT * FROM Table WHERE Name = 'abc'"

#uruchamiamy zapytanie
try:
    cursor.execute(sql)
    db.commit()
except:
    print("błąd komendy")
    db.rollback()
