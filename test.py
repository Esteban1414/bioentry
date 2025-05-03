import MySQLdb

try:
    db = MySQLdb.connect(
        host="localhost",
        user="root",
        passwd="",
        db="bioentry"
    )
    print("¡Conexión exitosa a la base de datos!")
    cursor = db.cursor()
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    print("Tablas en tu base de datos:", tables)
    db.close()
except Exception as e:
    print("Error de conexión:", e)