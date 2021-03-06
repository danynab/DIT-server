from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.cors import CORS

__author__ = 'Dani Meana'


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/dit.db'
cors = CORS(app, resources=r'*', allow_headers='Content-Type')
db = SQLAlchemy(app)

import application.controller
