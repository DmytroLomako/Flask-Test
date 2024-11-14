import flask, home_app, reg_app, catalog_app

project_shop = flask.Flask(
    import_name = 'shop',
    template_folder = 'templates'
)

project_shop.register_blueprint(home_app.home_app)
project_shop.register_blueprint(reg_app.reg_app)
project_shop.register_blueprint(catalog_app.catalog_app)