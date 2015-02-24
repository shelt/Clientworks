import sqlite3

main_con = sqlite3.connect("db/main.db")
main_con.isolation_level = None
c = main_con.cursor()

# Sessions (sid, uid)
#          (sid int, uid int)

# Users    (uid, username, hash, salt, pid, charname, email)
#          (uid int, username text, hash text, salt text, pid int, charname text, email text)

c.execute("CREATE TABLE IF NOT EXISTS Sessions (sid int, uid int)")
c.execute("CREATE TABLE IF NOT EXISTS Users (uid int, username text, hash text, salt text, pid int, charname text, email text)")

# root user for development purposes
from modules import crypto
salt = crypto.get_salt()
hash = crypto.get_hash("toor", salt)
charname = "NA"
email = "root@localhost.com"
data = {
"username":"root",
"hash":hash,
"salt":salt,
"pid": -1,
"charname":charname,
"email":email
}
c.execute("""INSERT INTO Users (uid, username, hash, salt, pid, charname, email)
                         VALUES(0, :username, :hash, :salt, :pid, :charname, :email)""", data)

main_con.close()