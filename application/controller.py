__author__ = 'Dani Meana'

import flask
from application import app
from application.services import EventService
from application.model import Event
import datetime, time


event1 = {
    "id": 1,
    "userId": "103788299879342667199",
    "title": "Don't eat alone in Computer Engineering's School",
    "description": "Hi! I am going to eat in EII and I do not want eat alone. "
                   "I am a amused person and I want eat with a person who likes talking about technology.",
    "categoryId": 1,
    "image": "http://156.35.95.67/dit/static/img/default-header.jpg",
    "time": time.mktime(datetime.datetime.now().timetuple()) * 1000,
    "lat": 43.355034,
    "lng": -5.851503,
    "address": "Calle Valdes Salas, 7, 33007 Oviedo, Asturias",
    "placeId": None
}

event2 = {
    "id": 2,
    "userId": "103788299879342667199",
    "title": "Have a drink and speach about Barsa vs Madrid",
    "description": "Howdy guys, We want people to talk about the next match between Barsa and Madrid. "
                   "Do you want to join us?",
    "categoryId": 2,
    "image": "http://156.35.95.67/dit/static/img/default-header.jpg",
    "time": time.mktime(datetime.datetime.now().timetuple()) * 1000,
    "lat": 43.36333,
    "lng": -5.845133,
    "address": "Calle Jovellanos, 4 33003 Oviedo, Asturias, Espana",
    "placeId": None
}

events = [event1, event2]

categories = [
    {
        "id": 1,
        "name": "Eating",
        "color": "#e91e64"
    },
    {
        "id": 2,
        "name": "Hangouts",
        "color": "#2196f3"
    },
    {
        "id": 2,
        "name": "Leisure",
        "color": "#ff5722"
    },
    {
        "id": 2,
        "name": "Personal care",
        "color": "#4caf50"
    },
    {
        "id": 2,
        "name": "Religion",
        "color": "#673ab7"
    },
    {
        "id": 2,
        "name": "Shopping",
        "color": "#ffeb3b"
    }
]


@app.route("/createTables")
def create():
    from application import db

    db.drop_all()
    db.create_all()
    event1_obj = Event.from_dict(event1)
    event2_obj = Event.from_dict(event2)
    event3_obj = Event.from_dict(event1)
    event4_obj = Event.from_dict(event2)
    event5_obj = Event.from_dict(event1)
    event6_obj = Event.from_dict(event2)
    EventService.save_event(event1_obj)
    EventService.save_event(event2_obj)
    EventService.save_event(event3_obj)
    EventService.save_event(event4_obj)
    EventService.save_event(event5_obj)
    EventService.save_event(event6_obj)
    return "<h1> Tablas creadas</h1>"


@app.route("/", methods=["GET"])
def hello():
    return flask.redirect("https://github.com/danynab/DIT-server")


@app.route("/events", methods=["GET"])
def find_near_events():
    lat = _get_request_arg('lat', None)
    lng = _get_request_arg('lng', None)
    radius = _get_request_arg('radius', None)
    limit = _get_request_arg('lng', None)
    page = _get_request_arg('lng', None)
    return _collection_to_json(EventService.find_near_events(lat, lng, radius, limit, page))


@app.route("/categories/<int:category_id>/events", methods=["GET"])
def find_near_events_by_category(category_id):
    lat = _get_request_arg('lat', None)
    lng = _get_request_arg('lng', None)
    radius = _get_request_arg('radius', None)
    limit = _get_request_arg('lng', None)
    page = _get_request_arg('lng', None)
    return _collection_to_json(EventService.find_near_events(lat, lng, radius, limit, page))


@app.route("/events/<int:event_id>")
def find_event(event_id):
    return _element_to_json(EventService.get(event_id))


@app.route("/categories")
def find_categories():
    return _response(categories)


def _get_request_arg(arg, default_value):
    return flask.request.args.get(arg, default_value)


def _collection_to_json(collection):
    return _response([e.to_dict() for e in collection])


def _element_to_json(element):
    return _response(element.to_dict())


def _response(data):
    """Create a JSON response."""
    return flask.Response(response=flask.json.dumps(data),
                          status=200,
                          mimetype="application/json")
