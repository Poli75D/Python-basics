#!/usr/bin/python
import pymysql
db = pymysql.connect("localhost", "root", "", "test")
cursor = db.cursor()
sql = """
    INSERT INTO testtable (
    name, location, gender, age)
    VALUES ('Krzysztof', 'PL', 'M', 25)
    """
try:
    cursor.execute(sql)
    
    db.commit()
except:
    print('BŁĄD KOMENDY')
    db.rollback()

db.close()
