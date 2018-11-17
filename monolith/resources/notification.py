"""
Sample Monolith Application
for HRDevFest 2018
"""
from flask_restful import Resource

from pymongo.errors import DuplicateKeyError


class Notification(Resource):
    """
    Handles Requests to Notification API Endpoints
    """
    
    def get(self):
        """
        GET Requests
        """
        pass

    def post(self):
        """
        POST Requests
        """
        pass

    def put(self):
        """
        PUT Requests
        """
        pass

    def delete(self):
        """
        Delete Requests
        """
        pass
