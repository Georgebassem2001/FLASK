from flask import Flask,render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY']='kfjnsad'

app.config['SQLALCHEMY_DATABASE_URI']='mysql://gokas:Gokas-2001@localhost/acme'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True

db=SQLAlchemy(app)
app.app_context().push()
    
from routes import *

if __name__=="__main__":
    app.run(debug=True)