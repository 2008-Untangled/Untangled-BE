from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from api import create_app, db
from api.database.models import User, Room, Memory
from tests import db_drop_everything

app = create_app()
migrate = Migrate(app, db)
manager = Manager(app)

# manage migrations
manager.add_command('db', MigrateCommand)


@manager.command
def routes():
    print(app.url_map)


@manager.command
def db_seed():
    db_drop_everything(db)
    db.create_all()

    # seed anything here we might need
    user = User(name='iandouglas', email='ian.douglas@iandouglas.com')
    db.session.add(user)

    user = db.session.query(User).filter_by(id=1).one()
    room_1 = Room(name='Kitchen', image='https://user-images.githubusercontent.com/65255478/109369416-81cc3b80-7859-11eb-8bc6-f4647040555a.png', user_id=user.id)
    room_2 = Room(name='Living Room', image='https://user-images.githubusercontent.com/65255478/109369440-901a5780-7859-11eb-83e9-350d3f3494ec.png', user_id=user.id)
    room_3 = Room(name='Backyard', image='https://user-images.githubusercontent.com/65255478/109369423-87c21c80-7859-11eb-8559-43a0cf43e9a9.png', user_id=user.id)
    room_4 = Room(name='Bedroom', image='https://user-images.githubusercontent.com/65255478/109369427-8a247680-7859-11eb-9330-b282ea6b4907.png', user_id=user.id)
    db.session.add(room_1)
    db.session.add(room_2)
    db.session.add(room_3)
    db.session.add(room_4)

    room_1 = db.session.query(Room).filter_by(id=1).one()
    room_2 = db.session.query(Room).filter_by(id=2).one()

    memory_1 = Memory(image='https://merriam-webster.com/assets/mw/images/article/art-wap-landing-mp-lg/family-of-four-7101-a234e9249b2c7223d4e4d8cd9432f9e9@1x.jpg', song='https://open.spotify.com/track/5IKLwqBQG6KU6MP2zP80Nu?si=OTIOYPYbRV-10u_9xKKOiw', description='This is a great memory', aromas='Roast in the oven', location='table', room_id=room_1.id)
    memory_2 = Memory(image='https://d1urgxgdb4lky3.cloudfront.net/wp-content/uploads/2020/05/191115-Cookie-Jar-Jennifer-SC-022copy.jpg', song='https://open.spotify.com/track/0bYg9bo50gSsH3LtXe2SQn?si=Srv8kAEbSuCa6iFGsGbKIA', description='Such great times', aromas='Fresh baked cookies', location='oven', room_id=room_1.id)
    memory_3 = Memory(image='https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/fireplace-with-fire-burning-royalty-free-image-75406522-1541632053.jpg', song='https://open.spotify.com/track/04KTF78FFg8sOHC1BADqbY?si=j7yqoZdST4-AKvUVTzKRig', description='So many laughs', aromas='Fire', location='hearth', room_id=room_2.id)
    memory_4 = Memory(image='https://media-api.xogrp.com/images/7dddc30f-813b-4caf-9da8-ad33e96fc697', song='', description='Day of our wedding', aromas='', location='picture frame', room_id=room_2.id)
    db.session.add(memory_1)
    db.session.add(memory_2)
    db.session.add(memory_3)
    db.session.add(memory_4)

    db.session.commit()
    print(f'obj count: {len(db.session.query(User).all())}')
    print(f'obj count: {len(db.session.query(Room).all())}')
    print(f'obj count: {len(db.session.query(Memory).all())}')


if __name__ == "__main__":
    manager.run()
