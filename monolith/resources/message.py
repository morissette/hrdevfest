"""
resources.message
"""
import time

from flask import current_app
from flask_restful import Resource

from pymongo.errors import DuplicateKeyError


class Message(Resource):
    """
    Handles Requests to Messaging API Endpoints
    """

    def get(self, message_id=None):
        """
        GET Requests
        """
        if message_id is not None:
            if int(message_id) == 0:
                return get_message_history()
            else:
                return get_message(message_id)

        else:
            return get_last_message()

    def post(self):
        """
        POST Requests
        """
        current_app.mongo.db.messages.insert_one({"_id": 0, "message": "testing"})
        current_app.mongo.db.messages.insert_one({"_id": 1, "message": "testing2"})
        return {
            "status": 200,
            "result": "success",
            "message": "Message sent"
        }

    def put(self, message_id):
        """
        PUT Requests
        """
        return edit_message(message_id)

    def delete(self, message_id):
        """
        Delete Requests
        """
        return delete_message(message_id)

def get_message_history():
    messages = current_app.mongo.db.messages.find()
    return [message for message in messages]

def get_message(message_id):
    return current_app.mongo.db.messages.find_one_or_404({"_id": int(message_id)})

def get_last_message():
    return current_app.mongo.db.messages.find_one()

def edit_message(message_id):
    current_app.mongo.db.messages.replace_one({"_id": int(message_id)}, {"message": "new message"})
    return {
        "status": 200,
        "result": "success",
        "message": "Message modified"
    }

def delete_message(message_id):
    current_app.mongo.db.messages.delete_one({"_id": int(message_id)})
    return {
        "status": 200,
        "result": "success",
        "message": "Message removed"
    }
