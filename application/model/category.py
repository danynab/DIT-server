from application import db

__author__ = 'Dani Meana'


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String)
    color = db.Column(db.String)

    def __init__(self, id_category, name=None, color='#000000', image=None):
        self.id = id_category
        self.name = name
        self.color = color
        self.image = image

    def to_dict(self):
        _dict = {'id': self.id,
                 'name': self.name,
                 'color': self.color,
                 'image': self.image}
        return {k: v for k, v in _dict.items() if v}