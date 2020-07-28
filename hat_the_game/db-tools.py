import argparse
import getpass
from enum import Enum

import hat_the_game.services
from hat_the_game.services.admin import check_if_superuser_already_exists
from hat_the_game.services.basic import is_password_secure


class Actions(Enum):
    CREATE_SUPERUSER = "create-superuser"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("action", type=str, choices=list(map(lambda x: x.value, Actions)))
    args = parser.parse_args()

    if args.action == Actions.CREATE_SUPERUSER.value:
        create_superuser()
    else:
        print("Understandable, have a nice day")


def create_superuser():
    # login
    while True:
        login = input("Username (Login): ")
        if not login:
            print("Login cannot be empty")
        elif len(login) >= 64:
            print(f"Too long login")
        elif check_if_superuser_already_exists(login=login):
            print(f"Superuser with login \"{login.lower().strip()}\" already exists")
        else:
            break
    # email
    while True:
        email = input("Email: ")
        if not email:
            print("Email cannot be empty")
        elif "@" not in email or "." not in email.split("@")[1]:
            print(f"Incorrect email!")
        elif len(email) >= 256:
            print(f"Too long email!")
        elif check_if_superuser_already_exists(email=email):
            print(f"Superuser with email \"{email.lower().strip()}\" already exists")
        else:
            break
    # first_name
    while True:
        first_name = input("First name: ")

        if not first_name:
            print("First name cannot be empty")
        elif len(first_name) >= 64:
            print("Too long first name")
        else:
            break
    # last_name
    while True:
        last_name = input("Last name: ")
        if not last_name:
            print("Last name cannot be empty")
        elif len(last_name) >= 64:
            print("Too long last name")
        else:
            break
    # password
    while True:
        password = getpass.getpass("Password: ")
        if not password:
            print("Password cannot be empty")
        elif not is_password_secure(password):
            print("Unsafe password! Password must be at least 8 characters, contain at least one "
                  "lowercase letter, one uppercase letter and one digit ")
        else:
            break
    # password again
    while True:
        password_again = getpass.getpass("Confirm password: ")
        if password != password_again:
            print("Passwords don't match")
        else:
            break

    try:
        hat_the_game.services.admin.create_superuser(login, email, first_name, last_name, password)
        print("\033[92mSuperuser successfully created\033[0m")
    except Exception as e:
        print("Something went wrong. Press enter to show traceback")
        input()
        raise e


if __name__ == '__main__':
    main()
