import flask, os
from flask_login import current_user
from home_app.views import get_user
from project.settings import database
from catalog_app.models import Product

def render_admin():
    if current_user.is_authenticated:
        if current_user.is_admin:
            if flask.request.method == 'POST':
                if 'id-product' in flask.request.form:
                    product_id = flask.request.form['id-product']
                    product = Product.query.get(product_id)
                    try:
                        path_to_delete = os.path.abspath(__file__ + f'/../../catalog_app/static/catalog_app/img/products/{product.image}.png')
                        os.remove(path_to_delete)
                    except:
                        print(f'image {product.image} not found')
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
                    image_path = os.path.abspath(__file__ + f'/../../catalog_app/static/catalog_app/img/products/{product.image}.png')
                    image.save(image_path)
            products = Product.query.all()
            return flask.render_template('admin.html', user=current_user, account = current_user.is_authenticated, username = get_user(current_user), products=products)
    return flask.abort(404)