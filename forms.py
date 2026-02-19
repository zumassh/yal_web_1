from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Optional


class PetitionForm(FlaskForm):
    name = StringField('Имя',
                       validators=[DataRequired(message="Имя обязательно для заполнения"),
                                   Length(min=2, max=50, message="Имя должно быть от 2 до 50 символов")])

    surname = StringField('Фамилия',
                          validators=[DataRequired(message="Фамилия обязательна для заполнения"),
                                      Length(min=2, max=50, message="Фамилия должна быть от 2 до 50 символов")])

    sex = RadioField('Пол',
                     choices=[('male', 'Мужской'), ('female', 'Женской')],
                     default='female',
                     validators=[DataRequired()])

    sign = BooleanField('Подписать петицию', default=True)

    submit = SubmitField('Подтвердить')