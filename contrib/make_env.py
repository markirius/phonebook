import os
from base64 import b64encode
from secrets import token_bytes

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def make_env():
    env = os.path.join(BASE_DIR, ".env")
    if os.path.isfile(env):
        print(".env already created!")
    else:
        file = open(env, "w")
        file.write(f"""SECRET_KEY={b64encode(token_bytes(32)).decode()}
DEBUG=TRUE
DEVELOPMENT=TRUE
ADMIN_ENABLED=TRUE
# LANGUAGE_CODE=pt-br
# DATABASE_URL=postgres://username:password@address:port/phonebook
# ALLOWED_HOSTS=localhost, 0.0.0.0, 127.0.0.1
""")
        file.close()


if __name__ == "__main__":
    make_env()
