__author__ = 'Dani'

from application.model import Event
from application import db
from sqlalchemy import desc


class EventService:
    @staticmethod
    def find_near_events(lat, lng, radius, from_id, elements):
        return EventService.find_near_events_by_category_id(None, lat, lng, radius, from_id, elements)

    @staticmethod
    def find_near_events_by_category_id(category_id, lat, lng, radius, from_id, elements):
        events = Event.query
        if category_id is not None:
            events = events.filter(Event.category_id == category_id)
        if from_id is not None:
            events = events.filter(Event.id < from_id)
        events = events.order_by(desc(Event.id)).limit(elements)
        return events

    @staticmethod
    def find_events_by_user_id(user_id, from_id, elements):
        events = Event.query.filter(Event.user_id == user_id)
        if from_id is not None:
            events = events.filter(Event.id < from_id)
        events = events.order_by(desc(Event.id)).limit(elements)
        return events

    @staticmethod
    def get(event_id):
        return Event.query.get(event_id)

    @staticmethod
    def save_event(event):
        db.session.add(event)
        db.session.commit()
