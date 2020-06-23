from application import create_app
from flask import current_app

app = create_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=current_app.config['DEBUG'])
