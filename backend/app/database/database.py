import sqlite3

# Nome do Banco de Dados
DATABASE_NAME = "barbearia.db"

# Função para conectar-se o banco de dados
def get_connection():
    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    return connection

# Função para criar as tabelas
def create_tables():
    
    # Conexão
    connection = get_connection()

    # Envia e processa os comandos
    cursor = connection.cursor()

    # Executa a operação contida
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

    # Salva a operação
    connection.commit()

    # Encerra a conexão
    connection.close()