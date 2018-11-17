#!/usr/bin/env python
"""
resources.authentication
"""
from flask import current_app
from flask_restful import Resource

from pymongo.errors import DuplicateKeyError


class Auth(Resource):
    """
    Handles Requests to Authentication API Endpoints
    """
    username = 'matt' # placeholder

    def get(self):
        """
        GET Requests
        """
        authed = current_app.mongo.db.users.find_one_or_404({"_id": self.username})
        return {
            "status": 200,
            "result": "success",
            "message": "User is authenticated"
        }

    def post(self):
        """
        POST Requests
        """
        try:
            result = current_app.mongo.db.users.insert_one({"_id": self.username})
            return {
                "status": 200,
                "result": "success",
                "message": "Authentication successful"
            }
        except DuplicateKeyError:
            return {
                "status": 409,
                "result": "error",
                "message": "Authentication failed"
            }
        except Exception:
            return {
                "status": 500,
                "result": "error",
                "message": "Authentication failed"
            }

    def put(self):
        """
        PUT Requests
        """
        authed = current_app.mongo.db.users.find_one_or_404({"_id": self.username})
        return {
            "status": 200,
            "result": "success",
            "message": "Authentication refreshed"
        }

    def delete(self):
        """
        Delete Requests
        """
        authed = current_app.mongo.db.users.find_one_or_404({"_id": self.username})
        current_app.mongo.db.users.delete_one({"_id": self.username})
        return {
            "status": 200,
            "result": "success",
            "message": "Logged out"
        }
