"""
Basic unit tests for Sample App
running in a Docker environment
"""
import json
import requests
import unittest2 as unittest

from pymongo import MongoClient


class ApiTest(unittest.TestCase):

    api_url = 'http://localhost:5000/v1/'

    def cleanup(self):
        msg_ids = [0,1]
        for msg_id in msg_ids:
            url = self.api_url + 'message/' + str(msg_id)
            response = requests.delete(url)

    def test_create_messages(self):
        # setup test messages
        self.cleanup()
        url = self.api_url + 'message'
        response = requests.post(url)
        self.assertEquals(response.status_code, 200)

    def test_get_message(self):
        message = 1
        url = self.api_url + 'message/' + str(message)
        response = requests.get(url)
        data = response.json()
        self.assertEquals(data['_id'], 1)

    def test_get_all_messages(self):
        message = 0
        url = self.api_url + 'message/' + str(message)
        response = requests.get(url)
        data = response.json()
        self.assertIsInstance(data[0]['_id'], int)

    def test_update_message(self):
        message = 1
        url = self.api_url + 'message/' + str(message)
        response = requests.put(url)
        data = response.json()
        self.assertEquals(data['status'], 200)

    def test_delete_message(self):
        pass

    def test_auth(self):
        pass

    def test_auth_logout(self):
        pass

    def test_auth_refresh(self):
        pass

    def test_get_notification(self):
        pass

    def test_update_notification(self):
        pass

    def test_delete_notification(self):
        pass

    def test_send_notification(self):
        pass
