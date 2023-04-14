from flask import Flask, request, jsonify, make_response
from typing import List
import mysql.connector

# Importar as classes Produto e Cliente dos módulos correspondentes
from produto import Produto
from cliente import Cliente

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='quickstore',
)

app = Flask(name)


class Pedido:
    def init(self, idpedido: int, produtos: List[Produto], cliente: Cliente):
        mycursor = mydb.cursor()
        mycursor.execute('SELECT * FROM Produto')
        meus_pedidos = mycursor.fetchall()
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
    mycursor = mydb.cursor()
    sql = f"insert into produto(idpedido, produtos, cliente) values  ('{data['idpedido']}',{data['produtos']},{data['cliente']});"
    mycursor.execute(sql)
    mydb.commit()
    return make_response(
       jsonify(
           mensagem='Feito com sucesso',
       )
   )
    #data = request.json
    #idpedido = data['idpedido']
    #produtos = [Produto(p['idproduto'], p['nome'], p['preco']) for p in data['produtos']]
    #cliente = Cliente(data['cliente']['idcliente'], data['cliente']['nome'])
    #pedido = Pedido(idpedido, produtos, cliente)
    #pedidos.append(pedido)
    #return jsonify({'message': 'Pedido criado com sucesso!'})


# Atualizar um pedido existente
@app.route('/pedidos/<int:idpedido>', methods=['PUT'])
def atualizar_pedido(idpedido):
    data = request.json
    idpedido = data['idpedido']
    produtos = data['produtos']
    cliente = data['cliente']
    mycursor1 = mydb.cursor()
    sql1 = f"UPDATE pedido SET idpedido, produtos, cliente = ('{data['idpedido']}',{data['produtos']},{data['cliente']});"
    mycursor1.execute(sql1)
    mydb.commit()
    return make_response

    #pedido = buscar_pedido(idpedido)
   # if pedido:
   #     data = request.json
   #     produtos = [Produto(p['idproduto'], p['nome'], p['preco']) for p in data['produtos']]
   #     cliente = Cliente(data['cliente']['idcliente'], data['cliente']['nome'])
   #     pedido.produtos = produtos
    #    pedido.cliente = cliente
   #     return jsonify({'message': 'Pedido atualizado com sucesso!'})
   # else:
   #     return jsonify({'message': 'Pedido não encontrado.'}), 404


# Deletar um pedido existente
@app.route('/pedidos/<int:idpedido>', methods=['DELETE'])
def deletar_pedido(idpedido):
    data = request.json
    idpedido = data['idpedido']
    mycursor = mydb.cursor()
    sql = f"DELETE FROM produto WHERE id = ('{data['id']}')"
    mycursor.execute(sql)
    mydb.commit()
    return make_response()
    #pedido = buscar_pedido(idpedido)
    #if pedido:
    #    pedidos.remove(pedido)
     #   return jsonify({'message': 'Pedido deletado com sucesso!'})
    #else:
     #   return jsonify({'message': 'Pedido não encontrado.'}), 404
