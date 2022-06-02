from flask_wtf import Form
from wtforms import StringField, IntegerField, TextAreaField, SubmitField, SelectField

from wtforms import validators,ValidationError

class ContactForm(Form):
    name=StringField("Name of the student:",[validators.DataRequired("please enter the name")])
    fname=StringField("Enter your father name:",[validators.DataRequired("please enter the name")])
    submit=SubmitField("submit:")



    