import flask, json, os

def render_catalog():
    path_to_json = os.path.abspath(__file__ + '/../products.json')
    with open(path_to_json, 'r') as file:
        data = json.load(file)
        print(data.values())
    return flask.render_template('catalog_app/catalog.html', products = data.values())

def render_product():
    return flask.render_template('catalog_app/product.html')