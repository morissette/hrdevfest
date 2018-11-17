#!/usr/bin/env python
"""
Sample Monolith Application
for HRDevFest 2018
Author Matthew Harris
"""
from resources.auth import Auth
from resources.message import Message
from resources.notification import Notification

from flask import Flask
from flask_pymongo import PyMongo
from flask_restful import reqparse, abort, Api, Resource

from pymongo.errors import DuplicateKeyError


# Setup Flask Service
app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/monolith'
app.mongo = PyMongo(app)
api = Api(app)

# Register API Endpoints
api.add_resource(Auth, '/v1/auth')
api.add_resource(Message, '/v1/message', '/v1/message/<message_id>')
api.add_resource(Notification, '/v1/notification', '/v1/notification/<notification_id>')

if __name__ == '__main__':
    app.run(debug=True)
