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
