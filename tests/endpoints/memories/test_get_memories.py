import json
import unittest

from api import create_app, db
from api.database.models import User, Room, Memory
from tests import db_drop_everything, assert_payload_field_type_value, \
    assert_payload_field_type


class GetMemoriesTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client()

    def tearDown(self):
        db.session.remove()
        db_drop_everything(db)
        self.app_context.pop()

class GetAllMemoriesTest(GetMemoriesTest):
  def test_happypath_get_all_memories(self):
    user_1 = User(name='Test User', email='email 1')
    user_1.insert()
    room_1 = Room(name='Kitchen', image='exampleimage1.com', user_id=user_1.id)
    room_1.insert()
    memory_1 = Memory(image='Picture string', song='song url', description='This is a great memory', aromas='Roast in the oven', location='table', room_id=room_1.id)
    memory_1.insert()
    memory_2 = Memory(image='Another string', song='this song url', description='Love this memory', aromas='Chestnuts roasting', location='counter', room_id=room_1.id)
    memory_2.insert()

    response = self.client.get(
      f'/api/v1/rooms/{room_1.id}/memories'
    )
    self.assertEqual(200, response.status_code)

    data = json.loads(response.data.decode('utf-8'))
    assert_payload_field_type_value(self, data, 'success', bool, True)
    assert_payload_field_type(self, data, 'data', list)

    results = data['data']

    first_result = results[0]
    assert_payload_field_type_value(
      self, first_result, 'image', str, memory_1.image
    )
    assert_payload_field_type_value(
      self, first_result, 'song', str, memory_1.song
    )
    assert_payload_field_type_value(
      self, first_result, 'description', str, memory_1.description
    )
    assert_payload_field_type_value(
      self, first_result, 'aromas', str, memory_1.aromas
    )
    assert_payload_field_type_value(
      self, first_result, 'location', str, memory_1.location
    )
    assert_payload_field_type_value(
      self, first_result, 'room_id', int, memory_1.room_id
    )

    second_result = results[1]
    assert_payload_field_type_value(
      self, second_result, 'image', str, memory_2.image
    )
    assert_payload_field_type_value(
      self, second_result, 'song', str, memory_2.song
    )
    assert_payload_field_type_value(
      self, second_result, 'description', str, memory_2.description
    )
    assert_payload_field_type_value(
      self, second_result, 'aromas', str, memory_2.aromas
    )
    assert_payload_field_type_value(
      self, second_result, 'location', str, memory_2.location
    )
    assert_payload_field_type_value(
      self, second_result, 'room_id', int, memory_2.room_id
    )

  def test_happypath_get_empty_rooms(self):
    user_1 = User(name='Test User', email='email 1')
    user_1.insert()
    room_1 = Room(name='Kitchen', image='exampleimage1.com', user_id=user_1.id)
    room_1.insert()

    response = self.client.get(
      f'/api/v1/rooms/{room_1.id}/memories'
    )
    self.assertEqual(200, response.status_code)

    data = json.loads(response.data.decode('utf-8)'))
    assert_payload_field_type_value(self, data, 'success', bool, True)
    assert_payload_field_type(self, data, 'data', list)
    self.assertEqual(0, len(data['data']))
