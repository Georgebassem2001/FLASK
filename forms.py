from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField,TextAreaField
from wtforms.validators import data_required

class AddTaskForm(FlaskForm):
    title= StringField("Title",validators=[data_required()])
    submit=SubmitField('submit')

class Addorder(FlaskForm):
    name = StringField('الأسم', validators=[data_required()])
    width = IntegerField('العرض', validators=[data_required()])
    height = IntegerField('الطول', validators=[data_required()])
    weight = IntegerField('الوزن', validators=[data_required()])
    hint = TextAreaField('ملاحظات')

class DeleteTaskForm(FlaskForm):
    submit=SubmitField('delete')