__author__ = 'Dani'

from application.wsservices import client, colors
from application.model import Category


class CategoryWSService:
    @staticmethod
    def get_all_categories():
        categories_from_ws = client.service.get_all_category()[0]
        return [Category(category.id, category.name, colors.next_color()) for category in categories_from_ws]
