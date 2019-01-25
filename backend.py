import sqlite3
import random


def connect():
    conn = sqlite3.connect('paggi.db')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS paggio(id INTEGER PRIMARY KEY, nome \
                TEXT, pag INTEGER) ')
    conn.commit()
    conn.close()


""" ANNULLATA per test


def ricerca():
    conn = sqlite3.connect("paggi.db")
    cur = conn.cursor()
    # linea modificta, n era passato alla funzione
    n = paggezza_text.get()
    # fine modifica
    cur.execute("SELECT pag FROM paggi WHERE nome = ? ", n)
    num = int(cur.fetchone())
    conn.close()
    if (num == ""):
        return random.randint(0, 100)
    return num

"""


def insert(nome, numero):
    conn = sqlite3.connect("paggi.db")
    cur = conn.cursor()
    cur.execute('INSERT INTO paggio VALUES(NULL,?,?)', (nome, numero))
    conn.commit()
    conn.close()


connect()
insert("luca", 10)
insert("giulia", 30)
insert("lella", 100)
