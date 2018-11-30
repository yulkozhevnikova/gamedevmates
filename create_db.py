import sqlite3

conn = sqlite3.connect('app.db')

c = conn.cursor()

c.execute('''
CREATE TABLE users_info (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          name TEXT,
          login TEXT,
          specialization TEXT,
          gamedevexp TEXT
)
''')

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

c.execute('''
CREATE TABLE users_rooms (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          users_id INTEGER,
          room_id INTEGER,
          FOREIGN KEY (users_id) REFERENCES users(id),
          FOREIGN KEY (room_id) REFERENCES room_information(id)       
)
''')



c.execute("INSERT into users_info values (1, 'Vasya', 'Vasek', 'Designer', 'None') ")
c.execute("INSERT into users_info values (15, 'Dima', 'Dimas', 'Manager', 'None') ")


c.execute("select * from users")

list (c.fetchall())


c.execute("INSERT into users_info values (1, 'Vasya', 'Designer', 'None') ")
c.execute("INSERT into users_info values (2, 'Dima', 'Manager', 'None') ")


c.execute("SELECT id FROM users")
results = c.fetchall()
print(results)



users_info = [
    {
        'ID': 1,
        'login': 'Roman',
        'name': 'Roman Ivanov',
        'specialization': 'Musician',
        'gamedevexp':'None'
    },

    {
        'ID': 2,
        'login': 'vaas',
        'name': 'Vasiliy Smirnov',
        'specialization': 'Designer',
        'gamedevexp': '2 years'
    },

    {
        'ID': 3,
        'login': 'griwa',
        'name': 'Grigoriy Potapenko',
        'specialization': 'Programmer',
        'gamedevexp': '1 years'
    },

     {
        'ID': 4,
        'login': 'Alex',
        'name': 'Alexey Moroz',
        'specialization': 'Sound designer',
        'gamedevexp': 'None'
    },
     {
        'ID': 5,
        'login': 'bro',
        'name': 'Rostislav Novikov',
        'specialization': 'Screenwriter',
        'gamedevexp': '5'
    },
     {
        'ID': 6,
        'login': 'len9',
        'name': 'Leonid Geishtor',
        'specialization': '3D modelling',
        'gamedevexp': '2'
    },
     {
        'ID': 7,
        'login': 'lima',
        'name': 'Vladimir Serebryakov',
        'specialization': 'Community Manager',
        'gamedevexp': '1'
    },
    {
        'ID': 8,
        'login': 'sor',
        'name': 'Vladislav Popov',
        'specialization': 'Tester',
        'gamedevexp': 'None'
    },
    {
        'ID': 9,
        'login': 'reg',
        'name': 'Denis Mrezhin',
        'specialization': 'Programmer',
        'gamedevexp': '3'
    },
]



# Adding it in the loop
for user in users_info:
    c.execute("INSERT INTO users_info "
              "(login, name, specialization, gamedevexp) "
              "VALUES "
              "('{login}','{name}','{specialization}','{gamedevexp}')".format(**user))
    conn.commit()

