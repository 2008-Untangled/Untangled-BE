import datetime
import json

import bleach
from flask import request
from flask_restful import Resource, abort
from sqlalchemy.orm.exc import NoResultFound

from api import db
from api.database.models import User, Room

def _validate_field(data, field, proceed, errors, missing_okay=False):
    if field in data:
        # sanitize the user input here
        data[field] = bleach.clean(data[field].strip())
        if len(data[field]) == 0:
            proceed = False
            errors.append(f"required '{field}' parameter is blank")
    if not missing_okay and field not in data:
        proceed = False
        errors.append(f"required '{field}' parameter is missing")
        data[field] = ''

    return proceed, data[field], errors

def _room_payload(room):
    return {
        'id': room.id,
        'name': room.name,
        'image': room.image,
        'user_id': room.user_id
    }

class RoomsResource(Resource):
    def get(self, *args, **kwargs):

        rooms = Room.query.filter(
            Room.user_id == kwargs["user_id"]
        ).all()

        results = [_room_payload(room) for room in rooms]
        return {
            'success': True,
            'data': results
        }, 200

class RoomResource(Resource):
    def get(self, *args, **kwargs):
        room_id = int(bleach.clean(kwargs['room_id'].strip()))
        room = db.session.query(Room).filter_by(id=room_id).one()

        results = _room_payload(room)
        return {
            'success': True,
            'data': results
        }, 200
