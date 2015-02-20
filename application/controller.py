from urllib.error import URLError
from application.model import event, attendee
from application.model.category import Category
from application.services.attendee_service import AttendeeService
from application.services.category_service import CategoryService
from application.services.event_service import EventService
from application.services.place_service import PlaceService
from werkzeug.exceptions import BadRequest

__author__ = 'Dani Meana'

import flask
from application import app


@app.after_request
def print_ip(response):
    ip = flask.request.headers.environ['HTTP_X_FORWARDED_FOR']
    user_agent = flask.request.headers.environ['HTTP_USER_AGENT']
    print()
    print(('IP: ' + ip if ip else 'None') + ((' - UserAgent: ' + user_agent) if user_agent else ''))
    return response


@app.errorhandler(Exception)
def all_exception_handler(error):
    print('ERROR: ' + str(error))
    return _response_error(code="dit_err", message="Server critical error. Please, contact with administrators. "
                                                   "Error: " + str(error),
                           status=500)


@app.errorhandler(404)
def resource_not_found(error):
    return _response_error(code="dit_404", message="Resource not found", status=404)


@app.route("/createTables")
def create():
    from application import db
    import application.data as data

    db.drop_all()
    print('## DB dropped ##')
    db.create_all()
    print('## DB created ##')

    fill = _get_request_arg('fill', True)
    print('## Fill: ' + ('True' if fill else 'False') + ' ##')
    if fill is True:
        for category in data.categories:
            CategoryService.save(
                Category(id_category=category['id'],
                         color=category['color'],
                         image=category['image']))

        for i in range(0, 10):
            for event_dict in data.events:
                EventService.save(event.from_dict(event_dict))

        for attendee_dict in data.attendees:
            AttendeeService.save(attendee.from_dict(attendee_dict))
        print('## DB filled ##')

    return _response_ok(code="dit_hello", message="Data initialized")


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
    try:
        return _collection_to_json(EventService.find_near_events(lat, lng, radius, from_id, elements))
    except ValueError:
        return _response_error(code="dit_fes", message="The arguments are not correct")


@app.route("/events", methods=["POST"])
def save_event():
    try:
        event_json = flask.request.get_json()
        event_obj = event.from_dict(event_json)
        EventService.save(event_obj)
        return _response_ok(code="dit_se", message="Event saved")
    except (KeyError, ValueError, BadRequest):
        return _response_error(code="dit_se", message="The event to save is wrong")


@app.route("/events/<int:event_id>", methods=["GET"])
def find_event(event_id):
    event_obj = EventService.get(event_id)
    if event_obj is None:
        return _response_error(code="dit_fe", message="Event not found")
    return _element_to_json(event_obj)


@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    event_obj = EventService.get(event_id)
    if event_obj is None:
        return _response_error(code="dit_de", message="Event not found")
    EventService.delete(event_obj)
    return _response_ok(code="dit_de", message="Event deleted")


@app.route("/events/<int:event_id>", methods=["PUT"])
def update_event(event_id):
    try:
        event_json = flask.request.get_json()
        event_obj = event.from_dict(event_json)
    except (KeyError, BadRequest):
        return _response_error(code="dit_ue", message="Event to update is wrong")

    try:
        event_obj.id = event_id
        EventService.update(event_obj)
        return _response_ok(code="dit_ue", message="Event updated")
    except (ValueError, AttributeError):
        return _response_error(code="dit_ue", message="Event to update does not exist")


@app.route("/events/<int:event_id>/attendees", methods=["GET"])
def find_attendees(event_id):
    return _collection_to_json(AttendeeService.find_attendees_by_event_id(event_id))


