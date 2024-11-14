import flask, reg_app

def render_home():
    return flask.render_template('home_app/home.html', list = reg_app.list_users)