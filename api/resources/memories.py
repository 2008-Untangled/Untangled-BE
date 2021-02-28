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

class MemoryResource(Resource):
    def patch(self, *args, **kwargs):
        memory_id = int(bleach.clean(kwargs['memory_id'].strip()))
        memory = None
        try: memory = db.session.query(Memory).filter_by(id=memory_id).one()
        except NoResultFound:
            return abort(404)

        preceed = True
        errors = []
        data = json.loads(request.data)
        proceed, description, errors = _validate_field(
            data, 'description', preceed, errors, missing_okay=True)
        proceed, image, errors = _validate_field(
            data, 'image', preceed, errors, missing_okay=True)
        proceed, song, errors = _validate_field(
            data, 'song', preceed, errors, missing_okay=True)
        proceed, aromas, errors = _validate_field(
            data, 'aromas', preceed, errors, missing_okay=True)
        proceed, x, errors = _validate_field(
            data, 'x', preceed, errors, missing_okay=True)
        proceed, y, errors = _validate_field(
            data, 'y', preceed, errors, missing_okay=True)

        if not preceed:
            return {
                'success': False,
                'error': 400,
                'errors': errors
            }, 400

        if description:
            memory.description = description
        if image:
            memory.image = description
        if song:
            memory.song = description
        if aromas:
            memory.aromas = description
        if x:
            memory.x = description
        if y:
            memory.y = description
        memory.update()

        memory_payload = _memory_payload(memory)
        memory_payload['success'] = True
        return memory_payload, 200
