from app.app import get_app

app = get_app()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
