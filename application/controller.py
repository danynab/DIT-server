from application.model.category import Category
from application.model.event import Event
from application.services.category_service import CategoryService
from application.services.event_service import EventService

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
        for event in data.events:
            EventService.save(Event(
                title=event["title"],
                description=event["description"],
                address=event["address"],
                time=event["time"],
                lat=event["lat"],
                lng=event["lng"],
                user_id=event["userId"],
                profile_image=event["profileImage"],
                category_id=event["categoryId"],
                place_id=event["placeId"]
            ))

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


@app.route("/events/<int:event_id>")
def find_event(event_id):
    return _element_to_json(EventService.get(event_id))


@app.route("/categories")
def find_categories():
    return _collection_to_json(CategoryService.get_all())


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
