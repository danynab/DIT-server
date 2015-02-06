__author__ = 'Dani'

from application.model import Event
from application import db


class EventService:
    @staticmethod
    def find_near_events(lat, lng, redius, category_id=None, limit=None, page=None):
        events_alchemy = Event.query.all()
        events = []
        for event in events_alchemy:
            events.append(event.to_dict())
        return events

    @staticmethod
    def find_events_by_user_id(user_id, limit=None, page=None):
        events_alchemy = Event.query.all()
        events = []
        for event in events_alchemy:
            events.append(event.to_dict())
        return events

    @staticmethod
    def save_event(event):
        db.session.add(event)
        db.session.commit()
