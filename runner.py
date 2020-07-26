import os

import tornado.ioloop


def print_warn(message):  # printing warning (yellow)
    print("\x1b[1;33m" + message + "\x1b[0m")


def print_err(message):  # printing errors (red)
    print('\x1b[1;31m' + message + '\x1b[0m')


if __name__ == "__main__":
    try:
        from hat_the_game import app
    except FileNotFoundError as e:
        print_err(f"Error: {e}")
        exit(0)

    port = os.environ.get("PORT", 8080)
    host = os.environ.get("HOST", "127.0.0.1")

    app.listen(port, address=host)

    if app.settings.get("debug", False):
        print_warn("    Debugger is active!")
    print_warn(f"    Running on http://{host}:{port} (press Ctrl+C to quit)\n")

    try:
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        tornado.ioloop.IOLoop.instance().stop()
