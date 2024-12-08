import flask
from .models import User
from project.settings import database

def render_reg():
    if flask.request.method == 'POST':
        name = flask.request.form['name']
        password = flask.request.form['password']
        user = User(name = name, password = password)
        database.session.add(user)
        database.session.commit()
        return flask.redirect('/')
    return flask.render_template('reg_app/reg.html')