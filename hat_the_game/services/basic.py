def is_password_secure(password: str) -> bool:
    """
    Проверяет надежность пароля
    :param password: Пароль (строка)
    :return: True, если пароль надежный, иначе - False
    """
    return not (len(password) < 8 or
                password.isdigit() or
                password.isalpha() or
                password.islower() or
                password.isupper()) and password.isalnum()
