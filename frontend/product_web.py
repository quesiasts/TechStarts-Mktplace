from flask import render_template, request, redirect, Blueprint

from backend.controller.produto_controller import ProductController
from backend.models.produto import Product

CONTROLLER = ProductController()

product_bp = Blueprint('product', __name__)


@product_bp.route('/produtos')
def produtos():
    return render_template('produtos.html')


@product_bp.route('/listar_produtos')
def listar_produto():
    return render_template('listar_produtos.html', produtos=CONTROLLER.read_all())


@product_bp.route('/adicionar_produtos')
def add_produtos():
    name = request.args.get('name')
    description = request.args.get('description')
    price = request.args.get('price')
    product = Product(name, description, price)
    CONTROLLER.create(product)
    return render_template('retorno_produtos.html', mensagem=f'Produto {name} cadastrado com sucesso!')


@product_bp.route('/produto/update')
def edit_produto():
    id = request.args.get('id')
    product = CONTROLLER.read_by_id(id)
    return render_template('produtos.html', product=product, edit=True)


@product_bp.route('/produto/update', methods=['POST'])
def save_produto():
    id = request.form.get('id')
    product = CONTROLLER.read_by_id(id)

    product.name = request.form.get('name')
    product.description = request.form.get('description')
    product.price = request.form.get('price')

    CONTROLLER.update(product)
    return redirect('/listar_produtos')


@product_bp.route('/produto/delete', methods=['POST'])
def delete_produto_web():
    id = request.form.get('id')
    CONTROLLER.delete(id)
    return redirect('/listar_produtos')
