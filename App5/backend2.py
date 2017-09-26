
import sqlite3

def dbConn():
    return(sqlite3.connect("books2.db"))

def connect():
    conn = dbConn()
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")

    conn.commit()
    conn.close()

def insert(title, author, year, isbn):

    conn = dbConn()
    cur = conn.cursor()

    cur.execute("INSERT INTO book VALUES(NULL, ?, ?, ?, ?)" , (title, author, year, isbn)  )

    conn.commit()
    conn.close()

def view():

    conn = dbConn()
    cur = conn.cursor()

    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.commit()
    conn.close()

    return(rows)


insert("test", "me", 2000, 123)

connect()


