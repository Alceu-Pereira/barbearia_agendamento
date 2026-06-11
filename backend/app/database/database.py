import sqlite3

DATABASE_NAME = "barbearia.db"

def get_connection():
    connection = sqlite3.connect(DATABASE_NAME)
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


def create_tables():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            telefone TEXT NOT NULL
        )
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS barbeiros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
            )

        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS agendamentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data DATE NOT NULL,
            hora TIME NOT NULL,
            status VARCHAR(100) NOT NULL,
            cliente_id INTEGER NOT NULL,
            barbeiro_id INTEGER NOT NULL,

            FOREIGN KEY (cliente_id) REFERENCES clientes(id),
            FOREIGN KEY (barbeiro_id) REFERENCES barbeiros(id)
            )
        """
    )

    connection.commit()
    connection.close()