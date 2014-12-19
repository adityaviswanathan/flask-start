import requests
import json
from . import app
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restless import APIManager

db = SQLAlchemy(app)
api_manager = APIManager(app, flask_sqlalchemy_db=db)

def db_entry(api_endpoint, payload):
	url = 'http://localhost:5000/api/' + api_endpoint
	print payload
	print url
	r = requests.post(url, data=json.dumps(payload), headers={'Content-Type': 'application/json'})
	# print 'I AM HERE'
	print r.text
	return
