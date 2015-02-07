__author__ = 'Dani'

from application.model import Event
from application import db


class EventService:
    @staticmethod
    def find_near_events(lat, lng, redius, category_id=None, limit=None, page=None):
        return Event.query.all()

    @staticmethod
    def find_events_by_user_id(user_id, limit=None, page=None):
        return Event.query.all()

    @staticmethod
    def save_event(event):
        db.session.add(event)
        db.session.commit()
