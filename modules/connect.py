import sqlite3

con = sqlite3.connect("db/main.db")
c = con.cursor()
con.isolation_level = None

close  = con.close