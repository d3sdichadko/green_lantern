from grocery_store.makers import make_app, make_db, make_manager, make_login_manager
from grocery_store.config import Config
from flask_migrate import Migrate


app = make_app()
db = make_db(app)
migrate = Migrate(app, db)
manager = make_manager(app)
login_manager = make_login_manager(app)

__all__ = ["app", "db", "manager"]
