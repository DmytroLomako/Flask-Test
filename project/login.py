import flask_login
from .settings import project_shop
from reg_app.models import User


project_shop.secret_key = 'key'
login_manager = flask_login.LoginManager(project_shop)
@login_manager.user_loader
def load_user(id):
    return User.query.get(id)