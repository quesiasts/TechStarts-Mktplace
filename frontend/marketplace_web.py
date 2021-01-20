from flask import render_template, request, redirect, Blueprint

from backend.controller.marketplace_controller import MarketplaceController
from backend.models.marketplace import Marketplace

CONTROLLER = MarketplaceController()

marketplace_bp = Blueprint('marketplace', __name__)


@marketplace_bp.route('/marketplaces')
def marketplaces():
    return render_template('marketplaces.html')


@marketplace_bp.route('/listagem_marketplaces')
def list_marketplace():
    return render_template('listagem_marketplaces.html', lista_marketplaces=CONTROLLER.read_all())


@marketplace_bp.route('/adicionar_marketplaces')
def add_marketplaces():
    name = request.args.get('name')
    description = request.args.get('description')
    marketplace = Marketplace(name, description)
    CONTROLLER.create(marketplace)
    return render_template('retorno_marketplaces.html',
                           mensagem=f'Marketplace {name} cadastrado com sucesso!')


@marketplace_bp.route('/marketplace/update')
def edit_marketplace():
    id = request.args.get('id')
    marketplace = CONTROLLER.read_by_id(id)
    return render_template('marketplaces.html', marketplace=marketplace, edit=True)


@marketplace_bp.route('/marketplace/update', methods=['POST'])
def save_marketplace():
    id = request.form.get('id')
    marketplace = CONTROLLER.read_by_id(id)

    marketplace.name = request.form.get('name')
    marketplace.description = request.form.get('description')

    CONTROLLER.update(marketplace)
    return redirect('/listagem_marketplaces')


@marketplace_bp.route('/marketplace/delete', methods=['POST'])
def delete_marketplace_web():
    id = request.form.get('id')
    CONTROLLER.delete(id)
    return redirect('/listagem_marketplaces')
