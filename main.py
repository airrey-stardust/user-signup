# create a user sign up with username, password, verify password, and email
# error when leaving fields empty

from flask import flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')



def index():

    return render_template('index.html')