import secrets

from hat_the_game.forms.create_game_session_form import CreateGameSessionForm
from .db_session_maker import make_session


def create_game_session_from_form(form: CreateGameSessionForm) -> None:
    """
    Создает запись в БД об игровой сессии на основе данных из формы CreateGameSessionForm
    :param form: Форма WTForms, заполненная пользователем
    :return: None
    """
    with make_session() as session:
        from hat_the_game.models import GameSession
        game_session = GameSession(
            invite_id=generate_invite_id(),
            name=form.name.data,
            private=form.is_private.data,

            word_set_id=None if form.own_set.data
            else form.categories.data
        )
        session.add(game_session)


def generate_invite_id() -> str:
    """
    Генерирует уникальный 8-значный код приглашения в игру
    :return: invite_id (строка из 8 символов)
    """
    with make_session() as session:
        while True:
            invite_id = secrets.token_urlsafe(6)

            from hat_the_game.models import GameSession
            from hat_the_game.handlers import handlers

            if session.query(GameSession).filter(GameSession.invite_id == invite_id).first():
                continue
            elif invite_id in map(lambda x: x[0].strip("\\/"), handlers):
                continue

            return invite_id
