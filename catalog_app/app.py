import flask

catalog_app = flask.Blueprint(
    name = 'catalog_app',
    import_name = 'catalog_app',
    template_folder = 'templates',
    static_folder ='static',
    static_url_path = '/catalog/'
)