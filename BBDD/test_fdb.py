import fdb

ConectionFDB = fdb.connect(database="C:/Temps/scat.fdb", user='SYSDBA', password='masterkey')
FDBCursor = ConectionFDB.cursor()
Voir = FDBCursor.execute("SELECT * FROM TB_PERSONA ORDER BY NOMBRE")
for lista in Voir:
    print(lista)
