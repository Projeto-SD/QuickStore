from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {
        "id": 1,
        "nome": "João da Silva",
        "cargo": "Vendedor",
        "senha": "123456"
    },
    {
        "id": 2,
        "nome": "Maria Souza",
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
    new_user = {
        "id": users[-1]['id'] + 1,
        "nome": request.json['nome'],
        "cargo": request.json['cargo'],
        "senha": request.json['senha']
    }
    users.append(new_user)
    return jsonify(new_user)({"message": "Usuario criado!"})

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = [user for user in users if user['id'] == user_id]
    user[0]['nome'] = request.json.get('nome', user[0]['nome'])
    user[0]['cargo'] = request.json.get('cargo', user[0]['cargo'])
    user[0]['senha'] = request.json.get('senha', user[0]['senha'])
    return jsonify(user[0])

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = [user for user in users if user['id'] == user_id]
    users.remove(user[0])
    return jsonify({"message": "Usuario deletado."})

if __name__ == '__main__':
    app.run(debug=True)