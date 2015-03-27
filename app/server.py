from flask import Flask,render_template,request

from flask.ext.mongoengine import MongoEngine

from posts.models import db

from flask.ext.restful import Api

from posts.views import Post

from resources import *

app=Flask(__name__)
app.config["MONGODB_SETTINGS"]={'db':'hoistme'}
api=Api(app)

db.init_app(app)



@app.route('/home')
@app.route('/')

def home():
	return render_template('home.html')


#flask blueprint registering

def blueprints():
	pass

blueprints()	
	
#RESOURCES FOR API

api.add_resource(Post,'/post')
