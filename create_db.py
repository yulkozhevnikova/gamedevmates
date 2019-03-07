
import sqlite3


conn = sqlite3.connect('app.db')

c = conn.cursor()

c.execute('''DROP TABLE users''')

c.execute('''
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    specialization TEXT,
    gamedevexp TEXT
)
''')


conn.commit()


c.execute('''
    ALTER TABLE users 
    ADD COLUMN login TEXT
''')


conn.commit()

c.execute('''
    ALTER TABLE users 
    ADD COLUMN photo TEXT
''')
conn.commit()

c.execute('''
    UPDATE users
    SET login="vlad"
    WHERE name='Volodya Smirnov'
''')
conn.commit()


users =[
    {'id': '1',
     'login': 'Vas',
     'name': 'Vasiliy',
     'specialization': 'Designer',
     'gamedevexp': '3',
     'photo': 'https://img.muz1.tv/img/2017-02-20/fmt_94_24_prof6.jpg'
     },
{'id': '2',
'login': 'jimbo',
'name': 'Roman Vlasov',
'specialization': 'Composer',
'gamedevexp': '2',
'photo': 'http://lichnosti.net/photos/479/13182635972.jpg'
},
{'id': '3',
'login': 'Yoko',
'name': 'Yoko Kanno',
'specialization': 'Composer',
'gamedevexp': '10',
'photo': 'http://4.bp.blogspot.com/-2MV2IW4RiKQ/VVezEyoskZI/AAAAAAABg2Y/jXMJ7_d7xDE/s1600/Yoko%2BOno%2C%2B1960s%2B(10).jpg'
},
{'id': '4',
'login': 'Vash',
'name': 'Vash Stampede',
'specialization': 'Tester',
'gamedevexp': '4',
'photo': 'https://www.buro247.ru/images/mick_jagger_70.jpg'
},
{'id': '5',
'login': 'rogue',
'name': 'Viktor Efremov',
'specialization': 'Composer',
'gamedevexp': '2',
'photo': 'https://24smi.org/public/media/celebrity/2017/01/28/FnUiB4hRlVpN_viktor-tsoi.jpg'
},
{'id': '6',
'login': 'jezz',
'name': 'Elena Vlasova',
'specialization': 'Designer',
'gamedevexp': '0',
'photo': 'https://sobesednik.ru/storage/posts/March2018/MxTNdbpM1ccWdY4MK035.jpg'
},
{'id': '7',
'login': 'belli',
'name': 'Lester Nygaard',
'specialization': 'Programmer',
'gamedevexp': '2',
'photo': 'https://flashbak.com/wp-content/uploads/2017/08/david-bowie-unseen-9.jpg'
},
{'id': '8',
'login': 'cody',
'name': 'Ivan Melnikov',
'specialization': 'Programmer',
'gamedevexp': '4',
'photo': 'http://fangid.com/media/filer_public/c6/40/c64071b2-b0f3-48cd-8540-99cdafb9041b/7434692.jpg'
},
{'id': '9',
'login': 'Reg',
'name': 'Vadim Litvinov',
'specialization': 'Manager',
'gamedevexp': '3',
'photo': 'https://c-ash.smule.com/sf/s53/arr/b3/02/eabfbb8e-ce65-4b61-bbb2-f99351755fad_1024.jpg'
},
{'id': '10',
'login': 'lizza',
'name': 'Elizaveta Karpina',
'specialization': 'Programmer',
'gamedevexp': '5',
'photo': 'http://skuky.net/wp-content/uploads/2018/06/monet1.jpg'
},
{'id': '11',
'login': 'on4k',
'name': 'John Doe',
'specialization': 'Designer',
'gamedevexp': '7',
'photo': 'http://images5.fanpop.com/image/photos/26500000/Rum-Diary-Premiere-London-johnny-depp-26527663-1681-2500.jpg'
},
{'id': '12',
'login': 'Flar',
'name': 'Philipp Rogers',
'specialization': 'Composer',
'gamedevexp': '0',
'photo': 'https://biletkartina.tv/files/activities/baskov_1.jpg'
},
{'id': '13',
'login': 'ANTOXA',
'name': 'Anton Antonov',
'specialization': 'Tester',
'gamedevexp': '0',
'photo': 'https://tntmusic.ru/media/content/article/2018-05-10_14-47-48__1b912552-5461-11e8-ae16-0d60569bb5a5.jpg'
},
{'id': '14',
'login': 'Ana',
'name': 'Anna Fedorova',
'specialization': 'Programmer',
'gamedevexp': '3',
'photo': 'http://g-l-a-m.ru/wp-content/uploads/2016/01/Anne-Hathaway-Keer-David-Slijper-3.jpg'
},
{'id': '15',
'login': 'sarah',
'name': 'Sarah Andersen',
'specialization': 'Designer',
'gamedevexp': '0',
'photo': 'https://www.kino-teatr.ru/news/9514/94020.jpg'
},
{'id': '16',
'login': 'kold',
'name': 'Kolin Nicolson',
'specialization': 'Programmer',
'gamedevexp': '6',
'photo': 'http://www.peoples.ru/art/cinema/actor/firth/firth_200708241843541jpg'
},
{'id': '17',
'login': 'jk',
'name': 'John Konor',
'specialization': 'Tester',
'gamedevexp': '2',
'photo': 'https://movies2535.files.wordpress.com/2016/03/eddie-furlong-as-john-connor-in-terminator-2.jpg'
},
{'id': '18',
'login': 'kim',
'name': 'Mia Sendler',
'specialization': '3D-Designer',
'gamedevexp': '3',
'photo': 'https://1.bp.blogspot.com/-f8VtXvejY2c/VBBG5FKhkPI/AAAAAAADE3s/Xo0acsTpPG0/s840/Milla_Jovovich-Marella_Art_365-2014-003.jpg'
},
{'id': '19',
'login': 'stepa',
'name': 'Stepan Smirnov',
'specialization': 'Sound-Designer',
'gamedevexp': '3',
'photo': 'https://24smi.org/public/media/resize/660x-/celebrity/2017/06/29/hQVKf4mSQ790_ivan-urgant.jpg'
},
{'id': '20',
'login': 'Arni',
'name': 'Arnold Layne',
'specialization': 'Programmer',
'gamedevexp': '0',
'photo': 'http://games-of-thrones.ru/sites/default/files/pictures/all/Arnold%20Schwarzenegger/2.jpg'
}
]



