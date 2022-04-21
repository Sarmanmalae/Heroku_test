from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, EmailField, IntegerField, BooleanField
from wtforms.validators import DataRequired
from wtforms import FileField


class RegisterForm(FlaskForm):
    name = StringField('Название', validators=[DataRequired()])
    price = IntegerField('Цена', validators=[DataRequired()])
    pic = FileField('Картинка', validators=[DataRequired()])
    category = StringField('Категория', validators=[DataRequired()])
    in_stock = BooleanField('В наличии?', validators=[DataRequired()])
    submit = SubmitField('Добавить')
