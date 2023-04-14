from flask import Flask, jsonify, request
from flask import Flask, jsonify, request,  jsonify, make_response
from typing import List
import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='quickstore',
)

app = Flask(name)

users = [
    {
        "id": 1,
        "name": "João da Silva",
        "cargo": "Vendedor",
        "senha": "123456"
    },
    {
        "id": 2,
        "name": "Maria Souza",
        "cargo": "Marketing",
        "senha": "abcdef"
    }
]

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = [user for user in users if user['id'] == user_id]
    return jsonify(user)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    mycursor = mydb.cursor()
    sql = f"insert into user(id, nome, cargo, senha) values  ('{data['id']}',{data['nome']},{data['cargo']},{data['senha']});"
    mycursor.execute(sql)
    mydb.commit()
    return make_response(
       jsonify(
           mensagem='Usuario criado com sucesso',
       )
   )

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    user_id = data['id']
    nome = data['nome']
    cargo = data['cargo']
    senha = data['senha']
    mycursor1 = mydb.cursor()
    sql1 = f"UPDATE usuário SET nome, cargo, senha, id = ('{data['nome']}',{data['cargo']},{data['senha']})  WHERE id = ('{data['id']}');"
    mycursor1.execute(sql1)
    mydb.commit()
    return make_response
    #user = [user for user in users if user['id'] == user_id]
    #user[0]['nome'] = request.json.get('nome', user[0]['nome'])
    #user[0]['cargo'] = request.json.get('cargo', user[0]['cargo'])
    #user[0]['senha'] = request.json.get('senha', user[0]['senha'])
    #return jsonify(user[0])

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    data = request.json
    user_id = data['id']
    mycursor = mydb.cursor()
    sql = f"DELETE FROM produto WHERE id = ('{data['id']}')"
    mycursor.execute(sql)
    mydb.commit()
    return make_response()

if name == 'main':
    app.run(debug=True)