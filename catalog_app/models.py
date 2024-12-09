from project.settings import database

class Product(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String)
    price = database.Column(database.Integer)
    description = database.Column(database.String)
    image = database.Column(database.String)
    def __repr__(self):
        return self.name
    
class Order(database.Model):
    id = database.Column(database.Integer, primary_key = True)
    user_id = database.Column(database.Integer, database.ForeignKey('user.id'))
    def __repr__(self):
        return self.name