from wtforms import BooleanField, StringField, IntegerField, SubmitField, RadioField
from wtforms.validators import DataRequired, NumberRange
from wtforms_tornado import Form


class CreateGameSessionForm(Form):
    own_set = BooleanField("Создать свой набор")
    categories = RadioField(choices=[
        (1, "Животные"),
        (2, "Предметы"),
    ], coerce=int)
    name = StringField("Название комнаты", validators=[DataRequired()],
                       render_kw={"class": "input-name"})
    team_number = IntegerField("Количество команд", default=2,
                               validators=[DataRequired(), NumberRange(min=2, max=5)])
    is_private = BooleanField("Закрытая комната")

    submit = SubmitField("Создать", render_kw={"class": "button create-menu__submit-button"})
