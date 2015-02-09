__author__ = 'Dani'

from application.wsservices import client, colors
from application.model import Category


class CategoryWSService:
    @staticmethod
    def get_all_categories():
        categories_from_ws = client.service.get_all_category()[0]
        categories_from_ws.append(categories_from_ws.pop(0))
        categories_from_ws = sorted(categories_from_ws, key=lambda category: category.name)
        return [Category(category.id, category.name, colors.next_color()) for category in categories_from_ws]
