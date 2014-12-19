import requests
import json
import datetime
from server.db import db
from . import app
from flask import redirect
from flask import jsonify

# def db_entry(api_endpoint, payload):
#     url = 'http://localhost:5000/api/' + api_endpoint
#     print payload
#     print url
#     r = requests.post(url, data=json.dumps(payload), headers={'Content-Type': 'application/json'})
#     print r.text
#     return

class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.BigInteger, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def save(self):
        self.updated_at = datetime.datetime.utcnow()
        db.session.add(self)

    def delete(self):
        db.session.remove(self)

    def __repr__(self):
        return '<%s %d>' % (self.__class__.__name__, self.id)

def to_json(inst, cls):
    convert = dict()
    # add your coversions for things like datetime's 
    # and what-not that aren't serializable.
    d = dict()
    for c in cls.__table__.columns:
        v = getattr(inst, c.name)
        if c.type in convert.keys() and v is not None:
            try:
                d[c.name] = convert[c.type](v)
            except:
                d[c.name] = "Error:  Failed to covert using ", str(convert[c.type])
        elif v is None:
            d[c.name] = str()
        else:
            d[c.name] = v
    return json.dumps(d) 

class User(Base):
    __tablename__ = 'users'
    name = db.Column(db.Text)
    email = db.Column(db.Text)
    twitter_handle = db.Column(db.Text, unique=True)
    photo = db.Column(db.Text)

    def __init__(self, name, email, twitter_handle, photo):
        self.name = name
        self.email = email
        self.twitter_handle = twitter_handle
        self.photo = photo

    @property
    def serialize(self):
        return to_json(self, self.__class__)      

    @staticmethod
    def get_or_create(payload):
        print('\n\nI AM HERE\n\n')
        resp = db.session.query(User).filter(User.twitter_handle==payload['twitter_handle']).first()
        print "NAME:" + resp.name
        if resp:
            return resp
        user = User(payload['name'], payload['email'], payload['twitter_handle'], payload['photo'])
        db.session.add(user)
        db.session.commit()
        return user            

# MODELS EXPOSED VIA API
app.config['API_MODELS'] = { 'users' : User }

# MODELS PERMITTED FOR CRUD
app.config['CRUD_URL_MODELS'] = { 'users' : User }
