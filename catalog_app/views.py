import flask, os
from .models import Product
from project.settings import database

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
    return flask.render_template('catalog_app/catalog.html', products = list_products)

def render_product():
    return flask.render_template('catalog_app/product.html')