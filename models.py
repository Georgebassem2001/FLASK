from app import db
from flask_login import LoginManager , UserMixin , login_required ,login_user, logout_user,current_user
from sqlalchemy.orm import backref

class tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100),nullable=False)
    date= db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f'{self.title} created on {self.date}'
    

class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(200))
    email = db.Column(db.String(200))
    password = db.Column(db.String(200))


class orders_id(db.Model):
    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    orders = db.relationship('orders', backref="orders_id",cascade='all,delete')

class orders(db.Model):
    job_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders_id.order_id'), nullable=False)
    width = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    hint = db.Column(db.String(100), nullable=True)
