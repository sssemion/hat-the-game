from contextlib import contextmanager
from typing import Iterator

from sqlalchemy.orm import Session

from hat_the_game import app

db = app.settings["db"]


@contextmanager
def make_session() -> Iterator[Session]:
    session = None

    try:
        session = db.sessionmaker()

        yield session
    except Exception:
        if session:
            session.rollback()
        raise
    else:
        session.commit()
    finally:
        if session:
            session.close()
