from typing import Any, Dict, List

class Produtos:
    produtos: List[Dict[str, Any]] = [
        {
            "id": 1,
            "titulo": "Cadeira Gamer",
            "descricao": "Cadeira confortável para fazer live",
            "preco": 5.0,
        },
        {
            "id": 2,
            "titulo": "Workshop",
            "descricao": "Workshop de deploy",
            "preco": 100.0,
        },
        {
            "id": 3,
            "titulo": "Iphone",
            "descricao": "Iphone 14",
            "preco": 999.0,  # ou qualquer float válido
        }
    ]

    def listar_produtos(self):
        return self.produtos
    
    def buscar_produto(self, produto_id):
        for produto in self.produtos:
            if produto["id"] == produto_id:
                return produto
        return {"error": "Produto não encontrado"}
    
    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        return produto