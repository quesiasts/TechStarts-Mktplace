from flask import render_template, request, redirect, Blueprint

from backend.controller.seller_controller import SellerController
from backend.models.seller import Seller

CONTROLLER = SellerController()

seller_bp = Blueprint('seller', __name__)


@seller_bp.route('/sellers')
def sellers():
    return render_template('sellers.html')


@seller_bp.route('/adicionar_sellers')
def add_seller():
    name = request.args.get('name')
    phone = request.args.get('email')
    email = request.args.get('phone')
    seller = Seller(name, email, phone)
    CONTROLLER.create(seller)
    return render_template('retorno_sellers.html', mensagem=f'Seller {name} cadastrado com sucesso!')


@seller_bp.route('/seller/update')
def edit_seller():
    id = request.args.get('id')
    seller = CONTROLLER.read_by_id(id)
    return render_template('sellers.html', seller=seller, edit=True)


@seller_bp.route('/seller/update', methods=['POST'])
def save_seller():
    id = request.form.get('id')
    seller = CONTROLLER.read_by_id(id)

    seller.name = request.form.get('name')
    seller.email = request.form.get('email')
    seller.phone = request.form.get('phone')

    CONTROLLER.update(seller)
    return redirect('/listar_sellers')


@seller_bp.route('/seller/delete', methods=['POST'])
def delete_seller_web():
    id = request.form.get('id')
    CONTROLLER.delete(id)
    return redirect('/listar_sellers')


@seller_bp.route('/listar_sellers')
def listar_seller():
    sellers = CONTROLLER.read_all()
    return render_template('listagem_sellers.html', sellers=sellers)
