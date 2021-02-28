import json
import unittest
from copy import deepcopy
from unittest.mock import patch

from api import create_app, db
from api.database.models import User, Room, Memory
from tests import db_drop_everything, assert_payload_field_type_value, \
    assert_payload_field_type


class PatchuserTest(unittest.TestCase):
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

        # adding extra padding in here to ensure we strip() it off later
        self.payload = {
            'image': 'new picture',
            'description': 'This is a different memory',
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
          f'/api/v1/rooms/{room_1.id}/memories'
        )
        results = data['data']
        first_result = results[0]
        assert_payload_field_type_value(
          self, first_result, 'image', str, 'new picture'
        )
        assert_payload_field_type_value(
          self, first_result, 'song', str, memory_1.song
        )
        assert_payload_field_type_value(
          self, first_result, 'description', str, 'This is a different memory'
        )
        assert_payload_field_type_value(
          self, first_result, 'aromas', str, memory_1.aromas
        )
        assert_payload_field_type_value(
          self, first_result, 'x', int, 200
        )
        assert_payload_field_type_value(
          self, first_result, 'y', int, 500
        )
        assert_payload_field_type_value(
          self, first_result, 'room_id', int, memory_1.room_id
        )