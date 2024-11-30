from project.settings import database

class User(database.Model):
    id = database.Column(database.Integer, primary_key = True)
    name = database.Column(database.String(50))
    password = database.Column(database.String(50))
    def __repr__(self):
        return f'User: {self.name}'
    