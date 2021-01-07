from flask import Flask, render_template, request
import sys
sys.path.append('.')
from backend.main import *

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/marketplaces')
def marketplaces():
    return render_template('marketplace.html', marketplaces=get_marketplaces())

@app.route('/categorias')
def categorias():
    return render_template('categorias.html', categorias=get_categorias())

@app.route('/produtos')
def produtos():
    return render_template('produtos.html', produtos=get_produtos())


@app.route('/sellers')
def sellers():
    return render_template('sellers.html', sellers=get_seller())


@app.route('/adicionar_produtos')
def add_produtos():
    return render_template('adicionar_produtos.html', mensagem=set_produtos(request.args.get('nome'), request.args.get('descricao'), request.args.get('preco')))

  
@app.route('/adicionar_marketplaces')
def add_marketplaces():
    return render_template('adicionar_marketplaces.html', mensagem=set_marketplaces(request.args.get('nome'), request.args.get('descricao')))

  
@app.route('/adicionar_categorias')
def add_categorias():
    return render_template('adicionar_categorias.html', mensagem=set_categorias(request.args.get('nome'), request.args.get('descricao')))

  
@app.route('/adicionar_sellers')
def add_seller():
    return render_template('adicionar_sellers.html', mensagem=set_seller(request.args.get('nome'),
                                                                         request.args.get('sobrenome'), request.args.get('telefone'), request.args.get('email')))


@app.route('/listarsellers')
def listar_sellers():
    return render_template('listagem_sellers.html', sellers=get_seller())


@app.route('/listarprodutos')
def listar_produtos():
    return render_template('listar_produtos.html', produtos=get_produtos())


@app.route('/listagem_marketplaces')
def list_marketplaces():
    return render_template('listagem_marketplaces.html', lista_marketplaces = get_marketplaces())


@app.route('/listagem_categorias')
def list_categorias():
    return render_template('listagem_categorias.html', lista_categorias = get_categorias())


app.run(debug=True)
