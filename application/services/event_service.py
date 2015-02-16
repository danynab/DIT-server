import time
import datetime
from application.model.event import Event
from application import db
from sqlalchemy import asc
from haversine import haversine

__author__ = 'Dani'


class EventService:
    @staticmethod
    def find_near_events(lat, lng, radius, from_id, elements):
        return EventService.find_near_events_by_category_id(None, lat, lng, radius, from_id, elements)

    @staticmethod
    def find_near_events_by_category_id(category_id, lat, lng, radius, from_id, elements):
        time_millis = time.mktime(datetime.datetime.now().timetuple()) * 1000
        events = Event.query.filter(Event.time > time_millis)
        if category_id is not None:
            events = events.filter(Event.category_id == category_id)
        events = events.order_by(asc(Event.time))
        position = _get_row(events, from_id)
        if position is None:
            return []
        events = [event for event in events if _are_points_closed(event.lat, event.lng, lat, lng, radius)]
        return _partition_events(events, position, elements)

    @staticmethod
    def find_events_by_user_id(user_id, from_id, elements):
        time_millis = time.mktime(datetime.datetime.now().timetuple()) * 1000
        events = Event.query.filter(Event.user_id == user_id).filter(Event.time > time_millis).order_by(asc(Event.time))
        position = _get_row(events, from_id)
        return _partition_events(events, position, elements) if position is not None else []

    @staticmethod
    def get(event_id):
        return Event.query.get(event_id)

    @staticmethod
    def save(event):
        db.session.add(event)
        db.session.commit()


def _get_row(events, event_id):
    if event_id is None:
        return 0
    event = Event.query.get(event_id)
    if event is not None:
        events_temp = events.filter(Event.time <= event.time)
        row = 0
        for event_temp in events_temp:
            row += 1
            if event_temp.id == event.id:
                return row
    return None


def _partition_events(events, position, elements):
    return events if elements is None else [event for event in events[int(position):(int(position) + int(elements))]]


def _are_points_closed(lat1, lng1, lat2, lng2, radius):
    if lat1 is None or lng1 is None or lat2 is None or lng2 is None or radius is None:
        return True
    else:
        return haversine((float(lat1), float(lng1)), (float(lat2), float(lng2))) <= float(radius)
