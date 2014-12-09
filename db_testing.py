import sqlite3

#simple example
with sqlite3.connect("database.db") as con:
    cur = con.cursor()
    print cur.execute("select * from account_holder").fetchall()
    
    
