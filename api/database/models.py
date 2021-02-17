import bleach
from sqlalchemy import Column, String, Integer
from api import db


class User(db.Model):
    """
    User Model
    """
    __tablename__ = 'users'

    # Auto-incrementing, unique primary key
    id = Column(Integer, primary_key=True)
    # unique name
    name = Column(String(80), nullable=False)
    # unique email
    email = Column(String(100), unique=True, nullable=False)

    def __init__(self, name, email, user_id=None):
        if name is not None:
            name = bleach.clean(name).strip()
            if name == '':
                name = None

        if email is not None:
            email = bleach.clean(email).strip()
            if email == '':
                email = None

        self.name = name
        self.email = email
        if user_id is not None:
            self.id = user_id

    def insert(self):
        """
        inserts a new model into a database
        the model must have a unique name
        the model must have a unique id or null id
        """
        db.session.add(self)
        db.session.commit()

    def update(self):
        """
        updates a new model into a database
        the model must exist in the database
        """
        db.session.commit()

    def delete(self):
        """
        deletes model from database
        the model must exist in the database
        """
        db.session.delete(self)
        db.session.commit()
