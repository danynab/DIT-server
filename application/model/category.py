__author__ = 'Dani'


class Category():
    def __init__(self, id_category, name, color='#000000'):
        self.id_category = id_category
        self.name = name
        self.color = color

    def to_dict(self):
        _dict = {'id': self.id_category,
                 'name': self.name,
                 'color': self.color}
        return {k: v for k, v in _dict.items() if v}
