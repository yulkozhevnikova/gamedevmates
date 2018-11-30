import sqlite3

conn = sqlite3.connect('app.db')

c = conn.cursor()

c.execute('''
CREATE TABLE users (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          name TEXT,
          specialization TEXT,
          experience TEXT
)
''')

c.execute('''
CREATE TABLE room_information (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          users_id INTEGER,
          room_name TEXT,
          mates_required INTEGER,
          user_name TEXT,
          FOREIGN KEY (users_id) REFERENCES users(id)  ,
          FOREIGN KEY (user_name) REFERENCES users(name)       
)
''')




c.execute("select * from users")

list (c.fetchall())


c.execute("INSERT into users values (1, 'Vasya', 'Designer', 'None') ")

c.execute("SELECT id FROM users")
results = c.fetchall()
print(results)