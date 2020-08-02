from project import db


class Product(db.Model):

    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('store.categories.id'), nullable=False)

    def __init__(self, name, price, category_id):
        self.name = name
        self.price = price
        self.category_id = category_id

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'category_id': self.category_id
        }
