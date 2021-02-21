import unittest
from sqlalchemy.exc import IntegrityError

from api import create_app, db
from api.database.models import Room


class AppTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_user_model(self):
        user = User(name='ian', email='ian.douglas@iandouglas.com')
        user.insert()
        room = Room(name='Kitchen', image='exampleimage1.com', user_id=user.id)
        room.insert()

        self.assertIsInstance(room, Room)
        self.assertIsNotNone(room.id)
        self.assertEqual('Kitchen', room.name)
        self.assertEqual('exampleimage1.com', room.image)
        self.assertEqual(user.id, room.user_id)