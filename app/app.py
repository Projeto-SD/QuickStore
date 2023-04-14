from flask import Flask
import produto
from flask import request,jsonify
#from flask_cors import CORS

app = Flask(__name__)
#CORS(app)


@app.route('/')
@app.route('/index')
def index():
    return " Teste "

@app.route('/delproduto', methods=['POST'])
def produtDel():
    return produto.deletar()


@app.route('/attproduto', methods=['POST'])
def produtAtualizar():
    return produto.atualizar()

@app.route('/retproduto', methods=['POST'])
def produtRetirar():
    return produto.retirar()


@app.route('/produts', methods=['POST'])
def produtCriar():
    return produto.criar()
   
@app.route('/produt', methods=['GET'])
def produtget():
    return produto.get_produtos()
 

if __name__ == '__main__':
    app.run(debug=True)