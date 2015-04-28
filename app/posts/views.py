
from flask import Blueprint,render_template,abort,request

from flask.ext.restful import Resource

from werkzeug import secure_filename
#post=Blueprint('post',__name__,template_folder='templates')
from models import _text

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
		userid=json['id']
		
		text=json['data']
		# decode the json and appropriately  call the required functions
		text_obj=_text.objects(pk=userid).first()
		text
		return json['data']

	def put(self):
		return "feature not available now"
