import flask, os
from .models import Product, Review
from project.settings import database
from flask_login import current_user
from home_app.views import get_user

def render_catalog():
    if flask.request.method == 'POST':
        if 'id-product' in flask.request.form:
            product_id = flask.request.form['id-product']
            product = Product.query.get(product_id)
            path_to_delete = os.path.abspath(__file__ + f'/../static/catalog_app/img/products/{product.image}.png')
            os.remove(path_to_delete)
            database.session.delete(product)
            database.session.commit()
        else:
            name = flask.request.form['name']
            price = flask.request.form['price']
            description = flask.request.form['description']
            product = Product(name = name, price = price, description = description)
            database.session.add(product)
            database.session.commit()
            product.image = f'{name}-{product.id}'
            database.session.commit()
            image = flask.request.files['image']
            image_path = os.path.abspath(__file__ + f'/../static/catalog_app/img/products/{product.image}.png')
            image.save(image_path)
    list_products = Product.query.all()
    return flask.render_template('catalog_app/catalog.html', products = list_products, account = current_user.is_authenticated, username = get_user(current_user))

def render_product(product_id):
    print(product_id)
    product = Product.query.get(product_id)
    print(get_user(current_user))
    if flask.request.method == 'POST':
        text = flask.request.form['review']
        rating = flask.request.form['rating']
        review = Review(text = text,raiting = rating, product_id = product_id)
        database.session.add(review)
        database.session.commit()
    return flask.render_template('catalog_app/product.html', account = current_user.is_authenticated, product = product, username = get_user(current_user))