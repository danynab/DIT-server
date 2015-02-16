__author__ = 'Dani Meana'

from application import db


class EventAttendees(db.Model):
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), primary_key=True)
    user_id = db.Column(db.Integer, primary_key=True)

    event = db.relationship('Event')

    def __init__(self, event_id, user_id):
        self.event_id = event_id
        self.user_id = user_id
