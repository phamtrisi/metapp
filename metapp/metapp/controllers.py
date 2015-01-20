import os

from flask import Flask, request, Response
from flask import render_template, url_for, redirect, send_from_directory, flash
from flask import send_file, make_response, abort
from flask.ext.login import login_user

from metapp import app, login_manager

# routing for API endpoints (generated from the models designated as
# API_MODELS)
from metapp.core import api_manager, db
from metapp.models import User

# for model_name in app.config['API_MODELS']:
#     model_class = app.config['API_MODELS'][model_name]
#     api_manager.create_api(model_class, methods=['GET', 'POST'])

# session = api_manager.session

# routing for basic pages (pass routing onto the Angular app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route('/')
def index(**kwargs):
    return render_template('index.html')

@app.route('/login', methods=["GET", "POST"])
def login():
	if request.method == 'POST':
		data = request.values
		username = data.get('username')
		password = data.get('password')
		user = User.query.filter(User.username==username).first()
		
		if not user or (user and not user.check_password(password)):
			flash("Invalid login")
			return redirect(url_for('login'))	

		login_user(user)
		flash("Logged in")
		return redirect(url_for('index'))

	return render_template("login.html")		

@app.route('/signup', methods=["GET", "POST"])
def signup():
	if request.method == 'POST':
		data = request.values
		username = data.get('username')
		email = data.get('email')
		password = data.get('password')
		user = User(first_name="Si", last_name="Pham", username=username, password=password)
		db.session.add(user)
		db.session.commit()
		flash("created new user")
		return redirect(url_for('index'))

	return render_template("signup.html")

# routing for CRUD-style endpoints
# passes routing onto the angular frontend if the requested resource exists
from sqlalchemy.sql import exists

# crud_url_models = app.config['CRUD_URL_MODELS']


# @app.route('/<model_name>/')
# @app.route('/<model_name>/<item_id>')
# def rest_pages(model_name, item_id=None):
#     if model_name in crud_url_models:
#         model_class = crud_url_models[model_name]
#         if item_id is None or session.query(exists().where(
#                 model_class.id == item_id)).scalar():
#             return make_response(open(
#                 'metapp/templates/index.html').read())
#     abort(404)

# special file handlers and error handlers


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'img/favicon.ico')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(403)
@app.errorhandler(401)
def not_allowed(e):
		return render_template('403.html'), 403
