from datetime import datetime

from metapp.core import db
from metapp import app

from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash

class User(db.Model):
	__tablename__ = "users"
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(80))
	last_name = db.Column(db.String(80))
	username = db.Column(db.String(25))
	password = db.Column(db.String(50))
	date_joined = db.Column(db.DateTime)
	date_last_logged_in = db.Column(db.DateTime)
   
	def __init__(self, first_name, last_name, username, password):
		self.first_name = first_name.title()
		self.last_name = last_name.title()
		self.username = username.lower()
		self.set_password(password)
	 
	def set_password(self, password):
		self.password = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password, password)

	def is_active(self):
		return True

	def get_id(self):
		return self.id

	












# # models for which we want to create API endpoints
# app.config['API_MODELS'] = { 'post': Post, 'comment' : Comment }

# # models for which we want to create CRUD-style URL endpoints,
# # and pass the routing onto our AngularJS application
# app.config['CRUD_URL_MODELS'] = { 'post': Post, 'comment' : Comment }
