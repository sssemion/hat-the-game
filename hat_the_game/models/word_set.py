from sqlalchemy import Column, Integer, String, Boolean

from hat_the_game import app

db = app.settings["db"]


class WordSet(db.Model):
    __tablename__ = "word_sets"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, index=True)
    description = Column(String)
    img = Column(String, default="/static/img/word-sets-icons/default.svg")
    private = Column(Boolean, default=False)

# Todo: модель Word и отношение один ко многим (к модели WordSet)
