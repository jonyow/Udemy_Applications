
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

def search(title = "", author = "", year ="", isbn =""):
    conn = dbConn()
    cur = conn.cursor()

    cur.execute("SELECT * FROM book WHERE title LIKE ? OR author LIKE ? or year = ? or isbn = ?", (title, author, year, isbn))
    rows = cur.fetchall()

    conn.commit()
    conn.close()
    return(rows)

def delete(id):
    conn = dbConn()
    cur = conn.cursor()

    cur.execute("DELETE FROM book WHERE ID=?", (id,))

    conn.commit()
    conn.close()

def update(id, title, author, year, isbn):
    conn = dbConn()
    cur = conn.cursor()

    cur.execute("UPDATE book SET title =?, author=?, year=?, isbn=? WHERE ID=?", (title, author, year, isbn, id))

    conn.commit()
    conn.close()

connect

# insert("test3", "me3", 2000, 1234)
# view()
