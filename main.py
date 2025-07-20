from typing import Any, Dict, List
from fastapi import FastAPI

app = FastAPI()

produtos: List[Dict[str, Any]] = [
    {
        "id": 1,
        "titulo": "Cadeira Gamer",
        "descricao": "Cadeira confortável para fazer live",
        "preço": 5.0,
    },
    {
        "id": 2,
        "a titulo": "Workshop",
        "descricao": "Workshop de deploy",
        "preço": 100.00,
    },
    {
        "id": 3,
        "a titulo": "Iphone",
        "descricao": "Iphone 14",
        "preço": None,
    },
]

@app.get("/")
def ola_mundo():
    return {"message": "Olá, mundo!"}

@app.get("/produtos")
def listar_produtos():
    return produtos

@app.get("/produtos/{produto_id}")
def obter_produto(produto_id: int):
    for produto in produtos:
        if produto["id"] == produto_id:
            return produto
    return {"error": "Produto não encontrado"}, 404

