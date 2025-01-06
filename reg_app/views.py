import flask, flask_login
from .models import User
from project.settings import database
from flask_login import current_user

def render_reg():
    if flask_login.current_user.is_authenticated:
        return flask.redirect('/')
    if flask.request.method == 'POST':
        name = flask.request.form['name']
        password = flask.request.form['password']
        user = User(name = name, password = password)
        database.session.add(user)
        database.session.commit()
        return flask.redirect('/auth/')
    return flask.render_template('reg_app/reg.html', title = 'Registration', account = current_user.is_authenticated)

def render_log():
    if flask_login.current_user.is_authenticated:
        return flask.redirect('/')
    if flask.request.method == 'POST':
        name = flask.request.form['name']
        password = flask.request.form['password']
        user = User.query.filter_by(name = name, password = password).first()
        if user:
            flask_login.login_user(user)
            return flask.redirect('/')
        else:
            return 'Неверные данные'
    return flask.render_template('reg_app/reg.html', title = 'Authorization', account = current_user.is_authenticated)

def render_logout():
    flask_login.logout_user()
    return flask.redirect('/')

def render_user():
    if flask.request.method == 'POST':
        user = User.query.get(current_user.id)
        flask_login.logout_user()
        database.session.delete(user)
        database.session.commit()
    if current_user.is_authenticated:
        return flask.render_template('reg_app/user.html', user = current_user, account = current_user.is_authenticated, username = current_user.name)
    return flask.redirect('/')