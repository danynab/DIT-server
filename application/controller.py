__author__ = 'Dani Meana'

import flask
from application import app
from application.services import EventService
from application.model import Event
import datetime


event1 = {
    "id": 1,
    "userId": "103788299879342667199",
    "title": "Don't eat alone in Computer Engineering's School",
    "description": "Hi! I am going to eat in EII and I do not want eat alone. "
                   "I am a amused person and I want eat with a person who likes talking about technology.",
    "categoryId": 2,
    "image": "http://156.35.95.69:8888/img/default-header.jpg",
    "date": "2015-02-15 13:30:00",
    "lat": 43.355034,
    "lng": -5.851503,
    "address": "Calle Valdes Salas, 7, 33007 Oviedo, Asturias"}

event2 = {
    "id": 2,
    "userId": "103788299879342667199",
    "title": "Have a drink and speach about Barsa vs Madrid",
    "description": "Howdy guys, We want people to talk about the next match between Barsa and Madrid. "
                   "Do you want to join us?",
    "categoryId": 1,
    "image": "http://156.35.95.69:8888/img/default-header.jpg",
    "date": "2015-02-20 18:30:00",
    "lat": 43.36333,
    "lng": -5.845133,
    "address": "Calle Jovellanos, 4 33003 Oviedo, Asturias, Espana"
}

events = [event1, event2]

category1 = {"id": 1, "name": "Hangouts"}

category2 = {"id": 2, "name": "Eating"}

categories = [category1, category2]

hello_message = "<h1>WELCOME TO DIT-server</h1>" \
                "<h3>Methods:</h3>" \
                "<ul><li>/events</li>" \
                "<li>/categories/<i>&lt;category_id&gt;</i>/events</li>" \
                "<li>/events/<i>&lt;event_id&gt;</i></li>" \
                "<li>/categories</li>"


@app.route("/createTables")
def create():
    from application import db

    db.drop_all()
    db.create_all()
    user_id = "103788299879342667199"
    title = "Don't eat alone in Computer Engineering's School"
    description = "Hi! I am going to eat in EII and I do not want eat alone. " \
                  "I am a amused person and I want eat with a person who likes talking about technology."
    category_id = 2
    image = "http://156.35.95.69:8888/img/default-header.jpg"
    date = "2015-02-15 13:30:00"
    lat = 43.355034
    lng = -5.851503
    address = "Calle Valdes Salas, 7, 33007 Oviedo, Asturias"
    event = Event(title, description, image, address, datetime.datetime.now(), lat, lng, user_id, category_id)
    EventService.save_event(event)
    return "<h1> Tablas creadas</h1>"


@app.route("/", methods=["GET"])
def hello():
    return hello_message


@app.route("/events", methods=["GET"])
def find_near_events():
    lat = _get_request_arg('lat', None)
    lng = _get_request_arg('lng', None)
    radius = _get_request_arg('radius', None)
    limit = _get_request_arg('lng', None)
    page = _get_request_arg('lng', None)
    events_array = EventService.find_near_events(lat, lng, radius, limit, page)
    return _response(events_array)


@app.route("/categories/<int:category_id>/events", methods=["GET"])
def find_near_events_by_category(category_id):
    return _response(events)


@app.route("/events/<int:event_id>")
def find_event(event_id):
    return _response(event1)


@app.route("/categories")
def find_categories():
    return _response(categories)


def _get_request_arg(arg, default_value):
    return flask.request.args.get(arg, default_value)


def _response(data):
    """Create a JSON response."""
    return flask.Response(response=flask.json.dumps(data),
                          status=200,
                          mimetype="application/json")