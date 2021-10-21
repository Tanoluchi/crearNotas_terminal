import mysql.connector

def conectar():

    database = mysql.connector.connect(
        host        = "localhost",
        user        = "root",
        passwd      = "",
        database    = "aplicacion",
        port        = 3306
    )

    # Activamos el uso de cache
    cursor = database.cursor(buffered = True)

    return [database, cursor]