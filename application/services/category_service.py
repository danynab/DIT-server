__author__ = 'Dani'

from application.wsservices import CategoryWSService


class CategoryService:
    @staticmethod
    def get_all():
        return CategoryWSService.get_all_categories()