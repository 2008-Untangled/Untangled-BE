import unittest
from sqlalchemy.exc import IntegrityError

from api import create_app, db
from api.database.models import User, Room, Memory


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

    def test_memory_model(self):
        user = User(name='ian', email='ian.douglas@iandouglas.com')
        user.insert()
        room = Room(name='Kitchen', image='exampleimage1.com', user_id=user.id)
        room.insert()
        memory = Memory(image='Picture string', song='song url', description='This is a great memory', aromas='Roast in the oven', room_id=room.id, x = 414, y = 346)
        memory.insert()

        self.assertIsInstance(memory, Memory)
        self.assertIsNotNone(memory.id)
        self.assertEqual('Picture string', memory.image)
        self.assertEqual('song url', memory.song)
        self.assertEqual('This is a great memory', memory.description)
        self.assertEqual('Roast in the oven', memory.aromas)
        self.assertEqual(414, memory.x)
        self.assertEqual(346, memory.y)
        self.assertEqual(room.id, memory.room_id)
