import sqlite3

con = sqlite3.connect("DEMO.db")
cur = con.cursor()
sql = "CREATE TABLE IF NOT EXISTS test(id INTEGER PRIMARY KEY,name TEXT,age INTEGER)"
cur.execute(sql)
