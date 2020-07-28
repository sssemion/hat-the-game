import datetime
from typing import Optional

from hat_the_game.models.superuser import Superuser
from hat_the_game.services.db_session_maker import make_session


def get_superuser_serialization(token: str) -> Optional[dict]:
    with make_session() as session:
        superuser = session.query(Superuser).filter(Superuser.token == token).first()
        if superuser and superuser.token_expiration > datetime.datetime.now():
            return superuser.to_dict_normal()
        return None
