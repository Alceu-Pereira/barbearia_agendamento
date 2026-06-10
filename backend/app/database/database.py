import sqlite3

DATABASE_NAME = "barbearia.db"

def get_connection():
    return sqlite3.connect(DATABASE_NAME)

def create_tables():
    connection = get_connection()
    cursor = connection.cursor(
        """
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            telefone TEXT NOT NULL
        )
        """
    )

    connection.commit()
    connection.close()