__author__ = 'Dani Meana'

from application import db


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    image = db.Column(db.String)
    address = db.Column(db.String)
    date = db.Column(db.DateTime)
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)
    user_id = db.Column(db.Integer)
    category_id = db.Column(db.Integer)
    place_id = db.Column(db.Integer)

    def __init__(self, title, description, image, address, date, lat, lng, user_id, category_id, place_id=None):
        self.title = title
        self.description = description
        self.image = image
        self.address = address
        self.date = date
        self.lat = lat
        self.lng = lng
        self.user_id = user_id
        self.category_id = category_id
        self.place_id = place_id

    def to_dict(self):
        _dict = {'id': self.id,
                 'title': self.title,
                 'description': self.description,
                 'image': self.image,
                 'address': self.address,
                 'date': self.date,
                 'lat': self.lat,
                 'lng': self.lng,
                 'userId': self.user_id,
                 'categoryId': self.category_id,
                 'placeId': self.place_id}
        return {k: v for k, v in _dict.items() if v}
