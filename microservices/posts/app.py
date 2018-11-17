# coding: utf8
from flask import Flask, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy


# Handle Requests
class Posts(Resource):
    """
    Handles all HTTP methods for Post Service
    """
    def get(self, post_uuid=None):
        """
        Retreive all posts or a given post on uuid
        :param post_uuid: UUID
        :return: Dict
        """
        if post_uuid:
            return get_post(post_uuid)
        return get_all_posts()

    def post(self):
        """
        Create a new post
        """
        post_data = request.get_json(force=True)
        return create_post(post_data)

    def put(self, post_uuid):
        """
        Update a post
        :param post_uuid: UUID
        :return: Boolean
        """
        return update_post(post_uuid)

    def delete(self, post_uuid):
        """
        Delete a post
        :param post_uuid: UUID
        :return: Boolean
        """
        return delete_post(post_uuid)


# Functions
def get_post(post_uuid):
    """
    Pull data from db for a blog post
    :param post_uuid: UUID
    :return: Dict
    """
    # Mock Data
    return {
        "post_uuid": post_uuid,
        "title": "I'm a blog post!",
        "content": "Yes, this is a blog post about things and stuff but mainly about showing how to do microservices in a simple and easy way",
        "author": "Matthew Harris",
        "created": "12-03-2016 12:15:00",
        "updated": ""
    }

def get_all_posts():
    """
    Pull all posts from db
    :return: List of Dicts
    """
    # Mock Data
    return [
        {
            "post_uuid": "1234-5678-1234-5678",
            "title": "I'm a blog post!",
            "content": "A post about foo",
            "author": "Matthew Harris",
            "created": "12-03-2016 12:15:17",
            "updated": ""
        },
        {
            "post_uuid": "2345-6789-2345-6789",
            "title": "I'm a different blog post!",
            "content": "A different post about bar",
            "author": "Matthew Harris",
            "created": "12-03-2016 12:18:33",
            "updated": ""
        }
    ]

def create_post(post_data):
    """
    Create a new post
    :param post_data: Dict
    :return: Boolean
    """
    # Mock Data
    return True

def update_post(post_uuid):
    """
    Update a given post
    :param post_uuid: UUID
    :return: Boolean
    """
    # Mock Data
    return True

def delete_post(post_uuid):
    """
    Delete a given post
    :param post_uuid: UUID
    :return: Boolean
    """
    # Mock Data
    return True

if __name__ == "__main__":
    # Setup App
    app = Flask(__name__)
    app.config.from_object('config')
    api = Api(app)
    db = SQLAlchemy(app)
    # Setup Routes
    api.add_resource(
            Posts,
            '/v1/post',
            '/v1/post/&lt;post_uuid&gt;',
            )

    # Run the App
    app.run(host="0.0.0.0")
