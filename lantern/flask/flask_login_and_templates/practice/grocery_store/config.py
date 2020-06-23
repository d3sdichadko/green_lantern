import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
FIXTURES_DIR = os.path.join(ROOT_DIR, 'fixtures')


class Config:
    DEBUG = True
    HOST = '127.0.0.1'
    PORT = 8080
    SECRET_KEY = 'aa01018c-c962-46c4-8087-c229c7e36c59'
    PG_USER = "cursor"
    PG_PASSWORD = "very_secret_password"
    PG_HOST = "127.0.0.1"
    PG_PORT = 5432
    DB_NAME = "cursor_grocery_store_db"
    SQLALCHEMY_DATABASE_URI = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
