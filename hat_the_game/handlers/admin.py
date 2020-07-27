import tornado.web


class AdminHandler(tornado.web.RequestHandler):
    async def get(self):
        if self.current_user is None:
            await self.render("admin-login.html")
        else:
            await self.render("admin.html")

    async def post(self):
        #  TODO: сделать форму авторизации суперпользователя (Логин и пароль).
        #   При успешной аутентификации в cookies сохраняется токен, после чего пользователя
        #   перенаправляют на /admin, но так как он уже авторизован, ему отображается панель
        #   администратора, вместо формы авторизации
        pass
