from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .schema import ProdutoSchema
from .config import SessionLocal, get_db
from .model import Produto

router = APIRouter()

@router.get("/")
def ola_mundo():
    return {"message": "Olá, mundo!"}

@router.get("/produtos", response_model=list[ProdutoSchema])
def listar_produtos(db: Session = Depends(get_db)):
    return db.query(Produto).all()

@router.get("/produtos/{produto_id}", response_model=ProdutoSchema)
def obter_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = db.query(Produto).filter(Produto.id == produto_id).first()
    if produto:
        return produto
    else:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

@router.post("/produtos", response_model=ProdutoSchema)
def adicionar_produto(produto: ProdutoSchema, db: Session = Depends(get_db)):
    db_produto = Produto(**produto.model_dump())
    db.add(db_produto)
    db.commit()
    db.refresh(db_produto)
    return db_produto

@router.delete("/produtos/{produto_id}")
def remover_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = db.query(Produto).filter(Produto.id == produto_id).first()
    if produto:
        db.delete(produto)
        db.commit()
        return {"message": "Produto removido com sucesso"}
    else:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    
@router.put("/produtos/{produto_id}", response_model=ProdutoSchema)
def atualizar_produto(produto_id: int, produto: ProdutoSchema, db: Session = Depends(get_db)):
    db_produto = db.query(Produto).filter(Produto.id == produto_id).first()
    if db_produto:
        for key, value in produto.model_dump().items():
            setattr(db_produto, key, value) if value else None
        db.commit()
        db.refresh(db_produto)
        return db_produto 
    else:
        raise HTTPException(status_code=404, detail="Produto não encontrado")