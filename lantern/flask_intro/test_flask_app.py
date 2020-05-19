from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return 'hello'


def test_simple():
    app.config['TESTING'] = True
    with app.test_client() as client:
        response = client.get('/')
        __import__("pdb").set_trace()
        print(response)



