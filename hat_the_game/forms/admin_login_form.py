from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from wtforms_tornado import Form


class AdminLoginForm(Form):
    login = StringField("Email или имя пользователя", validators=[DataRequired()])
    password = PasswordField("Пароль", validators=[DataRequired()])
    submit = SubmitField("Войти")
