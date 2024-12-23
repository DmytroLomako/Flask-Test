from project.settings import database

class Product(database.Model):
    __tablename__ = 'product'
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String)
    price = database.Column(database.Integer)
    description = database.Column(database.String)
    image = database.Column(database.String)
    reviews = database.relationship('Review', backref = 'product')
    def __repr__(self):
        return self.name
    
class Order(database.Model):
    id = database.Column(database.Integer, primary_key = True)
    user_id = database.Column(database.Integer, database.ForeignKey('user.id'))
    
class Review(database.Model):
    __tablename__ = 'review'
    id = database.Column(database.Integer, primary_key = True)
    text = database.Column(database.String)
    raiting = database.Column(database.Integer)
    user_id = database.Column(database.Integer, database.ForeignKey('user.id', name = 'review_user'))
    product_id = database.Column(database.Integer, database.ForeignKey('product.id'))