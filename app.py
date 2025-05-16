from flask import Flask, render_template, session
from banco import engine
from modelo import ItemPedido, Pedido, Produto, Cliente
from random import choice



app = Flask(__name__)

pedidos_concluidos = []
pedidos_ativos = []
pedidos_cancelados = []

@app.route('/')
def index():
    return render_template(
        'index/index.html',
        title='Eletromercio - Home',
        pedidos_ativos=pedidos_ativos,
        pedidos_concluidos=pedidos_concluidos,
        pedidos_cancelados=pedidos_cancelados
    )

@app.route('/pedidos')
def pedidos():
    return render_template(
        'index/pedidos.html',
        title='Eletromercio - Pedidos',
        pedidos_ativos=pedidos_ativos,
        pedidos_concluidos=pedidos_concluidos,
        pedidos_cancelados=pedidos_cancelados
    )
    
def precessar_pedidos():
    with engine.connect() as connection:
        try:
            cliente = choice(session.query(Cliente).all())
            produto = choice(session.query(Produto).all())
            
            if cliente.saldo < produto.preco:
                raise ValueError("Saldo insuficiente")
            if produto.estoque <= 0:
                raise ValueError("Produto fora de estoque")
            
            with session.begin():
                pedido = Pedido(cliente=cliente)
                item_pedido = ItemPedido(pedido=pedido, produto=produto, quantidade=1)
                
                cliente.saldo -= produto.preco
                produto.estoque -= 1
                
                pedidos_ativos.append(pedido)
                
                connection.execute(Pedido.__table__.insert(), pedido)
                connection.execute(ItemPedido.__table__.insert(), item_pedido)
                
                pedidos_concluidos.append(pedido)
        except Exception as e:
            print(f"Erro ao processar pedido: {e}")
            pedidos_cancelados.append(pedido)
            connection.rollback()  

    
if __name__ == '__main__':
    app.run(debug=True)
