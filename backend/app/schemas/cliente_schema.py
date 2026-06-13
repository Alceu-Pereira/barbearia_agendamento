from pydantic import BaseModel

class ClienteCreate(BaseModel):
    nome: str
    telefone: str

class ClienteUpdate(BaseModel):
    nome: str
    telefone: str
    