import tornado.web
from tornado_sqlalchemy import SessionMixin

from hat_the_game.forms.create_game_session_form import CreateGameSessionForm


class IndexHandler(SessionMixin, tornado.web.RequestHandler):
    async def get(self):
        create_game_form = CreateGameSessionForm()
        await self.render("index.html",
                          create_game_form=create_game_form)

    async def post(self):
        create_game_form = CreateGameSessionForm(self.request.arguments)
        if create_game_form.validate():
            from hat_the_game.services.game_sessions import create_game_session_from_form
            create_game_session_from_form(create_game_form)
        else:
            self.send_error(400)
