import sqlite3

MonConection = sqlite3.connect("GestionProduits")

MonCursor = MonConection.cursor()
# Create
"""
MonCursor.execute('''
    CREATE TABLE PRODUCTOS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
    PRECIO INTERGER,
    SECCION VARCHAR(20))
'''
                  )

Produits = [
    ("Pelota", 20, "Jugueteria"),
    ("Pantalon", 15, "Confeccion"),
    ("Destornillador", 25, "Ferreteria"),
    ("Jarron", 45, "Ceramica"),
    ("Pantalones", 35, "Confeccion")
]

MonCursor.executemany("INSERT INTO PRODUCTOS VALUES(NULL, ?, ?, ?)", Produits)

# MonCursor.execute("INSERT INTO PRODUCTOS VALUES('AR05', 'Tren', 15, 'Jugueteria')")
"""
# Reader
"""
MonCursor.execute("SELECT * FROM PRODUCTOS")
VarProduits = MonCursor.fetchall()
for produit in VarProduits:
    print(produit)
"""
# Update
"""
MonCursor.execute("UPDATE PRODUCTOS SET PRECIO=35 WHERE NOMBRE_ARTICULO='Pelota'")
"""
# Delete
"""
MonCursor.execute("DELETE FROM PRODUCTOS WHERE ID=5")
"""
MonConection.commit()

MonConection.close()
