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
        assert resp.json == {'good_id': 0}

    def test_successful_get_goods(self):
        resp = self.client.post(
            '/goods',
            json={"name": "Water", "price": 10}
        )
        # _import__("pdb").set_trace()
        good_id = resp.json['good_id']
        resp = self.client.get(f'/goods/{good_id}')
        assert resp.status_code == 200
        assert resp.json == {"name": "Water", "price": 10}

    def test_get_unexistent_good(self):
        resp = self.client.get(f'/goods/1')
        assert resp.status_code == 404
        assert resp.json == {'error': 'No such good_id 1'}

    def test_successful_update_good(self):
        resp = self.client.post(
            '/goods',
            json={"name": "Water", "price": 10}
        )
        good_id = resp.json['good_id']
        resp = self.client.put(
            f'/goods/{good_id}',
            json={"name": "Water", "price": 15}
        )
        assert resp.status_code == 200
        assert resp.json == {'successfully_updated': 0}


class TestStore(Initializer):
    def test_create_store(self):
        resp = self.client.post(
            '/store',
            json={'name': 'Mad Cow', 'location': 'Lviv', 'manager_id': 2}
        )
        assert resp.status_code == 200
        assert resp.json == {'store_id': 0}

    def test_successful_get_store(self):
        resp = self.client.post(
            '/store',
            json={"name": "Mad Cow", "location": "Lviv", "manager_id": 2}
        )
        # _import__("pdb").set_trace()
        store_id = resp.json['store_id']
        resp = self.client.get(f'/store/{store_id}')
        assert resp.status_code == 200
        assert resp.json == {"name": "Mad Cow", "location": "Lviv", "manager_id": 2}

    def test_get_unexistent_store(self):
        resp = self.client.get(f'/store/1')
        assert resp.status_code == 404
        assert resp.json == {'error': 'No such store_id 1'}

    def test_successful_update_store(self):
        resp = self.client.post(
            '/store',
            json={"name": "Mega Market", "location": "Kyiv", "manager_id": 3}
        )
        store_id = resp.json['store_id']
        resp = self.client.put(
            f'/store/{store_id}',
            json={"name": "Big Shop", "location": "Dnipro", "manager_id": 4}
        )
        assert resp.status_code == 200
        assert resp.json == {"successfully_updated": 0}
