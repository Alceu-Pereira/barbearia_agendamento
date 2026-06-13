from fastapi import APIRouter, HTTPException
from app.schemas.cliente_schema import ClienteCreate
from app.repositories.cliente_repository import (
    criar_cliente,
    listar_clientes,
    buscar_cliente_por_id,
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

@router.get("/clientes/{cliente_id}")
def buscar_cliente(cliente_id: int):
    cliente = buscar_cliente_por_id(cliente_id)
    if cliente is None:
        raise HTTPException(
            status_code=404,
            detail="Cliente não encontrado"
        )
    
    return cliente