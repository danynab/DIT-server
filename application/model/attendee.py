from application import db

__author__ = 'Dani Meana'


class Attendee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String)
    event_id = db.Column(db.Integer)
    profile_image = db.Column(db.String)

    def __init__(self, user_id, event_id, profile_image):
        self.user_id = user_id
        self.event_id = event_id
        self.profile_image = profile_image

    def to_dict(self):
        _dict = {'userId': self.user_id,
                 'eventId': self.event_id,
                 'profileImage': self.profile_image}
        return {k: v for k, v in _dict.items() if v}


def from_dict(_dict):
    user_id = _dict['userId']
    event_id = _dict['eventId']
    profile_image = _dict['profileImage']
    return Attendee(
        user_id=user_id,
        event_id=event_id,
        profile_image=profile_image
    )