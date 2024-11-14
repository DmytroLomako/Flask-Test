import flask

reg_app = flask.Blueprint(
    name = 'reg_app',
    import_name = 'reg_app',
    template_folder = 'templates',
    static_folder ='static',
    static_url_path = '/reg/'
)