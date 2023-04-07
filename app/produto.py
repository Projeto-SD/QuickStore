
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
    mycursor = mydb.cursor()
    sql = f"SELECT qtd FROM produtos WHERE id =('{data['id']}');"
    mycursor.execute(sql)
    qtdAtual = mycursor.fetchall()

    if(qtdAtual < qtd):
            return jsonify({'message': 'Quantidade não suficiente.'}), 404
    else:
            qtdfinal=qtdAtual-qtd
            mycursor1 = mydb.cursor()
            sql1 = f"UPDATE produtos SET qtd = ('{qtdfinal}') WHERE id = ('{data['id']}');"
            mycursor1.execute(sql1)
            mydb.commit()
            return make_response


# Atualizar um produto existente
def atualizar(id):
    product = encontra_produto(id)
    if product:
        data = request.json
        nomeProduto = data['nome']
        id = data['id']
        preco = data['preco']
        qtdI=data['qtdI']
        mycursor1 = mydb.cursor()
        sql1 = f"UPDATE produtos SET nome,preco,id,qtdI = ('{data['nome']}',{data['id']},{data['preco']},{data['qtd']})  WHERE id = ('{data['id']}');"
        mycursor1.execute(sql1)
        mydb.commit()
        
        return make_response
    else:
        return jsonify({'message': 'Pedido não encontrado.'}), 404


# Deletar um pedido existente
def deletar(idprod):
  
   mycursor = mydb.cursor()
   mycursor.execute('DELETE FROM clientes WHERE id = ('{data['id']}');')
   meus_produtos = mycursor.fetchall()
   
   return make_response(
       jsonify(
           mensagem='Lista de produtos',
           dados=meus_produtos
       )
   )

  



#teste2
for product in produtos:
    print(product.nomeProduto)