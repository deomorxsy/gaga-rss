#!/usr/bin/python3

import feedparser
from flask import Flask
from flask import render_template
from flask import request

from flask_login import LoginManager
from flask_login import login_required
from flask_login import login_user
from flask import redirect
from flask import url_for

#
import sys
sys.path.append('./auth/')
import account_area

#db dir
sys.path.append('./db/')
from mockdb import MockDBHelper as DBHelper
from user import User


app = Flask(__name__)

RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
             'cnn': 'http://rss.cnn.com/rss/edition.rss',
             'fox': 'http://feeds.foxnews.com/foxnews/latest',
             'iol': 'http://www.iol.co.za/cmlink/1.640'}

#"if strict_slashes is enabled (the default),
#visiting a branch URL without a trailing slash
#will redirect to the URL with a slash appended."
@app.route('/index/', strict_slashes=False)
@app.route('/index/<publication>/')
def get_news(publication='bbc'):
	feed = feedparser.parse(RSS_FEEDS[publication])
	first_article = feed['entries'][0]
	return render_template('index.html', article=feed['entries'])#, articles=feed['entries'])

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
   and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response




'''
#mock, not in prod
app = Flask(__name__)
app.secret_key = 'ThOnEu2jEtgKqp69BRNh79+8YM3CkxnyEB1db9i1PRxyXNiO5JC4PemrDTiAaOU/HgTmNvmpWAXYyQ+TAs7SS48Z4AqRFjkt9O4'
login_manager = LoginManager(app)

@app.route("/")
def home():
    return render_template("landing.html")

@app.route("/login", methods=["POST"], strict_slashes=False)
def login():
    email = request.form.get("email")
    passwd = request.form.get("password")
    user_passwd = DB.get_user(email)
    if user_passwd and user_passwd == passwd:
        user = User(email)
        login_user(user)
        return redirect(url_for('account'))
    return home()

@app.route("/account")
@login_required
def account():
    return "Logged in!"

@login_manager.user_loader
def load_user(user_id):
    user_passwd = DB.get_user(user_id)
    if user_passwd:
        return User(user_id)

'''


if __name__ == '__main__':
    app.run(port=5000, debug=True)

