import datetime

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy import orm

from hat_the_game import app

db = app.settings["db"]


class GameSession(db.Model):
    __tablename__ = "game_sessions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    invite_id = Column(String(8), nullable=False, unique=True, index=True)  # Идентификатор для
    # приглашения в игру (отображается в ссылке на сессию)

    name = Column(String(255), nullable=False, index=True)
    private = Column(Boolean, default=False)
    word_set_id = Column(Integer, ForeignKey("word_sets.id"))

    finished = Column(Boolean, default=False)
    creation_date = Column(DateTime, default=datetime.datetime.now())

    word_set = orm.relation("WordSet", foreign_keys=[word_set_id])