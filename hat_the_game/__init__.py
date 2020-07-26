import os

import tornado.web
from dotenv import load_dotenv

from .handlers import handlers

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
else:
    raise FileNotFoundError(".env file doesn't exists")

from .settings import SETTINGS

app = tornado.web.Application(
    handlers,
    **SETTINGS
)

from hat_the_game import models

app.settings["db"].create_all()
