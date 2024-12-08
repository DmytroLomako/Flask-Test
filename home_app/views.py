import flask
from  reg_app.models import User
from project.settings import database

def render_home():
    if flask.request.method == 'POST':
        email = flask.request.form['email']
        message = flask.request.form['message']
        user_id = flask.request.form['user_id']
        print(user_id)
        if user_id:
            user = User.query.get(user_id)
            # database.session.delete(user)
            user.name = message
            database.session.commit()
    list_users = User.query.all()
    return flask.render_template('home_app/home.html', list = list_users)