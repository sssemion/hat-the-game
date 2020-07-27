import datetime
import secrets

from sqlalchemy import Column, String, DateTime


class TokenAuthMixin:
    token = Column(String, index=True, unique=True)
    token_expiration = Column(DateTime)

    def get_token(self, expires_in: int = 3600) -> str:
        """
        Возвращает токен аутентификации. Если токен уже есть, и до его истечения осталось больше
        минуты, возвращается старый токен. Иначе, генерируется и возвращается новый
        :param expires_in: Срок действия токена в секундах (1 час по умолчанию)
        :return: Строка, содержащая токен
        """
        now = datetime.datetime.now()
        if self.token and self.token_expiration > now + datetime.timedelta(seconds=60):
            # Если токен действительный, возвращаем его
            return self.token
        # Иначе, генерируем новый и устанавливаем срок истечения через 3 часа
        self.token = secrets.token_urlsafe(24)
        self.token_expiration = now + datetime.timedelta(seconds=expires_in)
        return self.token

    def revoke_token(self) -> None:
        """
        Отзывает токен аутентификации.
        :return: None
        """
        # Отзыв токена (Время истечения изменяется на текущее - 1 секунда)
        self.token_expiration = datetime.datetime.now() - datetime.timedelta(seconds=1)
