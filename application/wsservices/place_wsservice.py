from application.model.place import Place

__author__ = 'Dani'

from application.wsservices import client


class PlaceWSService:
    @staticmethod
    def find_near_places_by_category(category_id, lat, lng, radius, elements):
        places_from_ws = client.get_client().service.get_near_places_by_category_id(
            category_id=category_id,
            lat=lat,
            lng=lng,
            radius=radius,
            elements=elements)[0]
        places_from_ws = sorted(places_from_ws, key=lambda place: place.rating)
        return [Place(
            id_place=place.id,
            name=place.name,
            lat=place.lat,
            lng=place.lng,
            address=place.address,
            image=place.image if 'image' in place else None,
            category_id=place.category_id,
            rating=place.rating
        ) for place in places_from_ws]
