from application.model.category import Category
from application.wsservices.category_wsservice import CategoryWSService
from application import db

__author__ = 'Dani Meana'


class CategoryService:
    @staticmethod
    def get_all():
        categories = CategoryWSService.get_all_categories()
        categories_result = []
        for category in categories:
            category_in_bd = CategoryService.get(category.id)
            if category_in_bd is not None:
                category.color = category_in_bd.color
                category.image = category_in_bd.image
            categories_result.append(category)
        return categories_result

    @staticmethod
    def get(category_id):
        return Category.query.get(category_id)

    @staticmethod
    def save(category):
        db.session.add(category)
        db.session.commit()