from flask import Flask, request, render_template, url_for, redirect
from database import Database
import os

app = Flask(__name__)
app.config.from_pyfile('server.cfg')

# initialize database
db = Database(app)

@app.route('/')
def home():
    return render_template('home.html', db=db)

@app.route('/mission')
def mission():
    return render_template('mission.html', db=db)

@app.route('/about')
def about():
    return render_template('about.html', db=db)

@app.route('/contact', methods=['GET','POST'])
def contact():
    if request.method == 'GET':
        return render_template('contact.html', db=db)
    else:
        name = request.form['name']
        print name
        email = request.form['email']
        print email
        interests = ''
        print interests
        if 'discuss' in request.form:
            discuss = request.form['discuss']
            interests += discuss
        if 'leading' in request.form:
            leading = request.form['leading']
            interests += leading
        if 'intouch' in request.form:
            intouch = request.form['intouch']
            interests += intouch
        print interests
        os.system("mail -s "+name+email+interests+" elevin@macalester.edu")
        db.create(name,email,interests)
        return redirect(url_for('home'))

@app.route('/resources')
def resources():
    return render_template('resources.html', db=db)
