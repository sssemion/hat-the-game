import os

import tornado.web

from .handlers import handlers

app = tornado.web.Application(
    handlers,
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    debug=True
)
