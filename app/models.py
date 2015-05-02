from flask.ext.mongoengine import MongoEngine

from posts.models import _post



db=MongoEngine()

class Global(db.Document):
	total_users_registered= db.IntField(min_value=1,default=1)
	total_active_users=db.IntField(min_value=0)
