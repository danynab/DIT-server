__author__ = 'Dani'

from application.model import Category
from application import db


class CategoryService:
    @staticmethod
    def get_all():
        return Category.query.all()

    @staticmethod
    def get(category_id):
        return Category.query.get(category_id)

    @staticmethod
    def save_event(event):
        db.session.add(event)
        db.session.commit()
