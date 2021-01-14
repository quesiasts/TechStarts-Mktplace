from flask import Flask, render_template, request, redirect
import sys
sys.path.append('.')

from backend.controller.produto_controller import *
from backend.controller.categoria_controller import *
from backend.controller.marketplace_controller import *
from backend.controller.seller_controller import *
from backend.controller.log_controller import *
from backend.models.categoria import *
from backend.models.marketplace import *
from backend.models.produto import *
from backend.models.seller import *



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
    name = request.args.get('nome')
    description = request.args.get('descricao')
    price = request.args.get('preco')
    produto = Produto(None, name, description, price)
    criar_produtos(produto)
    return render_template('retorno_produtos.html', mensagem=f'Produto {produto.name} cadastrado com sucesso!')


@app.route('/adicionar_marketplaces')
def add_marketplaces():
    name = request.args.get('name')
    description = request.args.get('description')
    marketplace = Marketplace(None, name, description)
    criar_marketplaces(marketplace)
    return render_template('retorno_marketplaces.html', mensagem=f'Marketplace {marketplace.name} cadastrado com sucesso!')


@app.route('/adicionar_categorias')
def add_categorias():
    nome = request.args.get('nome')
    descricao = request.args.get('descricao')
    categoria = Categoria(nome, descricao)
    criar_categorias(categoria)
    return render_template('retorno_categorias.html', mensagem=f'Categoria {categoria.name} cadastrado com sucesso!')

@app.route('/categoria/update')
def edit_categoria():
    id = request.args.get('id')
    categoria = edit_category(id) 
    return render_template('categorias.html', categoria = categoria, edit = True)


@app.route('/categoria/update', methods=['POST'])
def save_categoria():
    id = request.form.get('id')
    name = request.form.get('name')
    description = request.form.get('description')
    categoria = Categoria(name, description, id)
    update_categoria(categoria)      
    return redirect('/listagem_categorias')

@app.route('/categoria/delete', methods=['POST'])
def delete_categoria_web():
    id = request.form.get('id')
    delete_categoria(id) 
    return redirect('/listagem_categorias')

  
@app.route('/adicionar_sellers')
def add_seller():
    name = request.args.get('nome')
    phone = request.args.get('telefone')
    email = request.args.get('email')
    seller = Seller(None, name, phone, email)
    criar_sellers(seller)
    return render_template('retorno_sellers.html', mensagem=f'Seller {seller.name} cadastrado com sucesso!')


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
