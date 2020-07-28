import os

from tornado_sqlalchemy import SQLAlchemy

pg_user = os.environ.get("PG_USER")
pg_pass = os.environ.get("PG_PASS")
pg_host = os.environ.get("PG_HOST")
db_name = os.environ.get("DB_NAME")

SETTINGS = {
    "autoescape": None,
    "cookie_secret": os.environ.get("COOKIE_SECRET"),
    "db": SQLAlchemy(f"postgres://{pg_user}:{pg_pass}@{pg_host}/{db_name}"),
    "debug": True,
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
    "xsrf_cookies": True,
}
