from banco import Session
from modelo import Pedido, ItemPedido, Produto, Cliente

def popular_banco():
    with Session() as session:
        clientes = [
            Cliente(nome='Joao Pedro', saldo=12000),
            Cliente(nome='Bianca Cristine', saldo=15000),
            Cliente(nome='Henrique Lecce', saldo=20000),    
            Cliente(nome='Marcos Selmini', saldo=25000),
            Cliente(nome='Flavio Azevedo', saldo=0),
            Cliente(nome='Carlos Rafael', saldo=1000),
        ]
        produtos = [
            Produto(nome='iPhone 14 Pro Max', preco=7999.00, estoque=10),
            Produto(nome='Samsung Galaxy S23 Ultra', preco=5999.00, estoque=5),
            Produto(nome='MacBook Pro 16', preco=23999.00, estoque=3),
            Produto(nome='Dell XPS 13', preco=9999.00, estoque=7),
            Produto(nome='PlayStation 5', preco=4999.00, estoque=15),
            Produto(nome='Xbox Series X', preco=4999.00, estoque=8),
            Produto(nome='Nintendo Switch', preco=2999.00, estoque=20),
            Produto(nome='AirPods Pro', preco=2499.00, estoque=12),
            Produto(nome='Galaxy Buds Pro', preco=1999.00, estoque=10),
            Produto(nome='Apple Watch Series 8', preco=4999.00, estoque=5),
            Produto(nome='Samsung Galaxy Watch 5', preco=3999.00, estoque=8),
            
        ]
        
        session.add_all(clientes + produtos)
        session.commit()
        print("✅ Banco populado com sucesso!")
        
if __name__ == "__main__":
    popular_banco()