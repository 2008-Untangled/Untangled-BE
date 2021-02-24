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

        self.user_1 = User(name='zzz 1', email='e1')
        self.user_1.insert()

    def tearDown(self):
        db.session.remove()
        db_drop_everything(db)
        self.app_context.pop()

    def test_happypath_get_a_user(self):