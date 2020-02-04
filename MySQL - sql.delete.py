#!/usr/bin/python
import pymysql
db = pymysql.connect("localhost", "root", "", "test")
cursor = db.cursor()
sql = """
    DELETE FROM testtable WHERE name = 'Jedras'
    """
try:
    cursor.execute(sql)
    db.commit()
except:
    print('BŁĄD KOMENDY')
    db.rollback()
db.close()
