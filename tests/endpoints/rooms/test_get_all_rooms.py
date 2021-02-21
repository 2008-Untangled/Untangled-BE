import json
import unittest

from api import create_app, db
from api.database.models import User, Room
from tests import db_drop_everything, assert_payload_field_type_value, \
    assert_payload_field_type


class GetRoomsTest(unittest.TestCase):
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

class GetAllRoomsTest(GetRoomsTest):
  def test_happypath_get_all_rooms(self):
    user_1 = User(name='Test User', email='email 1')
    user_1.insert()
    room_1 = Room(name='Kitchen', image='exampleimage1.com', user_id=user_1.id)
    room_1.insert()
    room_2 = Room(name='Living Room', image='exampleimage2.com', user_id=user_1.id)
    room_2.insert()

    response = self.client.get(
      f'/api/v1/users/{user_1.id}/rooms'
    )
    self.assertEqual(200, response.status_code)

    data = json.loads(response.data.decode('utf-8'))
    assert_payload_field_type_value(self, data, 'success', bool, True)
    assert_payload_field_type(self, data, 'data', list)

    results = data['data']

    first_result = results[0]
    assert_payload_field_type_value(
      self, first_result, 'name', str, room_1.name
    )
    assert_payload_field_type_value(
      self, first_result, 'image', str, room_1.image
    )
    assert_payload_field_type_value(
      self, first_result, 'user_id', str, room_1.user_id
    )

    second_result = results[1]
    assert_payload_field_type_value(
      self, second_result, 'name', str, room_2.name
    )
    assert_payload_field_type_value(
      self, second_result, 'image', str, room_2.image
    )
    assert_payload_field_type_value(
      self, second_result, 'user_id', str, room_2.user_id
    )

  def test_happypath_get_empty_rooms(self):
    user_1 = User(name='Test User', email='email 1')
    user_1.insert()

    response = self.client.get(
      f'/api/v1/users/{user_1.id}/rooms'
    )

    self.assertEqual(200, response.status_code)

    data = json.loads(response.data.decode('utf-8)'))
    assert_payload_field_type_value(self, data, 'success', bool, True)
    assert_payload_field_type(self, data, 'data', list)
    self.assertEqual(0, len(data['data']))
