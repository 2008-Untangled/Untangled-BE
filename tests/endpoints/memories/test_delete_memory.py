import json
import unittest
from copy import deepcopy
from unittest.mock import patch

from api import create_app, db
from api.database.models import User, Room, Memory
from tests import db_drop_everything, assert_payload_field_type_value, \
    assert_payload_field_type

class DeletememoryTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client()

        self.user_1 = User(name='Test User', email='email 2')
        self.user_1.insert()
        self.room_1 = Room(name='Kitchen', image='exampleimage1.com', user_id=self.user_1.id)
        self.room_1.insert()
        self.memory_1 = Memory(image='Picture string', song='song url', description='This is a great memory', aromas='Roast in the oven', x = 123, y = 456, room_id=self.room_1.id)
        self.memory_1.insert()

    def tearDown(self):
        db.session.remove()
        db_drop_everything(db)
        self.app_context.pop()

    def test_happypath_delete_a_memory(self):
        response = self.client.delete(
            f'/api/v1/memories/{self.memory_1.id}'
        )
        self.assertEqual(204, response.status_code)
        self.assertEqual('', response.data.decode('utf-8'))

        # ensure it's really gone by getting a 404 if we try to fetch it again
        response = self.client.get(
            f'/api/v1/memories/{self.memory_1.id}'
        )
        self.assertEqual(404, response.status_code)

    def test_sadpath_delete_bad_id_memory(self):
        response = self.client.delete(
            f'/api/v1/memories/9999999'
        )
        self.assertEqual(404, response.status_code)

        data = json.loads(response.data.decode('utf-8'))
        assert_payload_field_type_value(self, data, 'error', int, 404)
        assert_payload_field_type_value(self, data, 'success', bool, False)
        assert_payload_field_type_value(
            self, data, 'message', str, 'resource not found'
        )