from flask import Flask
from flask import render_template
from flask import request, redirect
import db
import sqlite3
app = Flask(__name__)


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/')
def room_inf():
    conn = sqlite3.connect('app.db')
    conn.row_factory = dict_factory
    c = conn.cursor()

    c.execute ("SELECT * FROM room_information")
    room_information = list(c.fetchall())
    conn.close()
    return render_template('page03.html', room_information=room_information)


@app.route('/user')
def hello_world():
    # Connecting to DB
    conn = sqlite3.connect('app.db')
    conn.row_factory = dict_factory
    c = conn.cursor()

    # Handler logic here
    c.execute("SELECT * FROM users")
    users = list(c.fetchall())

    # Close connection
    conn.close()
    # Return resulting HTML
    return render_template('page01.html', users=users)


@app.route('/user/<login>/')
def user_page(login):
    conn = sqlite3.connect('app.db')
    conn.row_factory = dict_factory
    c = conn.cursor()

    # Handler logic here
    c.execute("SELECT * FROM users WHERE login='%s'" % login)
    user_data = c.fetchone()

    # Close connection
    conn.close()
    return render_template("userpage.html", user=user_data)



@app.route('/room_info/<room_name>/')
def room_page(room_name):
    conn = sqlite3.connect('app.db')
    conn.row_factory = dict_factory
    c = conn.cursor()

    # Handler logic here
    c.execute("SELECT * FROM room_information WHERE room_name='%s'" % room_name)
    room_data = c.fetchone()

    # Close connection
    conn.close()
    return render_template("roompage.html", room_info=room_data)




@app.route('/add_user', methods=['GET', 'POST'])
def add_user():

    user_created = False
    error_message = ""

    if request.method == 'POST':
        # add new user data
        user = {}
        user['login'] = request.form.get('login')
        user['name'] = request.form.get('name')
        user['specialization'] = request.form.get('specialization')
        user['gamedevexp'] = request.form.get('gamedevexp')
        user['photo'] = request.form.get('photo')


        # save to database
        conn = sqlite3.connect('app.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users where login='%s'" % user['login'])
        if c.fetchone():
            # user with this login is already in my database
            error_message = "user_exists"
        else:
            c.execute("INSERT INTO users "
                      "('login', 'name', 'gamedevexp', 'specialization', 'photo')"
                      "VALUES "
                      "('{login}','{name}','{gamedevexp}','{specialization}', '{photo}')"
                      "".format(**user))
            conn.commit()
            user_created = True
        conn.close()
        # redirect to user page
        # return redirect('/user/%s/' % user['login'])


    return render_template(
        "add_user.html",
        user_created=user_created,
        error_message=error_message
    )


@app.route('/search')
def search_for_person():
    q = request.args.get('query')
    conn = sqlite3.connect('app.db')
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE login like '%" + q + "%'")
    users = list(c.fetchall())
    conn.close()
    return render_template('search_results.html', q=q, users=users)




app.run()