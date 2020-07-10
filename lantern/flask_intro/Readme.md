## HW Flask Intro

### How to prepare environment for work:
$ /opt/python/bin/python3.8 -m venv venv

$ source venv/bin/activate

$ pip install -r requirements.txt

### How to test my app:
$ pytest -xv test_store.py

### How to run this app (as development WSGI server on 0.0.0.0:5000):
$ python run_app.py 