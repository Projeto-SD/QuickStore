
from flask import Flask, request, jsonify, make_response
from typing import List
import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='quickstore',
)

class Produto:
    def __init__(self, nomeProduto, idProduto: int, preco: float, quantidade: int):
        self.nomeProduto = nomeProduto
        self.idProduto = idProduto
        self.preco = preco
        self.quantidade = quantidade


# teste
produtos = [
    Produto("Parafuso",998,11.90,122),
    Produto("Broca",556,25.60,122),
    Produto("Furadeira",67,499.90,122)
]

for product in produtos:
    print(product.nomeProduto)

#@app.route('/produto', methods=['GET'])
def get_produtos():

   mycursor = mydb.cursor()
   mycursor.execute('SELECT * FROM Produto')
   meus_produtos = mycursor.fetchall()
   print(meus_produtos)
   
   return make_response(
       jsonify(
           mensagem='Lista de produtos',
           dados=meus_produtos
       )
   )


# Função para buscar um pedido pelo ID
def encontra_produto(idproc):
    for product in produtos:
        if product.idProduto == idproc:
            return product
    return False


# Criar um novo produto

def criar():
    data = request.json
    mycursor = mydb.cursor()
    sql = f"insert into produto(nomeProduto, id, preco, qtd) values  ('{data['nome']}',{data['id']},{data['preco']},{data['qtd']});"
    #sql = f"insert into produto(nomeProduto, id, preco, qtd) values  ('{a}',{b},{c},{d});"
    mycursor.execute(sql)
    mydb.commit()
    return make_response(
       jsonify(
           mensagem='Feito com sucesso',
       )
   )

# Descrescer quantidade
#@app.route('/produtos', methods=['POST'])
def retirar():
    data = request.json
    qtd = data['qtd']
    id = data['id']
    prod=encontra_produto(id)
    if( prod == False):
        return jsonify({'message': 'Produto não encontrado.'}), 404
    else:
        if(prod.preco < qtd):
            return jsonify({'message': 'Quantidade não suficiente.'}), 404
        else:
            prod = prod.preco - qtd
            return make_response


# Atualizar um produto existente
#@app.route('/produtos/<int:idproduto>', methods=['PUT'])
def atualizar(id):
    product = encontra_produto(id)
    if product:
        data = request.json
        nomeProduto = data['nome']
        pid = data['id']
        preco = data['preco']
        qtdI=data['qtdI']
        product(nomeProduto,pid,preco,qtdI)
        return make_response
    else:
        return jsonify({'message': 'Pedido não encontrado.'}), 404


# Deletar um pedido existente
#@app.route('/produtos/<int:idproduto>', methods=['DELETE'])
def deletar(idprod):
    product = encontra_produto(idprod)
    if product:
        produtos.remove(product)
        return jsonify({'message': 'Produto deletado com sucesso!'})
    else:
        return jsonify({'message': 'Produto não encontrado.'}), 404



#teste2
for product in produtos:
    print(product.nomeProduto)