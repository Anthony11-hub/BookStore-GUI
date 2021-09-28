import sqlite3
# oop is about encapsulating objects inside a class
class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.c = self.conn.cursor()#this is a local variable
        self.c.execute("""
        CREATE TABLE IF NOT EXISTS book (
        id INTEGER PRIMARY KEY,
        title text,
        author text,
        year integer,
        isbn integer)
        """)
        self.conn.commit()

    def insert(self,title, author, year, isbn):
        self.c.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title, author, year, isbn))
        self.conn.commit()

    def view(self):
        self.c.execute("SELECT * FROM book")
        rows = self.c.fetchall()
        return rows

    def search(self,title="", author="", year="", isbn=""):
        self.c.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
        rows = self.c.fetchall()
        return rows

    def delete(self,id):
        self.c.execute("DELETE FROM book WHERE id=?", (id,))
        self.conn.commit()


    def update(self,id, title, author, year, isbn):
        self.c.execute("UPDATE book SET title=?,author=?,year=?,isbn=? WHERE id=?", (title, author, year, isbn, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

