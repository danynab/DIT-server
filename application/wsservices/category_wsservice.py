from application.model.category import Category

__author__ = 'Dani Meana'

from application.wsservices import client


class CategoryWSService:
    @staticmethod
    def get_all_categories():
        categories_from_ws = client.get_client().service.get_all_categories()[0]
        categories_from_ws = sorted(categories_from_ws, key=lambda category: category.name)
        return [Category(category.id, category.name) for category in categories_from_ws]

    @staticmethod
    def get(category_id):
        category_from_ws = client.get_client().service.get_category(category_id)
        return Category(category_from_ws.id, category_from_ws.name)