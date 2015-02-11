__author__ = 'Dani'

import flask
import datetime, time


categories = [
    {
        "id": 1,
        "image": "http://156.35.95.67/dit/static/img/eating.png",
        "color": "#e91e64"
    },
    {
        "id": 2,
        "image": "http://156.35.95.67/dit/static/img/hangout.png",
        "color": "#2196f3"
    },
    {
        "id": 3,
        "image": "http://156.35.95.67/dit/static/img/leisure.png",
        "color": "#ff5722"
    },
    {
        "id": 4,
        "image": "http://156.35.95.67/dit/static/img/personal-care.png",
        "color": "#4caf50"
    },
    {
        "id": 5,
        "image": "http://156.35.95.67/dit/static/img/pray.png",
        "color": "#673ab7"
    },
    {
        "id": 6,
        "image": "http://156.35.95.67/dit/static/img/shopping.png",
        "color": "#ffeb3b"
    }
]

events = [
    {
        "id": 1,
        "userId": "103788299879342667199",
        "profileImage": "https://lh3.googleusercontent.com/-c50o8X13gjA/AAAAAAAAAAI/AAAAAAAABXA/NUBFG7rleUM/photo.jpg",
        "title": "Don't eat alone in Computer Engineering's School",
        "description": "Hi! I am going to eat in EII and I do not want eat alone. "
                       "I am a amused person and I want eat with a person who likes talking about technology.",
        "categoryId": 1,
        "headerImage": "http://156.35.95.67/dit/static/img/eating.png",
        "time": time.mktime(datetime.datetime.now().timetuple()) * 1000,
        "lat": 43.355034,
        "lng": -5.851503,
        "address": "Calle Valdes Salas, 7, 33007 Oviedo, Asturias",
        "placeId": None
    },
    {
        "id": 2,
        "userId": "100363393538924443678",
        "profileImage": "https://lh5.googleusercontent.com/-3IDJxUtZjzc/AAAAAAAAAAI/AAAAAAAAONo/rzdGnq3dW-k/photo.jpg",
        "title": "Have a drink and speach about Barsa vs Madrid",
        "description": "Howdy guys, We want people to talk about the next match between Barsa and Madrid. "
                       "Do you want to join us?",
        "categoryId": 2,
        "headerImage": "http://156.35.95.67/dit/static/img/hangout.jpg",
        "time": time.mktime(datetime.datetime.now().timetuple()) * 1000,
        "lat": 43.36333,
        "lng": -5.845133,
        "address": "Calle Jovellanos, 4 33003 Oviedo, Asturias, Espana",
        "placeId": None
    }
]