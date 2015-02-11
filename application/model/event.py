from application.services.category_service import CategoryService
from application import db

__author__ = 'Dani Meana'


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    address = db.Column(db.String)
    time = db.Column(db.BigInteger)
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)
    user_id = db.Column(db.String)
    profile_image = db.Column(db.String)
    category_id = db.Column(db.Integer)
    place_id = db.Column(db.Integer)

    def __init__(self, title, description, address, time, lat, lng, user_id, profile_image, category_id,
                 place_id=None):
        self.title = title
        self.description = description
        self.address = address
        self.time = time
        self.lat = lat
        self.lng = lng
        self.user_id = user_id
        self.profile_image = profile_image
        self.category_id = category_id
        self.place_id = place_id

    def to_dict(self):
        category = CategoryService.get(self.category_id)
        _dict = {'id': self.id,
                 'title': self.title,
                 'description': self.description,
                 'headerImage': category.image if category is not None else None,
                 'address': self.address,
                 'time': self.time,
                 'lat': self.lat,
                 'lng': self.lng,
                 'userId': self.user_id,
                 'profileImage': self.profile_image,
                 'categoryId': self.category_id,
                 'placeId': self.place_id}
        return {k: v for k, v in _dict.items() if v}