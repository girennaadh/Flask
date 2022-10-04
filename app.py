from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from utils import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
from create_db import create_database

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = SQLALCHEMY_TRACK_MODIFICATIONS
app.debug = True
app.secret_key = 'postgresisgood'

db = SQLAlchemy(app)

class UserRegistration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(120), nullable=False)
    uemail = db.Column(db.String(120), unique=True, nullable=False)
    ucourse = db.Column(db.String(120), nullable=False)
    uprof = db.Column(db.String(120), nullable=False)
    ucompany = db.Column(db.String(120), nullable=False)
    uearning = db.Column(db.String(120), nullable=False)

    def __init__(self, uname, uemail, ucourse, uprof, ucompany, uearning):
        self.uname = uname
        self.uemail = uemail
        self.ucourse = ucourse
        self.uprof = uprof
        self.ucompany = ucompany
        self.uearning = uearning


@app.route('/')
def home():
    """
    Grep all values from the database
    SELECT id, uname, uemail, ucourse, uprof, ucompany, uearning
	FROM public.user_registration;
    """
    list_data = []
    data = []
    users = UserRegistration.query.all()

    for user in users:
        data = [user.uname, user.uemail, user.ucourse, user.uprof, user.ucompany, user.uearning]
        list_data.append(data)
    print (list_data)
    return render_template("index.html", list_data=list_data)

@app.route('/adduser')
def adduser():
    return render_template("register.html")

@app.route("/register", methods=['POST'])
def register():
    uname = request.form["uname"]
    uemail = request.form["uemail"]
    ucourse = request.form["ucourse"]
    uprof = request.form["uprof"]
    ucompany = request.form["ucompany"]
    uearning = request.form["uearning"]
    entry = UserRegistration(uname, uemail, ucourse, uprof, ucompany, uearning)
    db.session.add(entry)
    db.session.commit()

    list_data = []
    data = []
    users = UserRegistration.query.all()

    for user in users:
        data = [user.uname, user.uemail, user.ucourse, user.uprof, user.ucompany, user.uearning]
        list_data.append(data)
    print (list_data)
    return render_template("index.html", list_data=list_data)

if __name__ == '__main__':
    create_database()
    db.create_all()
    app.run(debug=True,host='0.0.0.0')