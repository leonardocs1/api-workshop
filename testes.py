from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_ola_mundo():
    response = client.get("/")
    assert response.status_code == 200


def test_ola_mundo_conteudo():
    response = client.get("/")
    assert response.json() == {"message": "Olá, mundo!"}

def test_listar_produtos_status_code():
    response = client.get("/produtos")
    assert response.status_code == 200

def test_tamanho_da_lista_produtos():
    response = client.get("/produtos")
    assert len(response.json()) == 3

def test_obter_produto_existente():
    response = client.get("/produtos/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "titulo": "Cadeira Gamer",
        "descricao": "Cadeira confortável para fazer live",
        "preço": 5.0,
    }