from app import app,db
import datetime
from flask import render_template,redirect,url_for,flash,request
import forms
from models import tasks,User,orders,orders_id
from flask_login import LoginManager , UserMixin , login_required ,login_user, logout_user,current_user
from app import login_manager


# Function to group data by the first column
def group_data(data):
    grouped_data = {}
    for row in data:
        key = row[0]
        if key not in grouped_data:
            grouped_data[key] = []
        grouped_data[key].append(row[1:])
    return grouped_data

@login_manager.user_loader
def get(id):
    return User.query.get(id)

@app.route('/',methods=['GET'])
@app.route('/index')
def index():
    return render_template('home.html')

@app.route('/login',methods=['GET'])
def get_login():
    return render_template('login.html')


@app.route('/signup',methods=['GET'])
def get_signup():
    return render_template('signup.html')

@app.route('/login',methods=['POST'])
def login_post():
    email = request.form['email']
    password = request.form['password']
    user = User.query.filter_by(email=email).first()
    print(user)
    login_user(user)
    return redirect('homepage')

@app.route('/signup',methods=['POST'])
def signup_post():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    user = User(username=username,email=email,password=password)
    db.session.add(user)
    db.session.commit()
    user = User.query.filter_by(email=email).first()
    login_user(user)
    return redirect('/')

@app.route('/logout',methods=['GET'])
def logout():
    logout_user()
    return redirect('index')



@app.route("/homepage")
@login_required
def homepage():
    joined_data = db.session.query(orders_id, orders).join(orders, orders_id.order_id == orders.order_id).all()
    data_tuples = [(item.orders_id.order_id, item.orders_id.date, item.orders.width, item.orders.hight, item.orders.weight,item.orders.hint) for item in joined_data]

    grouped_data = group_data(data_tuples)
    print(grouped_data.items())
    #alltask=tasks.query.all()
    return render_template("homepage.html",grouped_data=grouped_data)


@app.route("/add",methods=['GET','POST'])
@login_required
def add():
    form=forms.AddTaskForm()
    if form.validate_on_submit():
        t=tasks(title=form.title.data,date=datetime.datetime.utcnow())
        db.session.add(t)
        db.session.commit()
        flash("TASK ADDED SUCCESSFULLY")
        return redirect(url_for('homepage'))
    return render_template("add.html",form=form)


@app.route("/edit/<int:task_id>",methods=['GET','POST'])
@login_required
def edit(task_id):
    t=tasks.query.get(task_id)
    form=forms.AddTaskForm()
    if t:
        if form.validate_on_submit():
            t.title=form.title.data
            t.date=datetime.datetime.utcnow()
            db.session.commit()
            return redirect(url_for('homepage'))

        form.title.data=t.title
        return render_template("edit.html",form=form,task_id=task_id)
        
    return redirect(url_for("homepage"))


@app.route("/delete/<int:task_id>",methods=['GET','POST'])
@login_required
def delete(task_id):
    t=orders_id.query.get(task_id)
    form=forms.DeleteTaskForm()
    if t:
        if form.validate_on_submit():
            db.session.delete(t)
            db.session.commit()
            return redirect(url_for("homepage"))
        return render_template("delete.html",form=form,task_id=task_id,title=orders_id.order_id)
    
    return render_template("delete.html")