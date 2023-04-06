from flask import Flask
import produto
from flask import request

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return " Teste "

@app.route('/produts', methods=['POST'])
def produtCriar():
    return produto.criar()
   
@app.route('/produt')
def produtget():
    return produto.get_produtos()
 

if __name__ == '__main__':
    app.run(debug=True)