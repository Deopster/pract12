import string
from random import randint
import random

from fastapi import FastAPI,HTTPException
import mysql.connector
from mysql.connector import connect, Error
try:
    connection = connect(
        host="host.docker.internal",
        user="root",
        password="Andrey16",
    )
except Error as e:
    print(e)
def makeTranz(out):
    with connection.cursor() as cursor:
        cursor.execute(out)
mycursor = connection.cursor()
makeTranz("CREATE DATABASE IF NOT EXISTS BAZA")
create_table = """
CREATE TABLE IF NOT EXISTS objects (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)
"""
mycursor.execute("USE BAZA")
mycursor.execute(create_table)


app = FastAPI()
@app.get("/sec_hello")
def read_root():
    mycursor = connection.cursor()
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for _ in range(5))
    sql = f"insert into objects(name,age) VALUES (%s, %s)"
    value = (rand_string, randint(1, 99))
    mycursor.execute(sql, value)
    connection.commit()
    return {"output": f"hello from second data was add ${value}"}
@app.get("/sec_bye")
def read_root():
    mycursor.execute("SELECT * FROM objects")
    rez=''
    for row in mycursor.fetchall():
        print(row)
        rez+=" "+str(row)
    connection.commit()
    return {"output": rez}
@app.get("/health")
def health():
    return

