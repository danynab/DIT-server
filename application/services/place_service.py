from application.wsservices.place_wsservice import PlaceWSService

__author__ = 'Dani Meana'


class PlaceService:
    @staticmethod
    def find_near_places_by_category(category_id, lat, lng, radius, elements=None):
        places = PlaceWSService.find_near_places_by_category(
            category_id=category_id,
            lat=lat,
            lng=lng,
            radius=radius,
            elements=int(elements) if elements is not None else None)
        return places