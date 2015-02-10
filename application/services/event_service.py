__author__ = 'Dani'

from application.model import Event
from application import db
from sqlalchemy import desc
from haversine import haversine


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
            event = Event.query.get(from_id)
            if event is not None:
                events_temp = events.order_by(desc(Event.time)).filter(Event.time >= event.time)
                row = 0
                for event_temp in events_temp:
                    row += 1
                    if event_temp.id == event.id:
                        break
            else:
                return []
        else:
            row = 0
        events = events.order_by(desc(Event.time))

        def is_closed(event_lat, event_lng):
            if lat is None or lng is None or radius is None:
                return True
            else:
                return haversine((float(lat), float(lng)), (float(event_lat), float(event_lng))) <= float(radius)

        events = [event for event in events[int(row):int(row) + int(elements)] if is_closed(event.lat, event.lng)]
        return events

    @staticmethod
    def find_events_by_user_id(user_id, from_id, elements):
        events = Event.query.filter(Event.user_id == user_id)
        return EventService._partition_events(events, from_id, elements)

    @staticmethod
    def get(event_id):
        return Event.query.get(event_id)

    @staticmethod
    def save_event(event):
        db.session.add(event)
        db.session.commit()

    @staticmethod
    def _partition_events(events, from_id, elements):

        if from_id is not None:
            event = Event.query.get(from_id)
            if event is not None:
                events_temp = events.order_by(desc(Event.time)).filter(Event.time >= event.time)
                row = 0
                for event_temp in events_temp:
                    row += 1
                    if event_temp.id == event.id:
                        break
            else:
                return []
        else:
            row = 0
        events = events.order_by(desc(Event.time)).offset(row).limit(elements)
        return events
