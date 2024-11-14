import flask, reg_app

def render_home():
    if flask.request.method == 'POST':
        email = flask.request.form['email']
        message = flask.request.form['message']
        print(email, message)
    return flask.render_template('home_app/home.html', list = reg_app.list_users)