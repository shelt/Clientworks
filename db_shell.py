import sqlite3

con = sqlite3.connect("db/main.db")
con.isolation_level = None
c = con.cursor()

buffer = ""

print ":: SQL Shell ::"
print "::   " + sqlite3.version + "   ::"

while True:
    print("> "),
    line = raw_input()
    if line == "exit":
        break
    buffer += line
    if sqlite3.complete_statement(buffer):
        try:
            buffer = buffer.strip()
            c.execute(buffer)

            if buffer.lstrip().upper().startswith("SELECT"):
                print c.fetchall()
        except sqlite3.Error as e:
            print "! ", e.args[0]
        buffer = ""
con.close()