for user in users:
    c.execute("INSERT INTO users "
              "('id', 'login', 'name', 'gamedevexp', 'specialization', 'photo')"
              "VALUES "
              "('{id}', '{login}','{name}','{gamedevexp}','{specialization}', '{photo}')".format(**user))
    conn.commit()


c.execute('''DROP TABLE room_information''')



c.execute('''
CREATE TABLE room_information (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          room_name TEXT,
          positions_required TEXT,
          admin_name TEXT
)
''')
conn.commit()


room_information = [
    {'id': '1',
     'room_name': 'CS',
     'positions_required': 'Tester',
     'admin_name': 'kolyan'
     }

]

for room_info in room_information:
    c.execute("INSERT INTO room_information "
              "('id', 'room_name', 'positions_required', 'admin_name')"
              "VALUES "
              "('{id}','{room_name}','{positions_required}','{admin_name}')".format(**room_info))
    conn.commit()

c.execute('''
    INSERT INTO room_information (id, room_name, positions_required, admin_name)
    VALUES
    (2, "Best Game Ever", "Tester, Designer, Programmer" , "Vas"),
    (3, "Worst Game Ever", "Composer, Programmer" , "sarah"),
    (4, "Just a Game", "Programmer, Manager" , "lizza"),
    (5, "Test Game", "Programmer, Programmer", "jesus")
''')
conn.commit()



conn.close()