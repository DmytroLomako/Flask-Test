import flask

cart_app = flask.Blueprint(
    name = 'cart_app',
    import_name = 'cart_app',
    template_folder = 'templates',
    static_folder ='static',
    static_url_path = '/cart/'
)