import json
import unittest
from copy import deepcopy
from unittest.mock import patch

from api import create_app, db
from api.database.models import User, Room, Memory
from tests import db_drop_everything, assert_payload_field_type_value, \
    assert_payload_field_type


class PatchmemoryTest(unittest.TestCase):
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

        self.payload = {
            'image': 'new_image',
            'description': 'new_description',
            'x': 200,
            'y': 500
        }

    def tearDown(self):
        db.session.remove()
        db_drop_everything(db)
        self.app_context.pop()

    def test_happypath_patch_a_memory(self):
        payload = deepcopy(self.payload)

        response = self.client.patch(
            f'/api/v1/memories/{self.memory_1.id}',
            json=payload,
            content_type='application/json'
        )
        self.assertEqual(200, response.status_code)

        data = json.loads(response.data.decode('utf-8'))
        assert_payload_field_type_value(self, data, 'success', bool, True)

        assert_payload_field_type_value(
            self, data, 'image', str, payload['image'].strip()
        )
        assert_payload_field_type_value(
            self, data, 'description', str, payload['description'].strip()
        )

        # Fetching that memory and checking if it is updated
        response = self.client.get(
          f'/api/v1/rooms/{self.room_1.id}/memories'
        )

        assert_payload_field_type_value(
          self, data, 'image', str, 'new_image'
        )
        assert_payload_field_type_value(
          self, data, 'song', str, self.memory_1.song
        )
        assert_payload_field_type_value(
          self, data, 'description', str, 'new_description'
        )
        assert_payload_field_type_value(
          self, data, 'aromas', str, self.memory_1.aromas
        )
        assert_payload_field_type_value(
          self, data, 'x', int, 200
        )
        assert_payload_field_type_value(
          self, data, 'y', int, 500
        )
        assert_payload_field_type_value(
          self, data, 'room_id', int, self.memory_1.room_id
        )

    def test_sadpath_patch_user_bad_id(self):
        response = self.client.patch(
            f'/api/v1/memories/999999'
        )
        self.assertEqual(404, response.status_code)

        data = json.loads(response.data.decode('utf-8'))
        assert_payload_field_type_value(self, data, 'error', int, 404)
        assert_payload_field_type_value(self, data, 'success', bool, False)
        assert_payload_field_type_value(
            self, data, 'message', str, 'resource not found'
        )