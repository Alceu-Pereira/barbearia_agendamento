from fastapi import FastAPI
from app.database.database import create_tables
from app.routers.cliente_router import router

app = FastAPI()

app.include_router(router)

create_tables()

@app.get("/")
def home():
    return {"mensagem": "Olá, Barbearia!"}