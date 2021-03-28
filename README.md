## Phonebook

- A simple project for education purpose

- Work's with sqlite or postgres databases

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

## Using postgresql

- Setting DATABASE_URL like:
```DATABASE_URL=postgres://username:password@address:port/phonebook```
