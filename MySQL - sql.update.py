#!/usr/bin/python
import pymysql
db = pymysql.connect("localhost", "root", "", "test")
cursor = db.cursor()
sql = """
    UPDATE testtable SET age = 50 WHERE name = "Andrzej"
    """
try:
    cursor.execute(sql)
    db.commit()
except:
    print('BŁĄD KOMENDY')
    db.rollback()
db.close()
