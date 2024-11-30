import flask, home_app, reg_app, catalog_app, os
import flask_migrate, flask_sqlalchemy

project_shop = flask.Flask(
    import_name = 'shop',
    template_folder = 'templates',
    instance_path = os.path.abspath(__file__ + '/../../instance')
)



project_shop.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
database = flask_sqlalchemy.SQLAlchemy(project_shop)
migrations = flask_migrate.Migrate(project_shop, database)