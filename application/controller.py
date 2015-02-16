from application.model import event
from application.model.category import Category
from application.services.category_service import CategoryService
from application.services.event_service import EventService
from application.services.place_service import PlaceService

__author__ = 'Dani Meana'

import flask
from application import app


@app.route("/createTables")
def create():
    from application import db
    import application.data as data

    db.drop_all()
    db.create_all()

    for category in data.categories:
        CategoryService.save(
            Category(id_category=category["id"], color=category["color"], image=category["image"]))

    for i in range(0, 10):
        for event_dict in data.events:
            EventService.save(event.from_dict(event_dict))

    return "<h1> Tablas creadas</h1>"


@app.route("/", methods=["GET"])
def hello():
    return flask.redirect("https://github.com/danynab/DIT-server")


@app.route("/events", methods=["GET"])
def find_near_events():
    lat = _get_request_arg('lat', None)
    lng = _get_request_arg('lng', None)
    radius = _get_request_arg('radius', None)
    from_id = _get_request_arg('fromId', None)
    elements = _get_request_arg('elements', None)
    return _collection_to_json(EventService.find_near_events(lat, lng, radius, from_id, elements))


@app.route("/events", methods=["POST"])
def save_event():
    event_json = flask.request.get_json()
    event_obj = event.from_dict(event_json)
    EventService.save(event_obj)
    return _response_ok()


@app.route("/events/<int:event_id>")
def find_event(event_id):
    return _element_to_json(EventService.get(event_id))


@app.route("/users/<string:user_id>/events", methods=["GET"])
def find_events_by_user(user_id):
    from_id = _get_request_arg('fromId', None)
    elements = _get_request_arg('elements', None)
    return _collection_to_json(EventService.find_events_by_user_id(user_id, from_id, elements))


@app.route("/categories/<int:category_id>/events", methods=["GET"])
def find_near_events_by_category(category_id):
    lat = _get_request_arg('lat', None)
    lng = _get_request_arg('lng', None)
    radius = _get_request_arg('radius', None)
    from_id = _get_request_arg('fromId', None)
    elements = _get_request_arg('elements', None)
    return _collection_to_json(
        EventService.find_near_events_by_category_id(category_id, lat, lng, radius, from_id, elements))


@app.route("/categories")
def find_categories():
    return _collection_to_json(CategoryService.get_all())


@app.route("/categories/<int:category_id>/places", methods=["GET"])
def find_near_places_by_category(category_id):
    lat = _get_request_arg('lat', None)
    lng = _get_request_arg('lng', None)
    radius = _get_request_arg('radius', None)
    elements = _get_request_arg('elements', None)
    return _collection_to_json(PlaceService.find_near_places_by_category(category_id, lat, lng, radius, elements))


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


def _response_ok():
    return flask.Response(status=200,
                          mimetype="application/json")