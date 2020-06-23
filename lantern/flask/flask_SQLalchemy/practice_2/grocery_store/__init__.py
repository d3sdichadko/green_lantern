from grocery_store.app import make_app, make_db


app = make_app()
db = make_db(app)

__all__ = ["app", "db"]
