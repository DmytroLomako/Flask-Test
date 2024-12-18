from project.settings import database
from flask_login import UserMixin

class User(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key = True)
    name = database.Column(database.String(50))
    password = database.Column(database.String(50))
    def __repr__(self):
        return f'User: {self.name}'
    