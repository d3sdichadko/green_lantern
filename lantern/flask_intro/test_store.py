import inject

from store_app import app
from fake_storage import FakeStorage


def configure_test(binder):
    db = FakeStorage()
    binder.bind('DB', db)


class Initializer:
    def setup(self):
        inject.clear_and_configure(configure_test)

        app.config['TESTING'] = True
        with app.test_client() as client:
            self.client = client


class TestUsers(Initializer):
    def test_create_new(self):
        resp = self.client.post(
            '/users',
            json={'name': 'John Doe'}
        )
        assert resp.status_code == 201
        assert resp.json == {'user_id': 0}

    def test_successful_get_user(self):
        resp = self.client.post(
            '/users',
            json={'name': 'John Doe'}
        )
        user_id = resp.json['user_id']
        resp = self.client.get(f'/users/{user_id}')
        assert resp.status_code == 200
        assert resp.json == {'name': 'John Doe'}

    def test_get_unexistent_user(self):
        resp = self.client.get(f'/users/1')
        assert resp.status_code == 404
        assert resp.json == {'error': 'No such user_id 1'}

    def test_successful_update_user(self):
        resp = self.client.post(
            '/users',
            json={'name': 'John Doe'}
        )
        user_id = resp.json['user_id']
        resp = self.client.put(
            f'/users/{user_id}',
            json={'name': 'Johanna Doe'}
        )
        assert resp.status_code == 200
        # assert resp.json == {'name': 'Johanna Doe'}
        assert resp.json == {'status': 'success'}

    def test_unsuccesful_update(self):
        resp = self.client.put(
            f'/users/1',
            json={'name': 'Johanna Doe'}
        )
        assert resp.status_code == 404
        assert resp.json == {'error': 'No such user_id 1'}


class TestGoods(Initializer):
    def test_create_goods(self):
        resp = self.client.post(
            '/goods',
            json={'name': 'Chocolate_bar', 'price': 10}
        )
        assert resp.status_code == 200
        assert resp.json == {'numbers_of_item_created': 1}
