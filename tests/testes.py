from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

# def test_ola_mundo():
#     response = client.get("/")
#     assert response.status_code == 200


# def test_ola_mundo_conteudo():
#     response = client.get("/")
#     assert response.json() == {"message": "Olá, mundo!"}

# def test_listar_produtos_status_code():
#     response = client.get("/produtos")
#     assert response.status_code == 200

