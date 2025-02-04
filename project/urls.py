import home_app, reg_app, catalog_app, cart_app, admin_app
from project.settings import project_shop

home_app.home_app.add_url_rule('/', view_func = home_app.render_home, methods = ['GET', 'POST'])
reg_app.reg_app.add_url_rule('/reg/', view_func = reg_app.render_reg, methods = ['GET', 'POST'])
reg_app.reg_app.add_url_rule('/auth/', view_func = reg_app.render_log, methods = ['GET', 'POST'])
reg_app.reg_app.add_url_rule('/logout/', view_func = reg_app.render_logout, methods = ['GET', 'POST'])
reg_app.reg_app.add_url_rule('/user/', view_func = reg_app.render_user, methods = ['GET', 'POST'])
catalog_app.catalog_app.add_url_rule('/catalog/', view_func = catalog_app.render_catalog, methods = ['GET', 'POST'])
catalog_app.catalog_app.add_url_rule('/product/<int:product_id>', view_func = catalog_app.render_product, methods = ['GET', 'POST'])
cart_app.cart_app.add_url_rule('/cart/', view_func = cart_app.render_cart, methods = ['GET', 'POST'])
admin_app.admin_app.add_url_rule('/admin/', view_func = admin_app.render_admin, methods = ['GET', 'POST'])

project_shop.register_blueprint(home_app.home_app)
project_shop.register_blueprint(reg_app.reg_app)
project_shop.register_blueprint(catalog_app.catalog_app)
project_shop.register_blueprint(cart_app.cart_app)
project_shop.register_blueprint(admin_app.admin_app)