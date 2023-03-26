from flask import Flask, request, jsonify
from typing import List

# Importar as classes Produto e Cliente dos módulos correspondentes
from produto import Produto
from cliente import Cliente


app = Flask(__name__)


class Pedido:
    def __init__(self, idpedido: int, produtos: List[Produto], cliente: Cliente):
        self.idpedido = idpedido
        self.produtos = produtos
        self.cliente = cliente


# Criar alguns pedidos de exemplo
pedidos = [
    Pedido(1, [Produto(1, 'Camiseta', 29.90)], Cliente(1, 'João')),
    Pedido(2, [Produto(2, 'Calça Jeans', 99.90), Produto(3, 'Camisa Social', 79.90)], Cliente(2, 'Maria')),
    Pedido(3, [Produto(4, 'Tênis', 149.90)], Cliente(3, 'José'))
]


# Função para buscar um pedido pelo ID
def buscar_pedido(idpedido):
    for pedido in pedidos:
        if pedido.idpedido == idpedido:
            return pedido
    return None


# Criar um novo pedido
@app.route('/pedidos', methods=['POST'])
def criar_pedido():
    data = request.json
    idpedido = data['idpedido']
    produtos = [Produto(p['idproduto'], p['nome'], p['preco']) for p in data['produtos']]
    cliente = Cliente(data['cliente']['idcliente'], data['cliente']['nome'])
    pedido = Pedido(idpedido, produtos, cliente)
    pedidos.append(pedido)
    return jsonify({'message': 'Pedido criado com sucesso!'})


# Atualizar um pedido existente
@app.route('/pedidos/<int:idpedido>', methods=['PUT'])
def atualizar_pedido(idpedido):
    pedido = buscar_pedido(idpedido)
    if pedido:
        data = request.json
        produtos = [Produto(p['idproduto'], p['nome'], p['preco']) for p in data['produtos']]
        cliente = Cliente(data['cliente']['idcliente'], data['cliente']['nome'])
        pedido.produtos = produtos
        pedido.cliente = cliente
        return jsonify({'message': 'Pedido atualizado com sucesso!'})
    else:
        return jsonify({'message': 'Pedido não encontrado.'}), 404


# Deletar um pedido existente
@app.route('/pedidos/<int:idpedido>', methods=['DELETE'])
def deletar_pedido(idpedido):
    pedido = buscar_pedido(idpedido)
    if pedido:
        pedidos.remove(pedido)
        return jsonify({'message': 'Pedido deletado com sucesso!'})
    else:
        return jsonify({'message': 'Pedido não encontrado.'}), 404
