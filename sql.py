import sqlite3
import time

def reg_user(id,ref):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute(""" CREATE TABLE IF NOT EXISTS user_time (
        id BIGINT,
        time_start BIGINT,
        time_bat_oplata,
        ref,
        status,
        viplata
        ) """)
    db.commit()

    if ref == '':
        ref = 'pusto'

    sql.execute(f"SELECT id FROM user_time WHERE id ='{id}'")
    if sql.fetchone() is None:
        time_start =round(time.time())
        sql.execute(f"INSERT INTO user_time VALUES (?,?,?,?,?,?)", (id,time_start,0,ref,0,0))
        db.commit()

    for i in sql.execute(f"SELECT * FROM user_time"):
        print(i)

def reg_time_bat_oplata(id):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    time_bat_oplata = round(time.time())
    sql.execute(f"UPDATE user_time SET time_bat_oplata= {time_bat_oplata}  WHERE id = {id} and time_bat_oplata = {0}")
    db.commit()

    for i in sql.execute(f"SELECT * FROM user_time"):
        print(i)

def info_ref(id):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    vsego = 0
    status = 0
    oplata = 0

    for i in sql.execute(f"SELECT ref FROM user_time WHERE ref = '{id}'"):
        vsego += 1
    for i in sql.execute(f"SELECT status FROM user_time WHERE ref = '{id}' and status = {1}"):
        status += 1

    oplata = sql.execute(f"SELECT viplata FROM user_time WHERE id = '{id}'").fetchone()
    oplata = oplata[0]


    return vsego,status,oplata
