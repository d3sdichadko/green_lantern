from flask import Flask
from flask_sqlalchemy import SQLAlchemy

PG_USER = "jeniatrofimenko"
PG_PASSWORD = "password"
PG_HOST = "localhost"
PG_PORT = 5432
DB_NAME = "test_orm"
SQLALCHEMY_DATABASE_URI = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{DB_NAME}"


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

db = SQLAlchemy(app)


class UserTable(db.Model):
    __tablename__ = 'user_table'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120))

    def __repr__(self):
        return '<User %r>' % self.username


class City(db.Model):
    __tablename__ = 'city_table'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user_table.id'))
    city = db.Column(db.String)


db.create_all()
db.session.commit()


@app.route("/")
def get_user_data():
    return UserTable.query.all()


if __name__ == "__main__":
    app.run()
