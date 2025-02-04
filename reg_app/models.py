from project.settings import database
from flask_login import UserMixin

class User(database.Model, UserMixin):
    __tablename__ = 'user'
    id = database.Column(database.Integer, primary_key = True)
    name = database.Column(database.String(50))
    password = database.Column(database.String(50))
    is_admin = database.Column(database.Boolean, default = False)
    reviews = database.relationship('Review', backref = 'user')
    def __repr__(self):
        return f'User: {self.name}'