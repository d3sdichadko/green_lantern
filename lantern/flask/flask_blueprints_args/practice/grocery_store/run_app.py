import inject

from store_app import make_app

if __name__ == '__main__':
    app = make_app()
    app.run(port=8080, debug=True)
