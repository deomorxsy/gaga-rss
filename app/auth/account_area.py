from flask.ext.login import LoginManager
from flask.ext.login import login_required

app = Flask(__name__)
login_manager = LoginManager(app)

@app.route("/")
def home():
    return render_template("landing.html")

@app.route("/account")
@login_required
def account():
    return "Logged in!"

