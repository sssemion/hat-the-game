import datetime
from typing import Optional

from hat_the_game.models.superuser import Superuser
from hat_the_game.services.db_session_maker import make_session


def check_if_superuser_already_exists(login: str = None, email: str = None) -> bool:
    """
    Проверяет, есть ли суперпользователь с таким логином, почтой или и логином, и почтой
    :param login: Логин (строка)
    :param email: Почта (строка)
    :return: True, если есть, иначе - False
    """
    if login is None and email is None:
        raise TypeError("check_if_superuser_already_exists takes at least one argument (either login, email or both)")

    with make_session() as session:
        if login and session.query(Superuser).filter(Superuser.login == login.lower().strip()).first():
            return True
        if email and session.query(Superuser).filter(Superuser.email == email.lower().strip()).first():
            return True
    return False


def create_superuser(login: str, email: str, first_name: str, last_name: str, password: str) -> None:
    with make_session() as session:
        superuser = Superuser(login=login,
                              email=email,
                              first_name=first_name,
                              last_name=last_name)
        superuser.set_password(password)
        session.add(superuser)


def log_in(login: str, password: str) -> Optional[str]:
    """
    Выполняет аутентификацию суперпользователя. Если аутентификация прошла успешно, возвращает токен
    авторизации, иначе - None
    :param login: имя пользователя или email (строка)
    :param password: пароль (строка)
    :return: токен авторизации или None
    """
    with make_session() as session:
        superuser = session.query(Superuser).filter((Superuser.login == login) | (Superuser.email == login)).first()
        if superuser and superuser.verify_password(password):
            return superuser.get_token()
        return None


def verify_token(token: str) -> bool:
    """
    Проверяет токен авторизации. Если токен существует и действителен, возвращает True, иначе - False
    :param token: токен авторизации (строка)
    :return: True, если токен действителен, иначе - False
    """
    with make_session() as session:
        superuser = session.query(Superuser).filter(Superuser.token == token).first()
        if superuser is None or superuser.token_expiration < datetime.datetime.now():
            return False
        return True
