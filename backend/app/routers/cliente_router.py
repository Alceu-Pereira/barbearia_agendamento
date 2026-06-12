from fastapi import APIRouter
from app.schemas.cliente_schema import ClienteCreate
from app.repositories.cliente_repository import (
    criar_cliente,
    listar_clientes
)

router = APIRouter()

@router.post("/clientes")
def cadastrar_cliente(cliente: ClienteCreate):
    criar_cliente(
        cliente.nome,
        cliente.telefone
    )
    return {
        "nome": cliente.nome,
        "telefone": cliente.telefone
    }

@router.get("/clientes")
def buscar_clientes():
    return listar_clientes()