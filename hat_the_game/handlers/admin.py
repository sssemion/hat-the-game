from typing import Optional

import tornado.web

from hat_the_game.forms.admin_login_form import AdminLoginForm


class AdminHandler(tornado.web.RequestHandler):
    async def get(self):
        current_user = await self.current_user
        if current_user is None:
            form = AdminLoginForm()
            await self.render("admin/admin-login.html", form=form)
        else:
            params = {
                "superuser_token": current_user
            }
            await self.render("admin/admin.html", **params)

    async def post(self):
        login_form = AdminLoginForm(self.request.arguments)
        if login_form.validate():
            from hat_the_game.services.admin import log_in
            token = log_in(login_form.login.data, login_form.password.data)
            if token is None:
                await self.render("admin/admin-login.html", form=login_form, login_failed=True)
            else:
                self.set_secure_cookie("token", token.encode("utf-8"))
                await self.redirect("/admin")

    async def get_current_user(self) -> Optional[str]:
        # self.current_user представляет собой токен авторизации, хранящийся в cookies
        token = self.get_secure_cookie("token")
        if not token:
            return None
        token = token.decode("utf-8")
        from hat_the_game.services.admin import verify_token
        if verify_token(token):
            return token
        return None
