from app import app,db
import datetime
from flask import render_template,redirect,url_for,flash
import forms
from classes import tasks

@app.route("/")
@app.route("/index")
def index():
    alltask=tasks.query.all()
    return render_template("index.html",alltasks=alltask)

@app.route("/add",methods=['GET','POST'])
def add():
    form=forms.AddTaskForm()
    if form.validate_on_submit():
        t=tasks(title=form.title.data,date=datetime.datetime.utcnow())
        db.session.add(t)
        db.session.commit()
        flash("TASK ADDED SUCCESSFULLY")
        return redirect(url_for('index'))
    return render_template("add.html",form=form)


@app.route("/edit/<int:task_id>",methods=['GET','POST'])
def edit(task_id):
    t=tasks.query.get(task_id)
    form=forms.AddTaskForm()
    if t:
        if form.validate_on_submit():
            t.title=form.title.data
            t.date=datetime.datetime.utcnow()
            db.session.commit()
            return redirect(url_for('index'))

        form.title.data=t.title
        return render_template("edit.html",form=form,task_id=task_id)
        
    return redirect(url_for("index"))


@app.route("/delete/<int:task_id>",methods=['GET','POST'])
def delete(task_id):
    t=tasks.query.get(task_id)
    form=forms.DeleteTaskForm()
    if t:
        if form.validate_on_submit():
            db.session.delete(t)
            db.session.commit()
            return redirect(url_for("index"))
        return render_template("delete.html",form=form,task_id=task_id,title=t.title)
    
    return render_template("delete.html")