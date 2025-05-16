from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

class Cliente():
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    saldo = Column(Float)

class Produto():
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    preco = Column(Float)
    estoque = Column(Integer)

class Pedido():
    __tablename__ = 'pedidos'
    id = Column(Integer, primary_key=True)
    cliente_id = Column(Integer, ForeignKey('clientes.id'))
    cliente = relationship('Cliente')
    itens = relationship('ItemPedido')

class ItemPedido():
    __tablename__ = 'itens_pedido'
    id = Column(Integer, primary_key=True)
    pedido_id = Column(Integer, ForeignKey('pedidos.id'))
    produto_id = Column(Integer, ForeignKey('produtos.id'))
    quantidade = Column(Integer)
    pedido = relationship('Pedido')
    produto = relationship('Produto')


