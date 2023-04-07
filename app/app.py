from flask import Flask
import produto
from flask import request

app = Flask(__name__)

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
   
@app.route('/produt')
def produtget():
    return produto.get_produtos()
 

if __name__ == '__main__':
    app.run(debug=True)