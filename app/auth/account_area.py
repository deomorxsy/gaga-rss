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

