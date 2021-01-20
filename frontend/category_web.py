from flask import render_template, request, redirect, Blueprint

from backend.controller.categoria_controller import CategoryController
from backend.models.categoria import Category

CONTROLLER = CategoryController()

category_bp = Blueprint('category', __name__)


@category_bp.route('/categorias')
def categorias():
    return render_template('categorias.html')


@category_bp.route('/listagem_categorias')
def list_categoria():
    return render_template('listagem_categorias.html', lista_categorias=CONTROLLER.read_all())


@category_bp.route('/adicionar_categorias')
def add_categorias():
    name = request.args.get('nome')
    description = request.args.get('descricao')
    category = Category(name, description)
    CONTROLLER.create(category)
    return render_template('retorno_categorias.html', mensagem=f'Categoria {name} cadastrado com sucesso!')


@category_bp.route('/categoria/update')
def edit_categoria():
    id = request.args.get('id')
    category = CONTROLLER.read_by_id(id)
    return render_template('categorias.html', category=category, edit=True)


@category_bp.route('/categoria/update', methods=['POST'])
def save_categoria():
    id = request.form.get('id')
    category = CONTROLLER.read_by_id(id)

    category.name = request.form.get('name')
    category.description = request.form.get('description')

    CONTROLLER.update(category)
    return redirect('/listagem_categorias')


@category_bp.route('/categoria/delete', methods=['POST'])
def delete_categoria_web():
    id = request.form.get('id')
    CONTROLLER.delete(id)
    return redirect('/listagem_categorias')
