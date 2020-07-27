from hat_the_game.handlers.admin import AdminHandler
from hat_the_game.handlers.index import IndexHandler

handlers = [
    [r"/", IndexHandler],
    [r"/admin", AdminHandler]
]