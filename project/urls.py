import home_app, reg_app, catalog_app

home_app.home_app.add_url_rule('/', view_func = home_app.render_home, methods = ['GET', 'POST'])
reg_app.reg_app.add_url_rule('/reg/', view_func = reg_app.render_reg, methods = ['GET', 'POST'])
catalog_app.catalog_app.add_url_rule('/catalog/', view_func = catalog_app.render_catalog, methods = ['GET', 'POST'])