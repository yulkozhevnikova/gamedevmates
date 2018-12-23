# Import sqlite3 module (in standart library - do not need to install)
import sqlite3

# Connect ot Database - in local file app.db
conn = sqlite3.connect('app.db')
# Create a cursor - a
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




# Our base data
users = [
    {'id': '1',
     'login': 'Vas',
     'name': 'Vasiliy',
     'specialization': 'Designer',
     'gamedevexp': '3',
     'photo': 'http://dic.academic.ru/pictures/wiki/files/79/Official_portrait_of_Barack_Obama.jpg'
     },
    {'id': '2',
     'login': 'jimbo',
     'name': 'Roman Vlasov',
     'specialization': 'Composer',
     'gamedevexp': '2',
     'photo': 'http://b.vimeocdn.com/ts/173/794/173794976_640.jpg'
     },
    {'id': '3',
     'login': 'Yoko',
     'name': 'Yoko Kanno',
     'specialization': 'Composer',
     'gamedevexp': '10',
     'photo': 'http://b.vimeocdn.com/ts/173/794/173794976_640.jpg'
     },
    {'id': '4',
     'login': 'Vash',
     'name': 'Vash Stampede',
     'specialization': 'Tester',
     'gamedevexp': '4',
     'photo': 'http://b.vimeocdn.com/ts/173/794/173794976_640.jpg'
     },
    {'id': '5',
     'login': 'rogue',
     'name': 'Viktor Efremov',
     'specialization': 'Composer',
     'gamedevexp': '2',
     'photo': 'http://b.vimeocdn.com/ts/173/794/173794976_640.jpg'
     },
    {'id': '6',
     'login': 'jezz',
     'name': 'Elena Vlasova',
     'specialization': 'Designer',
     'gamedevexp': '0',
     'photo': 'http://b.vimeocdn.com/ts/173/794/173794976_640.jpg'
     },
    {'id': '7',
     'login': 'belli',
     'name': 'Lester Nygaard',
     'specialization': 'Programmer',
     'gamedevexp': '2',
     'photo': 'http://b.vimeocdn.com/ts/173/794/173794976_640.jpg'
     },
    {'id': '8',
     'login': 'cody',
     'name': 'Ivan Melnikov',
     'specialization': 'Programmer',
     'gamedevexp': '4',
     'photo': 'http://b.vimeocdn.com/ts/173/794/173794976_640.jpg'
     },
    {'id': '9',
     'login': 'Reg',
     'name': 'Vadim Litvinov',
     'specialization': 'Manager',
     'gamedevexp': '3',
     'photo': 'http://b.vimeocdn.com/ts/173/794/173794976_640.jpg'
     },
    {'id': '10',
     'login': 'lizza',
     'name': 'Elizaveta Karpina',
     'specialization': 'Programmer',
     'gamedevexp': '5',
     'photo': 'http://b.vimeocdn.com/ts/173/794/173794976_640.jpg'
     },
    {'id': '11',
     'login': 'on4k',
     'name': 'John Doe',
     'specialization': 'Designer',
     'gamedevexp': '7',
     'photo': 'http://b.vimeocdn.com/ts/173/794/173794976_640.jpg'
     },
    {'id': '12',
     'login': 'Flar',
     'name': 'Philipp Rogers',
     'specialization': 'Composer',
     'gamedevexp': '0',
     'photo': 'http://b.vimeocdn.com/ts/173/794/173794976_640.jpg'
     },
    {'id': '13',
     'login': 'ANTOXA',
     'name': 'Anton Antonov',
     'specialization': 'Tester',
     'gamedevexp': '0',
     'photo': 'http://b.vimeocdn.com/ts/173/794/173794976_640.jpg'
     },
    {'id': '14',
     'login': 'Ana',
     'name': 'Anna Fedorova',
     'specialization': 'Programmer',
     'gamedevexp': '3',
     'photo': 'http://b.vimeocdn.com/ts/173/794/173794976_640.jpg'
     },
    {'id': '15',
     'login': 'sarah',
     'name': 'Sarah Andersen',
     'specialization': 'Designer',
     'gamedevexp': '0',
     'photo': 'http://b.vimeocdn.com/ts/173/794/173794976_640.jpg'
     },
    {'id': '16',
     'login': 'kold',
     'name': 'Kolin Nicolson',
     'specialization': 'Programmer',
     'gamedevexp': '6',
     'photo': 'http://b.vimeocdn.com/ts/173/794/173794976_640.jpg'
     },
    {'id': '17',
     'login': 'jk',
     'name': 'John Konor',
     'specialization': 'Tester',
     'gamedevexp': '2',
     'photo': 'http://b.vimeocdn.com/ts/173/794/173794976_640.jpg'
     },
    {'id': '18',
     'login': 'kim',
     'name': 'Mia Sendler',
     'specialization': '3D-Designer',
     'gamedevexp': '3',
     'photo': 'http://b.vimeocdn.com/ts/173/794/173794976_640.jpg'
     },
    {'id': '19',
     'login': 'stepa',
     'name': 'Stepan Smirnov',
     'specialization': 'Sound-Designer',
     'gamedevexp': '3',
     'photo': 'http://b.vimeocdn.com/ts/173/794/173794976_640.jpg'
     },
    {'id': '20',
    'login': 'Arni',
    'name': 'Arnold Layne',
    'specialization': 'Programmer',
    'gamedevexp': '0',
    'photo': 'http://b.vimeocdn.com/ts/173/794/173794976_640.jpg'
    }
       ]
# Adding it in the loop
for user in users:
    c.execute("INSERT INTO users "
              "('id', 'login', 'name', 'gamedevexp', 'specialization', 'photo')"
              "VALUES "
              "('{id}', '{login}','{name}','{gamedevexp}','{specialization}', '{photo}')".format(**user))
    conn.commit()




# Add second table

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
    INSERT INTO room_information (id, room_name, positions_required, admin_name,)
    VALUES
    (2, "Best Game Ever", "Tester, Designer, Programmer" , "Vas"),
    (3, "Worst Game Ever", "Composer, Programmer" , "sarah"),
    (4, "Just a Game", "Programmer, Manager" , "lizza"),
    (5, "Test Game", "Programmer, Programmer", "jesus")
''')
conn.commit()



conn.close()