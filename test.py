
from flask import Flask
from flask import render_template
from flask import request
import db
import sqlite3
app = Flask(__name__)




@app.route('/')
def hello_world():
    # Connecting to DB
    conn = sqlite3.connect('app.db')
    c = conn.cursor()

    # Handler logic here
    c.execute("SELECT * FROM users_info")
    users = list(c.fetchall())

    # Close connection
    conn.close()
    # Return resulting HTML
    return render_template('page02.html', users_info=users)


@app.route('/search')
def search_for_person():
    conn = sqlite3.connect('app.db')
    c = conn.cursor
    q = request.args.get('query')
    c.execute("SELECT* FROM users_info where name LIKE '{q}'".format(q=q))
    users = list(c.fetchall())
    return render_template('search_results.html', q=q, users_info=users)




app.run()