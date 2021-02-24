import json
import unittest

from api import create_app, db
from api.database.models import User, Room
from tests import db_drop_everything, assert_payload_field_type_value, \
    assert_payload_field_type

class GetRoomTest(unittest.TestCase):
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

    def test_happypath_get_a_room(self):
      user_1 = User(name='Test User', email='email 1')
      user_1.insert()
      room_1 = Room(name='Kitchen', image='exampleimage1.com', user_id=user_1.id)
      room_1.insert()
      room_2 = Room(name='Living Room', image='exampleimage2.com', user_id=user_1.id)
      room_2.insert()

      response = self.client.get(
      f'/api/v1/rooms/{room_2.id}'
      )
      self.assertEqual(200, response.status_code)

      data = json.loads(response.data.decode('utf-8'))
      assert_payload_field_type_value(self, data, 'success', bool, True)
      
      results = data['data']
     
      assert_payload_field_type_value(
            self, results, 'name', str, room_2.name
        )
      assert_payload_field_type_value(
          self, results, 'image', str, room_2.image
      )
      assert_payload_field_type_value(
          self, results, 'user_id', int, user_1.id
      )
