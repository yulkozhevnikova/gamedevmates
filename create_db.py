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
    {
        'login': 'Vas',
        'name': 'Vasiliy',
        'specialization': 'Designer',
        'gamedevexp': '3',
        'photo': 'http://dic.academic.ru/pictures/wiki/files/79/Official_portrait_of_Barack_Obama.jpg'
    },
    {
        'login': 'jimbo',
        'name': 'Roman Vlasov',
        'specialization': 'Composer',
        'gamedevexp': '2',
        'photo': 'http://b.vimeocdn.com/ts/173/794/173794976_640.jpg'
    },
    {
        'login': 'Yoko',
        'name': 'Yoko Kanno',
        'specialization': 'Composer',
        'gamedevexp': '10',
        'photo': 'http://b.vimeocdn.com/ts/173/794/173794976_640.jpg'
    },
    {
        'login': 'Vash',
        'name': 'Vash Stampede',
        'specialization': 'Tester',
        'gamedevexp': '4',
        'photo': 'http://b.vimeocdn.com/ts/173/794/173794976_640.jpg'
    },
    {
        'login': 'rogue',
        'name': 'Viktor Efremov',
        'specialization': 'Composer',
        'gamedevexp': '2',
        'photo': 'http://b.vimeocdn.com/ts/173/794/173794976_640.jpg'
    },
    {
        'login': 'jezz',
        'name': 'Elena Vlasova',
        'specialization': 'Designer',
        'gamedevexp': 'None',
        'photo': 'http://b.vimeocdn.com/ts/173/794/173794976_640.jpg'
    },
    {
        'login': 'belli',
        'name': 'Lester Nygaard',
        'specialization': 'Programmer',
        'gamedevexp': '2',
        'photo': 'http://b.vimeocdn.com/ts/173/794/173794976_640.jpg'
    },
    {
        'login': 'cody',
        'name': 'Ivan Melnikov',
        'specialization': 'Programmer',
        'gamedevexp': '4',
        'photo': 'http://b.vimeocdn.com/ts/173/794/173794976_640.jpg'
    },
    {
        'login': 'Reg',
        'name': 'Vadim Litvinov',
        'specialization': 'Manager',
        'gamedevexp': '3',
        'photo': 'http://b.vimeocdn.com/ts/173/794/173794976_640.jpg'
    },
    {
        'login': 'lizza',
        'name': 'Elizaveta Karpina',
        'specialization': 'Programmer',
        'gamedevexp': '5',
        'photo': 'http://b.vimeocdn.com/ts/173/794/173794976_640.jpg'
    },
    {
        'login': 'on4k',
        'name': 'John Doe',
        'specialization': 'Designer',
        'gamedevexp': '7',
        'photo': 'http://b.vimeocdn.com/ts/173/794/173794976_640.jpg'
    },
    {
        'login': 'Flar',
        'name': 'Philipp Rogers',
        'specialization': 'Composer',
        'gamedevexp': 'None',
        'photo': 'http://b.vimeocdn.com/ts/173/794/173794976_640.jpg'
    },
    {
        'login': 'ANTOXA',
        'name': 'Anton Antonov',
        'specialization': 'Tester',
        'gamedevexp': 'None',
        'photo': 'http://b.vimeocdn.com/ts/173/794/173794976_640.jpg'
    },
    {
        'login': 'Ana',
        'name': 'Anna Fedorova',
        'specialization': 'Programmer',
        'gamedevexp': '3',
        'photo': 'http://b.vimeocdn.com/ts/173/794/173794976_640.jpg'
    }

]
# Adding it in the loop
for user in users:
    c.execute("INSERT INTO users "
              "('login', 'name', 'gamedevexp', 'specialization', 'photo')"
              "VALUES "
              "('{login}','{name}','{gamedevexp}','{specialization}', '{photo}')".format(**user))
    conn.commit()

# Add second table
c.execute('''
CREATE TABLE room_information (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          users_id INTEGER,
          room_name TEXT,
          mates_required INTEGER,
          user_name TEXT,
          FOREIGN KEY (users_id) REFERENCES users(id),
          FOREIGN KEY (user_name) REFERENCES users(name)       
)
''')
conn.commit()

c.execute('''
    INSERT INTO room_information (room_name, mates_required, user_name)
    VALUES
    ("Beholder", 8 , "Volodya")
''')
conn.commit()

# Many to many connection
c.execute('''
CREATE TABLE users_rooms (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          users_id INTEGER,
          room_id INTEGER,
          FOREIGN KEY (users_id) REFERENCES users(id),
          FOREIGN KEY (room_id) REFERENCES room_information(id)       
)
''')

conn.commit()

c.execute("INSERT INTO users_rooms (users_id, room_id) VALUES (1, 1)")
conn.commit()
c.execute("INSERT INTO users_rooms (users_id, room_id) VALUES (2, 1)")
conn.commit()


c.execute("SELECT u.* "
          "FROM users_rooms ue "
          "JOIN users u ON (u.id=ue.user_id) "
          "WHERE ue.room_id=1")


conn.close()