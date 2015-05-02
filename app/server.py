from flask import Flask,render_template,request,redirect,url_for

from flask.ext.cors import CORS

from flask.ext.mongoengine import MongoEngine

from users.models import db

from flask.ext.restful import Api

from posts.views import Post

from resources import *

from users.models import User

from models import Global
 
from flask.ext.login import LoginManager,login_user,logout_user,current_user,login_required


from mongoengine import *





app=Flask(__name__,static_folder='templates')
app.config["MONGODB_SETTINGS"]={'db':'hoistme'}
app.secret_key="akshaynathrhoistme"
api=Api(app)
cors = CORS(app)
db.init_app(app)

login_manager=LoginManager()
login_manager.init_app(app)
login_manager.login_view='home'



#login userload function - predefined for flask login

@login_manager.user_loader
def load_user(mail):
    t= User.objects(email=mail).first()
    print(t)
    return t




@app.route('/home')
@app.route('/')
@app.route('/login')

def home():
	return render_template('index.html')


#flask blueprint registering

def blueprints():
	pass

blueprints()	
	
#RESOURCES FOR API

api.add_resource(Post,'/post')





#login

@app.route('/login',methods=['POST'])
@app.route('/',methods=['POST'])
@app.route('/home', methods=['POST'])
def login():
	if request.form['email'] and request.form['password']:
		email=request.form['email']
		password=request.form['password']
		obj=User.objects.filter(Q(email=email) & Q(password=password)).first()
		
		if obj:
			print ("User found. Proceeding login ");
			login_user(obj)
		        return "Logged in "			
		else:	
			print("User not found . Proceed Registration ");
			return redirect(url_for('register'))

	return "Enter proper email or username"	
	



#logout
@app.route('/logout')
@login_required
def logout():
	logout_user
	print('logged out')
	return redirect(url_for('home'))



#registration page

@app.route('/register',methods=['GET'])
def register():
	return render_template("registration/index.html")	

@app.route('/register',methods=['POST'])
def addtodatabase():
	
	email     = request.form['email']
	password  = request.form['password']
	if email is None :
		return "Error . Enter email" 
	if password is None:
		return "Error .Enter password"
	obj=User.objects.filter(Q(email=email) & Q(password=password)).first()
	if obj is None:
		newUser=User()
		newGLOBAL=Global()
		newUser.email= email
		newUser.password=password
		newUser.authenticated=True
		newUser.save()
		newGLOBAL.inc__total_users_registered=1
		newGLOBAL.save()
		login_user(newUser)
		return "logged In"
	else:
		return redirect(url_for('home'))	



#admin use- total users
@app.route('/admin')
def count():
	obj=User()
	return "Count"+(obj.objects.item_frequencies())
