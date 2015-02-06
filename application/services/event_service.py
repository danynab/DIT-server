__author__ = 'Dani'

from application.model import Event
from application import db


def find_near_events(lat, lng, redius, limit=None, page=None):
    events_alchemy = Event.query.all()
    events = []
    for event in events_alchemy:
        events.append(event.to_dict())
    return events


def save_event(event):
    db.session.add(event)
    db.session.commit()
