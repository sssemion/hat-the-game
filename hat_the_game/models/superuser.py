import datetime

from sqlalchemy import Column, Integer, String, DateTime

from hat_the_game import app
from hat_the_game.models.mixins.login_mixin import LoginMixin
from hat_the_game.models.mixins.token_auth_mixin import TokenAuthMixin

db = app.settings["db"]


class Superuser(LoginMixin, TokenAuthMixin, db.Model):
    __tablename__ = "superusers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String(63), index=True, nullable=False, unique=True)
    email = Column(String(255), index=True, nullable=False, unique=True)
    first_name = Column(String(63))
    last_name = Column(String(63))
    reg_date = Column(DateTime, default=datetime.datetime.now())
    password = Column(String(255))

    def verify_password(self, assumed_password: str, **kwargs) -> bool:
        return super(Superuser, self).verify_password(self.password, assumed_password)