@app.route("/events/<int:event_id>/attendees", methods=["POST"])
def add_attendee(event_id):
    try:
        attendee_json = flask.request.get_json()
        attendee_obj = attendee.from_dict(attendee_json)
    except (KeyError, BadRequest):
        return _response_error(code="dit_aa", message="Attendee to add to an event is wrong")
    if event_id is not attendee_obj.event_id:
        return _response_error(code="dit_aa", message="The event of the attendee is not correct")
    event_obj = EventService.get(event_id)
    if event_obj is None:
        return _response_error(code="dit_aa", message="Event not found")
    attendee_old = AttendeeService.get(event_id, attendee_obj.user_id)
    if attendee_old is not None:
        return _response_ok(code="dit_aa", message="Attendee already exists")
    AttendeeService.save(attendee_obj)
    return _response_ok(code="dit_aa", message="Attendee added")


@app.route("/events/<int:event_id>/attendees/<string:user_id>", methods=["DELETE"])
def delete_attendee(event_id, user_id):
    attendee_obj = AttendeeService.get(event_id, user_id)
    if attendee_obj is None:
        return _response_error(code="dit_da", message="Attendee not found")
    AttendeeService.delete(attendee_obj)
    return _response_ok(code="dit_da", message="Attendee deleted")


@app.route("/users/<string:user_id>/events", methods=["GET"])
def find_events_by_user(user_id):
    from_id = _get_request_arg('fromId', None)
    elements = _get_request_arg('elements', None)
    try:
        return _collection_to_json(EventService.find_events_by_user_id(user_id, from_id, elements))
    except ValueError:
        return _response_error(code="dit_fesu", message="The arguments are not correct")


@app.route("/users/<string:user_id>/attendees/events", methods=["GET"])
def find_user_attended_events(user_id):
    from_id = _get_request_arg('fromId', None)
    elements = _get_request_arg('elements', None)
    attendees = AttendeeService.find_attendees_by_user_id(user_id)
    try:
        return _collection_to_json(EventService.find_events_by_attendees(attendees, from_id, elements))
    except ValueError:
        return _response_error(code="dit_fuae", message="The arguments are not correct")


@app.route("/categories/<int:category_id>/events", methods=["GET"])
def find_near_events_by_category(category_id):
    lat = _get_request_arg('lat', None)
    lng = _get_request_arg('lng', None)
    radius = _get_request_arg('radius', None)
    from_id = _get_request_arg('fromId', None)
    elements = _get_request_arg('elements', None)
    try:
        return _collection_to_json(
            EventService.find_near_events_by_category_id(category_id, lat, lng, radius, from_id, elements))
    except ValueError:
        return _response_error(code="dit_fesc", message="The arguments are not correct")


@app.route("/categories")
def find_categories():
    try:
        return _collection_to_json(CategoryService.get_all())
    except URLError:
        return _response_error(code="dit_fc", message="The server is not available", status=500)


@app.route("/categories/<int:category_id>", methods=["GET"])
def find_category(category_id):
    category_obj = CategoryService.get(category_id)
    if category_obj is None:
        return _response_error(code="dit_fc", message="Category not found")
    return _element_to_json(category_obj)


@app.route("/categories/<int:category_id>/places", methods=["GET"])
def find_near_places_by_category(category_id):
    lat = _get_request_arg('lat', None)
    lng = _get_request_arg('lng', None)
    radius = _get_request_arg('radius', None)
    elements = _get_request_arg('elements', None)
    try:
        return _collection_to_json(PlaceService.find_near_places_by_category(category_id, lat, lng, radius, elements))
    except URLError:
        return _response_error(code="dit_fpc", message="The server is not available", status=500)


def _get_request_arg(arg, default_value):
    return flask.request.args.get(arg, default_value)


def _collection_to_json(collection):
    return _response([e.to_dict() for e in collection])


def _element_to_json(element):
    return _response(element.to_dict())


def _response(data):
    return flask.Response(response=flask.json.dumps(data),
                          status=200,
                          mimetype='application/json')


def _response_ok(code, message):
    data = {
        'code': code,
        'message': message
    }
    return flask.Response(response=flask.json.dumps(data),
                          status=200,
                          mimetype='application/json')


def _response_error(code, message, status=400):
    data = {
        'code': code,
        'message': message
    }
    return flask.Response(response=flask.json.dumps(data),
                          status=status,
                          mimetype='application/json')
