import os
import mysql.connector

def reconnect():
    db = mysql.connector.connect(
        host=os.getenv("MYSQLHOST"),
        user=os.getenv("MYSQLUSER"),
        password=os.getenv("MYSQLPASSWORD"),
        database=os.getenv("MYSQL_DATABASE"),
        port=int(os.getenv("MYSQLPORT")),
        autocommit=True,
        connection_timeout=30,
        consume_results=True
    )

    cursor = db.cursor()

    return db, cursor