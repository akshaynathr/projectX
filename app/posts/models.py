from flask.ext.mongoengine import MongoEngine
from users.models import _user
db=MongoEngine()

class _post(db.Document):
	_author=db.ReferenceField(_user)
	_title=db.StringField()
	_content=db.StringField()
#	_position
	_tags=db.ListField(db.StringField())
	meta={ 'allow_inheritance':True}

class _comments(db.EmbeddedDocument):
	_content=db.StringField()	



class _imagepost(_post):
	_image_path=db.StringField()
	
class _soundpost(_post):
	_sound_path=db.StringField()

class _videopost(_post):
	_video_path=db.StringField()

class _article(_post):
	_article_link=db.StringField()

