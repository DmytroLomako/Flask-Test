import flask
from catalog_app.models import Product
from flask_login import current_user
from home_app.views import get_user

def render_cart():
    list_product_id = []
    products = flask.request.cookies.get('product')
    if products != None:
        list_product_id = products.split(',')
    list_product = []
    for id in list_product_id:
        product = Product.query.get(id)
        if product != None:
            list_product.append(product)
    return flask.render_template('cart.html', list_product = list_product, user=current_user, account=current_user.is_authenticated, username = get_user(current_user))