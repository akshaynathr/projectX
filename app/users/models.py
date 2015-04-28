from flask.ext.mongoengine import MongoEngine

db=MongoEngine()

class User(db.Document):
	
	email=db.StringField()
	password=db.StringField()
	authenticated=db.StringField()

	def is_active(self):
		return True

	def get_id(self):
		return self.email

	def is_authenticated(self):
		return self.authenticated

	def is_anonymous(self):
		return False



