import flask
# from .models import Product

def render_catalog():
    if flask.request.method == 'POST':
        name = flask.request.form['name']
        price = flask.request.form['price']
        description = flask.request.form['description']
        print(name, price, description)
    list_products = []#Product.query.all()
    return flask.render_template('catalog_app/catalog.html', products = list_products)

def render_product():
    return flask.render_template('catalog_app/product.html')