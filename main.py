from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def ola_mundo():
    return {"message": "Olá, mundo!"}
