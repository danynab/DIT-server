__author__ = 'Dani'


class Place():
    def __init__(self, id_place, name, lat, lng, address, image, category_id, rating):
        self.id = id_place
        self.name = name
        self.lat = lat
        self.lng = lng
        self.address = address
        self.image = image
        self.category_id = category_id
        self.rating = rating

    def to_dict(self):
        _dict = {'id': self.id,
                 'name': self.name,
                 'lat': self.lat,
                 'lng': self.lng,
                 'address': self.address,
                 'image': self.image,
                 'categoryId': self.category_id,
                 'rating': self.rating
        }
        return {k: v for k, v in _dict.items() if v}