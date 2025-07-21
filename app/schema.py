from pydantic import BaseModel, PositiveInt
from typing import Optional

class ProdutoSchema(BaseModel):
    id: int
    titulo: str
    descricao: Optional[str] = None
    preco: PositiveInt 
