import sqlite3

MonConection = sqlite3.connect("PrimereBase")

MonCoursor = MonConection.cursor()

# MonCoursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(20), PRECIO INTEGER, SECCION VARCHAR(20))")

# MonCoursor.execute("INSERT INTO PRODUCTOS VALUES('Pan', 2000, 'Panaderia')")

"""AutresProductos = [
    ("Camiseta", 10, "Deportes"),
    ("Jarron", 90, "Ceramica"),
    ("Camion", 20, "Jugueteria")

]"""

# MonCoursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)", AutresProductos)

MonCoursor.execute("SELECT * FROM PRODUCTOS")

VarProductos = MonCoursor.fetchall()

for producto in VarProductos:
    print("Nombre Articulo: ", producto[0], "Seccion: ", producto[2])

MonConection.commit()

MonConection.close()
