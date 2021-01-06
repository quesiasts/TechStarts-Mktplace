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
    return render_template('marketplace.html', marketplaces = get_marketplaces())

@app.route('/produtos')
def produtos():
    return render_template('produtos.html', produtos = get_produtos())

@app.route('/adicionar_produtos')
def add_produtos():
    return render_template('adicionar_produtos.html', mensagem = set_produtos(request.args.get('nome'), request.args.get('descricao'),request.args.get('preco')))

@app.route('/adicionar_marketplaces')
def add_marketplaces():
    return render_template('adicionar_marketplaces.html', mensagem = set_marketplaces(request.args.get('nome'), request.args.get('descricao')))

@app.route('/listagem_marketplaces')
def list_marketplaces():
    return render_template('listagem_marketplaces.html', lista_marketplaces = get_marketplaces()) 


app.run(debug=True)