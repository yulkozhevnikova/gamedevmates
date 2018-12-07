# Import sqlite3 module (in standart library - do not need to install)
import sqlite3

# Connect ot Database - in local file app.db
conn = sqlite3.connect('app.db')
# Create a cursor - a
c = conn.cursor()


c.execute('''
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    specialization TEXT,
    gamedevexp TEXT
)
''')

conn.commit()

# Adding some data (feel free to use you own data)
c.execute('''
    INSERT INTO users (name, specialization, gamedevexp)
    VALUES ("Volodya", "Tester", "3")
''')
conn.commit()

c.execute('''
    ALTER TABLE users
    ADD COLUMN login TEXT
''')
conn.commit()

c.execute('''
    UPDATE users
    SET login="vlad"
    WHERE name='Volodya Smirnov'
''')
conn.commit()


c.execute('''
    ALTER TABLE users
    ADD COLUMN photo TEXT
''')
conn.commit()


# Our base data
users = [
    {
        'login': 'Vas',
        'name': 'Vasiliy',
        'specialization': 'Designer',
        'gamedevexp': '3'
    },
    {
        'login': 'jimbo',
        'name': 'Roman Vlasov',
        'specialization': 'Composer',
        'gamedevexp': '2'
    }
]
# Adding it in the loop
for user in users:
    c.execute("INSERT INTO users "
              "('login', 'name', 'gamedevexp', 'specialization')"
              "VALUES "
              "('{login}','{name}','{gamedevexp}','{specialization}')".format(**user))
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

c.execute("INSERT INTO users_rooms (user_id, room_id) VALUES (1, 1)")
conn.commit()
c.execute("INSERT INTO users_rooms (user_id, room_id) VALUES (2, 1)")
conn.commit()


c.execute("SELECT u.* "
          "FROM users_rooms ue "
          "JOIN users u ON (u.id=ue.user_id) "
          "WHERE ue.room_id=1")


conn.close()