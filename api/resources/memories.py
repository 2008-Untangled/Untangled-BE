import datetime
import json

import bleach
from flask import request
from flask_restful import Resource, abort
from sqlalchemy.orm.exc import NoResultFound

from api import db
from api.database.models import User, Room, Memory

def _validate_field(data, field, proceed, errors, memory, missing_okay=False):
    if field in data and type(data[field]) is str:
        # sanitize the user input here
        data[field] = bleach.clean(data[field].strip())
        if len(data[field]) == 0:
            proceed = False
            errors.append(f"required '{field}' parameter is blank")
    if not missing_okay and field not in data:
        proceed = False
        errors.append(f"required '{field}' parameter is missing")
        data[field] = ''
    if missing_okay and field not in data:
        data[field] = getattr(memory, field)

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
    def get(self, *args, **kwargs):
        memory_id = int(bleach.clean(kwargs['memory_id'].strip()))
        memory = None
        try:
            memory = db.session.query(Memory).filter_by(id=memory_id).one()
        except NoResultFound:
            return abort(404)

        user_payload = _user_payload(memory)
        user_payload['success'] = True
        return user_payload, 200

    def patch(self, *args, **kwargs):
        memory_id = int(bleach.clean(kwargs['memory_id'].strip()))
        memory = None
        try: memory = db.session.query(Memory).filter_by(id=memory_id).one()
        except NoResultFound:
            return abort(404)

        proceed = True
        errors = []
        data = json.loads(request.data)
        proceed, image, errors = _validate_field(
            data, 'image', proceed, errors, memory, missing_okay=True)
        proceed, song, errors = _validate_field(
            data, 'song', proceed, errors, memory, missing_okay=True)
        proceed, description, errors = _validate_field(
            data, 'description', proceed, errors, memory, missing_okay=True)
        proceed, aromas, errors = _validate_field(
            data, 'aromas', proceed, errors, memory, missing_okay=True)
        proceed, x, errors = _validate_field(
            data, 'x', proceed, errors, memory, missing_okay=True)
        proceed, y, errors = _validate_field(
            data, 'y', proceed, errors, memory, missing_okay=True)

        if not proceed:
            return {
                'success': False,
                'error': 400,
                'errors': errors
            }, 400

        if description:
            memory.description = description
        if image:
            memory.image = image
        if song:
            memory.song = song
        if aromas:
            memory.aromas = aromas
        if x:
            memory.x = x
        if y:
            memory.y = y
        memory.update()

        memory_payload = _memory_payload(memory)
        memory_payload['success'] = True
        return memory_payload, 200

    def delete(self, *args, **kwargs):
        memory_id = kwargs['memory_id']
        memory = None
        try:
            memory = db.session.query(Memory).filter_by(id=memory_id).one()
        except NoResultFound:
            return abort(404)

        memory.delete()
        return {}, 204