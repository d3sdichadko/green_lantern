from grocery_store.app import make_app, make_db, make_manager
from grocery_store.config import Config
from flask_migrate import Migrate


app = make_app()
db = make_db(app)
migrate = Migrate(app, db)
manager = make_manager(app)


__all__ = ["app", "db", "manager"]
