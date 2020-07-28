import binascii
import hashlib
import os


class LoginMixin:
    def generate_password_hash(self, password: str) -> str:
        """
        Генерирует безопасный хэш пароля для хранения в базе данных
        :param password: Исходный пароль
        :return: Строка, содержащая хешированный пароль
        """
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode("ascii")
        password_hash = hashlib.pbkdf2_hmac("sha512",
                                            password.encode("utf-8"),
                                            salt,
                                            100000)
        password_hash = binascii.hexlify(password_hash)
        return (salt + password_hash).decode("ascii")

    def verify_password(self, stored_password: str, assumed_password: str) -> bool:
        """
        Проверяет переданный пароль на совпадение с сохраненным.

        Метод следует переопределить в модели так, чтобы он получал 1 аргумент (введенный пароль),
        и вызывал метод родителя, передавая в него пароль, хранящийся в модели, и полученный аргумент

        :param assumed_password: Введенный пароль для проверки
        :param stored_password: Сохраненный пароль
        :return: True есди пароль верный, иначе False
        """
        salt = stored_password[:64]
        stored_password = stored_password[64:]

        password_hash = hashlib.pbkdf2_hmac("sha512",
                                            assumed_password.encode("utf-8"),
                                            salt.encode("ascii"),
                                            100000)
        password_hash = binascii.hexlify(password_hash).decode("ascii")
        return stored_password == password_hash
