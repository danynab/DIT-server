__author__ = 'Dani'

from application import db


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    color = db.Column(db.String(7))

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def to_dict(self):
        _dict = {'id': self.id,
                 'name': self.name,
                 'color': self.color}
        return {k: v for k, v in _dict.items() if v}
