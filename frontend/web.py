from flask import Flask, render_template, request, redirect

from backend.controller.base_controller import *
from backend.controller.produto_controller import *
from backend.controller.categoria_controller import *
from backend.controller.marketplace_controller import *
from backend.controller.seller_controller import *
from backend.controller.log_controller import *
from backend.models.categoria import *
from backend.models.marketplace import *
from backend.models.produto import *
from backend.models.seller import *

category_controller = CategoryController('Categoria')
marketplace_controller = MarketplaceController('Marketplace')
product_controller = ProductController('Produto')
seller_controller = SellerController('Seller')
log_controller = LogController()

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/marketplaces')
def marketplaces():
    return render_template('marketplaces.html')


@app.route('/categorias')
def categorias():
    return render_template('categorias.html')


@app.route('/produtos')
def produtos():
    return render_template('produtos.html')


@app.route('/sellers')
def sellers():
    return render_template('sellers.html')



#PRODUTO
@app.route('/adicionar_produtos')
def add_produtos():
    name = request.args.get('name')
    description = request.args.get('description')
    price = request.args.get('price')
    product = Product(name, description, price)
    product_controller.create(product)
    return render_template('retorno_produtos.html', mensagem=f'Produto {product.name} cadastrado com sucesso!')

@app.route('/produto/update')
def edit_produto():
    id = request.args.get('id')
    product = product_controller.read_by_id(id) 
    return render_template('produtos.html', product = product, edit = True)


@app.route('/produto/update', methods=['POST'])
def save_produto():
    id = request.form.get('id')
    name = request.form.get('name')    
    description = request.form.get('description')
    price = request.form.get('price')
    product = Product(name, description, price, id)
    product_controller.update(product)      
    return redirect('/listar_produtos')

@app.route('/produto/delete', methods=['POST'])
def delete_produto_web():
    id = request.form.get('id')
    product_controller.delete(id) 
    return redirect('/listar_produtos')


#MARKETPLACES
@app.route('/adicionar_marketplaces')
def add_marketplaces():
    name = request.args.get('name')
    description = request.args.get('description')
    marketplace = Marketplace(name, description)
    marketplace_controller.create(marketplace)
    return render_template('retorno_marketplaces.html', mensagem=f'Marketplace {marketplace.name} cadastrado com sucesso!')

@app.route('/marketplace/update')
def edit_marketplace():
    id = request.args.get('id')
    marketplace = marketplace_controller.read_by_id(id) 
    return render_template('marketplaces.html', marketplace = marketplace, edit = True)

@app.route('/marketplace/update', methods=['POST'])
def save_marketplace():
    id = request.form.get('id')
    name = request.form.get('name')
    description = request.form.get('description')
    marketplace = Marketplace(name, description, id)
    marketplace_controller.update(marketplace)      
    return redirect('/listagem_marketplaces')



@app.route('/marketplace/delete', methods=['POST'])
def delete_marketplace_web():
    id = request.form.get('id')
    marketplace_controller.delete(id) 
    return redirect('/listagem_marketplaces')



#CATEGORIA
@app.route('/adicionar_categorias')
def add_categorias():
    name = request.args.get('nome')
    description = request.args.get('descricao')
    category = Category(name, description)
    category_controller.create(category)
    return render_template('retorno_categorias.html', mensagem=f'Categoria {category.name} cadastrado com sucesso!')

@app.route('/categoria/update')
def edit_categoria():
    id = request.args.get('id')
    category = category_controller.read_by_id(id) 
    return render_template('categorias.html', category = category, edit = True)


@app.route('/categoria/update', methods=['POST'])
def save_categoria():
    id = request.form.get('id')
    name = request.form.get('name')
    description = request.form.get('description')
    category = Category(name, description, id)
    category_controller.update(category)      
    return redirect('/listagem_categorias')

@app.route('/categoria/delete', methods=['POST'])
def delete_categoria_web():
    id = request.form.get('id')
    category_controller.delete(id) 
    return redirect('/listagem_categorias')


#SELLERS
@app.route('/adicionar_sellers')
def add_seller():
    name = request.args.get('name')
    phone = request.args.get('email')
    email = request.args.get('phone')
    seller = Seller(name, email, phone)
    seller_controller.create(seller)
    return render_template('retorno_sellers.html', mensagem=f'Seller {seller.name} cadastrado com sucesso!')

@app.route('/seller/update')
def edit_seller():
    id = request.args.get('id')
    seller = seller_controller.read_by_id(id) 
    return render_template('sellers.html', seller = seller, edit = True)


@app.route('/seller/update', methods=['POST'])
def save_seller():
    id = request.form.get('id')
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    seller = Seller(name, email, phone, id)
    seller_controller.update(seller)      
    return redirect('/listar_sellers')

@app.route('/seller/delete', methods=['POST'])
def delete_seller_web():
    id = request.form.get('id')
    seller_controller.delete(id) 
    return redirect('/listar_sellers')


@app.route('/listar_sellers')
def listar_seller():
    listaSeller = seller_controller.read_all()
    print(listaSeller[0].name)
    return render_template('listagem_sellers.html', sellers=listaSeller)


@app.route('/listar_produtos')
def listar_produto():
    return render_template('listar_produtos.html', produtos=product_controller.read_all())


@app.route('/listagem_marketplaces')
def list_marketplace():
    return render_template('listagem_marketplaces.html', lista_marketplaces = marketplace_controller.read_all())


@app.route('/listagem_categorias')
def list_categoria():
    return render_template('listagem_categorias.html', lista_categorias = category_controller.read_all())


@app.route('/listagem_logs')
def list_log():
    return render_template('listagem_logs.html', lista_logs = log_controller.read_all())


app.run(debug=True)
