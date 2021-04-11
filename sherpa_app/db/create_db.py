import sqlite3

con = sqlite3.connect('sherpa.db')
cur = con.cursor()
print("Opened database successfully")

cur.execute('CREATE TABLE master (usuario TEXT PRIMARY KEY)')
print("Table master created successfully")

cur.execute('CREATE TABLE detalle (detalle_id INTEGER PRIMARY KEY, \
                                    ciudad TEXT NOT NULL, \
                                    cp INTEGER NOT NULL, \
                                    usuario TEXT NOT NULL,\
                                    FOREIGN KEY (usuario) \
                                        REFERENCES master (usuario))')
print("Table detalle created successfully")

con.commit()

con.close()