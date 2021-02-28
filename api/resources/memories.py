import datetime
import json

import bleach
from flask import request
from flask_restful import Resource, abort
from sqlalchemy.orm.exc import NoResultFound

from api import db
from api.database.models import User, Room, Memory

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

def _memory_payload(memory):
    return {
        'id': memory.id,
        'image': memory.image,
        'song': memory.song,
        'description': memory.description,
        'aromas': memory.aromas,
        'x': memory.x,
        'y': memory.y,
        'room_id': memory.room_id
    }

class MemoriesResource(Resource):
    def get(self, *args, **kwargs):

        memories = Memory.query.filter(
            Memory.room_id == kwargs["room_id"]
        ).all()

        results = [_memory_payload(memory) for memory in memories]
        return {
            'success': True,
            'data': results
        }, 200
