import os

from flask import Blueprint, jsonify, request

from project.models.category import Category
from project import db


categories_blueprint = Blueprint('categories', __name__)


@categories_blueprint.route('/categories', methods=['GET', 'POST'])
def all_categories():
    if request.method == 'POST':
        post_data = request.get_json()
        name = post_data.get('name')
        db.session.add(Category(name=name))
        db.session.commit()
    else:
        response_object['categories'] = [category.to_json() for category in Category.query.all()]
    return js


@categories_blueprint.route('/categories/ping', methods=['GET'])
def ping():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })


@categories_blueprint.route('/categories/<category_id>', methods=['PUT', 'DELETE'])
def single_category(category_id):
    category = Category.query.filter_by(id=category_id).first()
    if request.method == 'PUT':
        post_data = request.get_json()
        category.name = post_data.get('name')
        db.session.commit()
    if request.method == 'DELETE':
        db.session.delete(category)
        db.session.commit()
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()
