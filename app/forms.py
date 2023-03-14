from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import InputRequired


class MyForm(FlaskForm):
    title = StringField('Property Title', validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])
    rooms = StringField('No. of Rooms', validators=[InputRequired()])
    bathrooms = StringField('No. of Bathrooms', validators=[InputRequired()])
    price = StringField('Price', validators=[InputRequired()])
    desc = TextAreaField('Description', validators=[InputRequired()])
    prop_type = SelectField(u'Property Type', choices=[('h', 'House'), ('a', 'Apartment')], validators=[InputRequired()])


class PhotoForm(FlaskForm):
    photo = FileField('Photo', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'Images only!')
    ])
    description = StringField('Description', validators=[InputRequired()])