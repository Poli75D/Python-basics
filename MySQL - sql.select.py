#!/usr/bin/python
import pymysql
db = pymysql.connect("localhost", "root", "", "test")
cursor = db.cursor()
sql = "SELECT * FROM testtable"
try:
    cursor.execute(sql)
    results = cursor.fetchall()  
    for row in results:
        name = row[0]
        location = row[1]
        gender = row[2]
        age = row[3]
        print("Name: %s, Location: %s, Gender: %s, Age: %s" % (name, location, gender, age))
        db.commit()
except:
    print('BŁĄD KOMENDY')
    db.rollback()
db.close()
