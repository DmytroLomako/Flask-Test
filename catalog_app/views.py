import flask, os
from .models import Product, Review
from project.settings import database
from flask_login import current_user
from home_app.views import get_user

def render_catalog():
    list_products = Product.query.all()
    return flask.render_template('catalog_app/catalog.html', products = list_products, account = current_user.is_authenticated, username = get_user(current_user), user=current_user)

def render_product(product_id):
    print(product_id)
    product = Product.query.get(product_id)
    print(get_user(current_user))
    if flask.request.method == 'POST':
        text = flask.request.form['review']
        rating = flask.request.form['rating']
        review = Review(text = text,raiting = rating, product_id = product_id)
        if current_user.is_authenticated:
            review.user_id = current_user.id
        database.session.add(review)
        database.session.commit()
    return flask.render_template('catalog_app/product.html', account = current_user.is_authenticated, product = product, username = get_user(current_user), user=current_user)