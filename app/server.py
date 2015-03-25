from flask import Flask,render_template,request

from flask.ext.mongoengine import MongoEngine

from models import db

app=Flask(__name__)

app.config["MONGODB_SETTINGS"]={'db':'hoistme'}


db.init_app(app)



@app.route('/home')
@app.route('/')

def home():
	return render_template('home.html')


#flask blueprint registering

def blueprints():
	pass

blueprints()	
	

