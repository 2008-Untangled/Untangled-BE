import json
import unittest
from copy import deepcopy
from unittest.mock import patch

from api import create_app, db
from api.database.models import User, Room, Memory
from tests import db_drop_everything, assert_payload_field_type_value, \
    assert_payload_field_type

class CreatememoryTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client()

        self.user_1 = User(name='Test User 2', email='email 3')
        self.user_1.insert()
        self.room_1 = Room(name='Kitchen', image='exampleimage1.com', user_id=self.user_1.id)
        self.room_1.insert()
        self.payload = {
            'image': 'new_image',
            'song': 'new_song',
            'description': 'This is a new description',
            'aromas': 'new_aroma',
            'x': 500,
            'y': 600
        }

    def tearDown(self):
        db.session.remove()
        db_drop_everything(db)
        self.app_context.pop()

    def test_happypath_create_memory(self):
        payload = deepcopy(self.payload)

        response = self.client.post(
            f'/api/v1/rooms/{self.room_1.id}/memories', json=payload,
            content_type='application/json'
        )
        self.assertEqual(201, response.status_code)

        data = json.loads(response.data.decode('utf-8'))
        assert_payload_field_type_value(self, data, 'success', bool, True)

        assert_payload_field_type(self, data, 'id', int)
        memory_id = data['id']
        assert_payload_field_type_value(
            self, data, 'image', str, payload['image'].strip()
        )
        assert_payload_field_type_value(
            self, data, 'song', str, payload['song'].strip()
        )
        assert_payload_field_type_value(
            self, data, 'description', str, payload['description'].strip()
        )
        assert_payload_field_type_value(
            self, data, 'aromas', str, payload['aromas'].strip()
        )
        assert_payload_field_type_value(
            self, data, 'x', int, payload['x']
        )
        assert_payload_field_type_value(
            self, data, 'y', int, payload['y']
        )