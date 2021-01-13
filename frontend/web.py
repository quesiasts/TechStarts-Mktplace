from flask import Flask, render_template, request, redirect
import sys
sys.path.append('.')
from backend.controller.produto_controller import *
from backend.controller.categoria_controller import *
from backend.controller.marketplace_controller import *
from backend.controller.seller_controller import *
from backend.controller.log_controller import *


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/marketplaces')
def marketplaces():
    return render_template('marketplace.html', marketplaces=listar_marketplaces())


@app.route('/categorias')
def categorias():
    return render_template('categorias.html', categorias=listar_categorias())


@app.route('/produtos')
def produtos():
    return render_template('produtos.html', produtos=listar_produtos())


@app.route('/sellers')
def sellers():
    return render_template('sellers.html', sellers=listar_sellers())


@app.route('/adicionar_produtos')
def add_produtos():
    nome = request.args.get('nome')
    descricao = request.args.get('descricao')
    preco = request.args.get('preco')
    criar_produtos(nome, descricao, preco)
    return render_template('retorno_produtos.html', mensagem=f'Produto {nome} cadastrado com sucesso!')


@app.route('/adicionar_marketplaces')
def add_marketplaces():
    nome = request.args.get('nome')
    descricao = request.args.get('descricao')
    criar_marketplaces(nome, descricao)
    return render_template('retorno_marketplaces.html', mensagem=f'Marketplace {nome} cadastrado com sucesso!')


@app.route('/adicionar_categorias')
def add_categorias():
    nome = request.args.get('nome')
    descricao = request.args.get('descricao')
    criar_categorias(nome, descricao)
    return render_template('retorno_categorias.html', mensagem=f'Categoria {nome} cadastrado com sucesso!')

  
@app.route('/adicionar_sellers')
def add_seller():
    nome = request.args.get('nome')
    telefone = request.args.get('telefone')
    email = request.args.get('email')
    criar_sellers(nome, email, telefone)
    return render_template('retorno_sellers.html', mensagem=f'Seller {nome} cadastrado com sucesso!')


@app.route('/listarsellers')
def listar_seller():
    return render_template('listagem_sellers.html', sellers=listar_sellers())


@app.route('/listarprodutos')
def listar_produto():
    return render_template('listar_produtos.html', produtos=listar_produtos())


@app.route('/listagem_marketplaces')
def list_marketplace():
    return render_template('listagem_marketplaces.html', lista_marketplaces = listar_marketplaces())


@app.route('/listagem_categorias')
def list_categoria():
    return render_template('listagem_categorias.html', lista_categorias = listar_categorias())


@app.route('/listagem_logs')
def list_log():
    return render_template('listagem_logs.html', lista_logs = listar_logs())


app.run(debug=True)
