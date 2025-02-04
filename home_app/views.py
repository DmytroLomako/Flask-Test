import flask
from  reg_app.models import User
from project.settings import database
from flask_login import current_user

def get_user(current_user):
    name = 'Anonymous'
    if current_user.is_authenticated:
        name = current_user.name
    return name
def render_home():
    if flask.request.method == 'POST':
        email = flask.request.form['email']
        message = flask.request.form['message']
    list_users = User.query.all()
    return flask.render_template('home_app/home.html', list = list_users, username = get_user(current_user), account = current_user.is_authenticated, user=current_user)