from flask.ext.mongoengine import MongoEngine

db=MongoEngine()

class _user(db.Document):
	_name=db.StringField()
	_emailid=db.StringField()
	_password=db.StringField()

class _post(db.Document):
	_author=db.ReferenceField(_user)
	_title=db.StringField()
	_content=db.StringField()
#	_position
	_tags=db.ListField(db.StringField())
	meta={ 'allow_inheritance':True}

class _comments(db.EmbeddedDocument):
	_content=db.StringField()	

