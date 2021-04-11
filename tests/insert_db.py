import sqlite3

usuario_prueba = "hola1"
ciudad_prueba = "madrid"
cp_prueba = 11111

con = sqlite3.connect('../sherpa_app/db/sherpa.db')
cur = con.cursor()
print("Opened database successfully")

cur.execute("INSERT INTO master (usuario) \
               VALUES (?)",(usuario_prueba,))

cur.execute("INSERT INTO detalle (ciudad,cp,usuario) \
               VALUES (?,?,?)",(ciudad_prueba, cp_prueba, usuario_prueba))

print("Inserted data successfully")

for row in cur.execute("SELECT * FROM master"):
    print(row)

for row in cur.execute("SELECT * FROM detalle"):
    print(row)

print("Selected data successfully")

#con.commit()

con.close()