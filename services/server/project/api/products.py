import os

from flask import Blueprint, jsonify, request

from project.models.product import Product
from project import db


products_blueprint = Blueprint('products', __name__)


@products_blueprint.route('/products', methods=['GET', 'POST'])
def all_products():
    if request.method == 'POST':
        post_data = request.get_json()
        name = post_data.get('name')
        price = post_data.get('price')
        category_id = post_data.get('category_id')
        db.session.add(Product(name=name, price=price, category_id=category_id))
        db.session.commit()
    else:
        response_object['products'] = [product.to_json() for product in Product.query.all()]
    return jsonify(response_object)


@products_blueprint.route('/products/ping', methods=['GET'])
def ping():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })


@products_blueprint.route('/products/<product_id>', methods=['PUT', 'DELETE'])
def single_product(product_id):
    product = Product.query.filter_by(id=product_id).first()
    if request.method == 'PUT':
        post_data = request.get_json()
        product.name = post_data.get('name')
        product.price = post_data.get('price')
        product.category_id = post_data.get('category_id')
        db.session.commit()
    if request.method == 'DELETE':
        db.session.delete(product)
        db.session.commit()
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()
