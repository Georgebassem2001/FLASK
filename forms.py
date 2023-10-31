from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import data_required

class AddTaskForm(FlaskForm):
    title= StringField("Title",validators=[data_required()])
    submit=SubmitField('submit')


class DeleteTaskForm(FlaskForm):
    submit=SubmitField('delete')