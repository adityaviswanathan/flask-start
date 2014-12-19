import os
import json
from flask import Flask, request, Response
# from flask.ext.triangle import Triangle

app = Flask(__name__, static_folder='../client/static', template_folder='../client/views')
app.config.from_object('server.settings')
app.url_map.strict_slashes = False
# Triangle(app)

import server.controllers
from server.db import db

# db.session = Session()


