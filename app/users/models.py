from flask.ext.mongoengine import MongoEngine

db=MongoEngine()

class _user(db.Document):
        _name=db.StringField()
        _emailid=db.StringField()
        _password=db.StringField()

