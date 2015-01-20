import os
import json
from flask import Flask, request, Response
from flask import render_template, send_from_directory, url_for
from flask.ext.login import LoginManager

app = Flask(__name__)

app.config.from_object('metapp.settings')
app.url_map.strict_slashes = False

# Login manager
login_manager = LoginManager()
login_manager.init_app(app)

import metapp.core
import metapp.models
import metapp.controllers

