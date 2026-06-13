from app.database.database import get_connection

def criar_cliente(nome, telefone):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        """
        INSERT INTO clientes (nome, telefone)
        VALUES (?, ?)
        """,
        (nome, telefone)
    )

    connection.commit()
    connection.close()

def listar_clientes():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT * FROM clientes
        """
    )

    clientes = cursor.fetchall()
    
    connection.close()

    return clientes

def buscar_cliente_por_id(cliente_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT * FROM clientes
        WHERE id = ?
        """,
        (cliente_id,)
    )
    cliente = cursor.fetchone()
    connection.close()
    return cliente

