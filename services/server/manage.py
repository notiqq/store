from flask.cli import FlaskGroup

from project import create_app, db
from project.api.models import Product


app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command('seed_db')
def seed_db():
    """Seeds the database."""
    db.session.add(Product(
        name='iPhone 11',
        price=20,
        category_id=1
    ))
    db.session.add(Product(
        name='iPhone 10',
        price=17,
        category_id=1
    ))
    db.session.add(Product(
        name='iPhone 9',
        price=16,
        category_id=1
    ))
    db.session.commit()


if __name__ == '__main__':
    cli()
