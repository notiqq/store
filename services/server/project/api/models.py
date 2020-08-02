import datetime

from flask import current_app
from sqlalchemy.sql import func

from project import db


class Category(db.Model):

    __tablename__ = 'categories'
    __table_args__ = {"schema": "store"}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)

    def __init__(self, name):
        self.name = name

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Product(db.Model):

    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('store.categories.id'), nullable=False)

    def __init__(self, name, price, category_id):
        self.name = title
        self.price = price
        self.category_id = category_id

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'price': self.price,
            'category_id': self.category_id
        }
