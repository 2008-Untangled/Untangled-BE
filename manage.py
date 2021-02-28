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
    room_3 = db.session.query(Room).filter_by(id=3).one()
    room_4 = db.session.query(Room).filter_by(id=4).one()

    memory_1 = Memory(image='https://itdoesnttastelikechicken.com/wp-content/uploads/2017/05/super-moist-vegan-banana-nut-muffins-easy-dairy-free-facebook.jpg’', song='https://open.spotify.com/album/3mGmn1JDde3XyKQqZTJUAL?highlight=spotify:track:4QxDOjgpYtQDxxbWPuEJOy', description='Your mothers secret recipe for those banana nut muffins', aromas='Crisp winter air, hot cocoa, fresh baked banana bread', x = 500, y = 550, room_id=room_1.id)
    memory_2 = Memory(image='https://merriam-webster.com/assets/mw/images/article/art-wap-landing-mp-lg/family-of-four-7101-a234e9249b2c7223d4e4d8cd9432f9e9@1x.jpg', song='https://open.spotify.com/album/3alZBOvPaK3hgMEEymw4Yr?highlight=spotify:track:0mHyWYXmmCB9iQyK18m3FQ', description='Babysittng your grandchildren every Sunday', aromas='Baby powder, diapers, fresh peaches', x = 209, y = 379, room_id=room_1.id)
    memory_3 = Memory(image='https://cdn.images.express.co.uk/img/dynamic/41/590x/monopoly-gamer-board-games-reboot-super-mario-nintendo-823505.jpg', song='https://open.spotify.com/album/6mmv0gwumlFGWDGJXF4yEv?highlight=spotify:track:29U7stRjqHU6rMiS8BfaI9', description='Playing monopoly and drinking lemonade', aromas='Lemons, fresh cut roses', x = 677, y = 785, room_id=room_1.id)

    memory_4 = Memory(image='https://i.pinimg.com/236x/3e/81/2f/3e812f93fc028189d5b2b761e164ff6a--a-christmas-story-christmas-morning.jpg', song='https://open.spotify.com/track/2yPoRJvPqwpbGLJPRikrZW?si=13b08af526f24414', description='Christmas morning when Ralphie got the Red Rider he wanted so badly', aromas='Fresh pine, torn paper, coffee', x = 414, y = 346, room_id=room_2.id)
    memory_5 = Memory(image='https://static01.nyt.com/images/2016/09/12/watching/12watching1/12watching1-superJumbo-v2.jpg', song='https://open.spotify.com/track/3MXfueQqoiF93unHCQZos2?si=a274b3b4699741f2', description='Mike, Lucas, and Will playing Dungeons and Dragons while having a sleep over', aromas='Mac n cheese, stinky shoes', x = 224, y = 756, room_id=room_2.id)
    memory_6 = Memory(image='https://i1.wp.com/highdefdiscnews.com/wp-content/uploads/2018/10/the_great_outdoors_11.png?ssl=1', song='https://open.spotify.com/track/7demHL0GXA6YmTNqw3Btz8?si=1c2afaeb41a14a8b', description='One of the best camping trips with the family', aromas='Campfire, pine trees, old cabin', x = 570, y = 714, room_id=room_2.id)

    memory_7 = Memory(image='https://c1.staticflickr.com/9/8452/7984891423_309149ea12_b.jpg', song='https://open.spotify.com/album/77spqXa3VNN0mw13PgWWyY?highlight=spotify:track:6n6OQfBpCgzF9oEg8zhBN7', description='Playing with my grandkids in the backyard', aromas='Freshly mowed grass', x = 602, y = 831, room_id=room_3.id)
    memory_8 = Memory(image='https://wpcluster.dctdigital.com/sundaypost/wp-content/uploads/sites/13/2017/08/JE0165_royalty-free-image_family-BBQ-smartbrush_AW2_060217-1024x683.jpg', song='https://open.spotify.com/album/4sSXylKcBB3p47VfrBJlfK?highlight=spotify:track:1LM5zQv5pBKPyO7rm7Uz6U', description='Family BBQs after church on Sundays', aromas='grill smoke', x = 530, y = 463, room_id=room_3.id)
    memory_9 = Memory(image='https://cdn.images.dailystar.co.uk/dynamic/1/photos/551000/620x/Young-girl-flying-a-kite-682596.jpg', song='https://open.spotify.com/album/3usnShwygMXVZB4IV5dwnU?highlight=spotify:track:2RlgNHKcydI9sayD2Df2xp', description='Teaching the kids how to fly kites', aromas='Sunshine on the skin', x = 200, y = 831, room_id=room_3.id)

    memory_10 = Memory(image='https://amz.netweather.tv/monthly_09_2015/post-2611-0-09582700-1442308742.jpg', song='https://open.spotify.com/album/1CsuCA05y9r7ftG9bGGtWV?highlight=spotify:track:3m167vBQI5YLK0a1m6L6Y1', description='The blizzard where the whole neighborhood came together and dug out the driveway', aromas='Crisp winter air, hot cocoa, bacon and eggs for breakfast', x = 510, y = 422, room_id=room_4.id)
    memory_11 = Memory(image='https://flashbak.com/wp-content/uploads/2017/09/078_1967-1026x1024.jpg', song='https://open.spotify.com/album/6lPb7Eoon6QPbscWbMsk6a?highlight=spotify:track:4uGIJG1jYFonGc4LGp5uQL', description='Dancing at Lindas garden party', aromas='Fruit punch, aftershave, honeysuckle', x = 315, y = 647, room_id=room_4.id)
    memory_12 = Memory(image='https://groovyhistory.com/content/124227/f0e9bedffd72ead0c2b92d96674be472.jpg', song='https://open.spotify.com/album/5Qcef60m4gcckV24PmPYVq?highlight=spotify:track:2rUHBIfbMBB92n1gSfSqwF', description='Tailgating outside Madison Square Garden waiting to see Bruce Springsteen in concert', aromas='Net hairspray, beer, hot pavement', x = 119, y = 377, room_id=room_4.id)

    db.session.add(memory_1)
    db.session.add(memory_2)
    db.session.add(memory_3)
    db.session.add(memory_4)
    db.session.add(memory_5)
    db.session.add(memory_6)
    db.session.add(memory_7)
    db.session.add(memory_8)
    db.session.add(memory_9)
    db.session.add(memory_10)
    db.session.add(memory_11)
    db.session.add(memory_12)

    db.session.commit()
    print(f'obj count: {len(db.session.query(User).all())}')
    print(f'obj count: {len(db.session.query(Room).all())}')
    print(f'obj count: {len(db.session.query(Memory).all())}')


if __name__ == "__main__":
    manager.run()
