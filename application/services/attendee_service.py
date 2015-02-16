from application import db
from application.model.attendee import Attendee

__author__ = 'Dani Meana'


class AttendeeService:
    @staticmethod
    def find_attendees_by_event_id(event_id):
        return Attendee.query.filter(Attendee.event_id == event_id)

    @staticmethod
    def get(event_id, user_id):
        return Attendee.query.filter(Attendee.event_id == event_id).filter(Attendee.user_id == user_id).first()

    @staticmethod
    def save(attendee):
        db.session.add(attendee)
        db.session.commit()

    @staticmethod
    def delete(attendee):
        print(attendee)
        db.session.delete(attendee)
        db.session.commit()
