from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from subprocess import call

app = Flask(__name__)
app.config['SECRET_KEY'] = "SuperSecretKey"
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://bnffgxgcxgyobi:94154bed8bf0e06416ef2ccb2c4e1c73b936b229b5ac570b4edc3522ff48842b@ec2-184-73-153-64.compute-1.amazonaws.com:5432/d6urq5baj9736a"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project1:password123@localhost/project1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
app.config['UPLOAD_FOLDER'] = './app/static/photo'
db = SQLAlchemy(app)

allowed_exts = ["jpg", "jpeg", "png"]

from app import views