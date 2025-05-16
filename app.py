from flask import Flask, render_template
from banco import engine

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

if __name__ == '__main__':
    app.run(debug=True)
