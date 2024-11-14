import flask

list_users = []
def render_reg():
    if flask.request.method == 'POST':
        name = flask.request.form['name']
        password = flask.request.form['password']
        print(name, password)
        dict_user = {
            'name': name,
            'password': password
        }
        list_users.append(dict_user)
        print(list_users)
        return flask.redirect('/')
    return flask.render_template('reg_app/reg.html')