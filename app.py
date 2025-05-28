from flask import Flask, render_template
from banco import engine, Session
from modelo import ItemPedido, Pedido, Produto, Cliente
from random import choice
from concurrent.futures import ProcessPoolExecutor



app = Flask(__name__)

pedidos_concluidos = []
pedidos_ativos = []
pedidos_cancelados = []

@app.route('/')
def index():
    return render_template('index/index.html',title='Eletromercio - Home')


@app.route('/pedido', methods=['POST'])
def pedido():
    executor = ProcessPoolExecutor()
    executor.submit(processar_pedidos)
    return {'mensagem': 'Pedido recebido com sucesso'}, 202

@app.route('/relatorio')
def relatorio():
    with Session() as session:
        pedidos = session.query(Pedido).all()
        return render_template('index/relatorio.html', pedidos=pedidos)


@app.route('/status')
def status():
    with Session() as session:
        total_concluidos = session.query(Pedido).count()
        total_ativos = session.query(Pedido).filter(Pedido.itens.any()).count()
        total_cancelados = session.query(Pedido).filter(Pedido.itens == None).count()

        return render_template('index/status.html',concluidos=total_concluidos, ativos=total_ativos, cancelados=total_cancelados)

    
def processar_pedidos():
    with Session() as session:
        try:

            clientes = session.query(Cliente).filter(Cliente.saldo > 0).all()
            if not clientes:
                raise ValueError("Nenhum cliente com saldo disponível")

            cliente = choice(clientes)

            produtos = session.query(Produto).filter(Produto.estoque > 0, Produto.preco <= cliente.saldo).all()

            if not produtos:
                raise ValueError(f"{cliente.nome} não tem produtos acessíveis com o saldo atual")

            produto = choice(produtos)

            pedido = Pedido(cliente=cliente)
            item_pedido = ItemPedido(pedido=pedido, produto=produto, quantidade=1)

            cliente.saldo -= produto.preco
            produto.estoque -= 1

            session.add(pedido)
            session.add(item_pedido)
            session.commit()

            pedidos_concluidos.append(pedido)

        except Exception as e:
            session.rollback()
            print(f"❌ Erro ao processar pedido: {e}")

    
if __name__ == '__main__':
    app.run(debug=True)
