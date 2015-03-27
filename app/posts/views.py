from flask import Blueprint,render_template,abort,request

from flask.ext.restful import Resource

from werkzeug import secure_filename
#post=Blueprint('post',__name__,template_folder='templates')

class Post(Resource):
	def get(self):
		return "welcome to hoistme api"
	def post(self):
		file=request.files['file']
		if file:
			return "File detected"
		else:
			return "File not detected"
	def put(self):
		return "feature not available now"

