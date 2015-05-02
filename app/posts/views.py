
from flask import Blueprint,render_template,abort,request

from flask.ext.restful import Resource

from werkzeug import secure_filename
#post=Blueprint('post',__name__,template_folder='templates')

from users.models import User

from models import _post

class Post(Resource):
	def get(self):
		apikey=request.headers.get("Authorization",'')
		
		if apikey.lower() =="123":

			json=request.json
			data=json['text']
			print(data)

			return data	
		else:
			return "Authenticate"
				

	def post(self):

		json=request.json
		
		print (json)	
		userid=request.json['id']
		#query for the user with user id
		target_user=User.objects(pk=userid).first()
		
		#create new post object. Fill the details and save
		newpost=_post()
		newpost._title=json['data']
		#point the post to user
		target_user.posts.append(new_post)
		target_user.save()
		# decode the json and appropriately  call the required functions
		return json['data']

	def put(self):
		return "feature not available now"
