from fastapi import FastAPI
from app.database.database import create_tables

app = FastAPI()

create_tables()

@app.get("/")
def home():
    return {"mensagem": "Olá, Barbearia!"}