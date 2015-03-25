from flask import Flask

from flask.ext.mongoengine import MongoEngine

from models import db

app=Flask(__name__)

app.config["MONGODB_SETTINGS"]={'db':'hoistmeapp'}

db.init_app(app)

