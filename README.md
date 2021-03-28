## Phonebook

- A simple project for education purpose

- Work's with sqlite or postgres databases

- Build with:
* python 3.9.2
* django 2.2.19

## Decouple .env file

| var | default | type |
| :-: | :-----: | :--: |
| SECRET_KEY | <random_string> | string |
| ALLOWED_HOSTS | 127.0.0.1, 0.0.0.0, localhost | string (separated by commas) |
| DATABASE_URL | sqlite:///db.sqlite3 | string |
| DEBUG | False | boolean |
| ADMIN_ENABLED | False | boolean |
| LANGUAGE_CODE | en-us | string |
| DEVELOPMENT | False | boolean |

- You can generate .env file using:
```python contrib/make_env.py```

## Using postgresql

- Setting DATABASE_URL like:
```DATABASE_URL=postgres://username:password@address:port/phonebook```
