from fastapi import FastAPI
from .schema import ProdutoSchema
from .routes import router
from typing import List


app = FastAPI()

app.include_router(router)
