#!/usr/bin/python
import pymysql
db = pymysql.connect("localhost", "root", "", "test")
cursor = db.cursor()
sql = '''CREATE TABLE TestTable (
    name CHAR(20) NOT NULL,
    location CHAR(100),
    gender CHAR(1),
    age INTEGER )'''

cursor.execute(sql)
db.close()
