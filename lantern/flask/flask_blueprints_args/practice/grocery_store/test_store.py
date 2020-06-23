import inject

from fake_storage import FakeStorage
from store_app import make_app


def configure_test(binder):
    db = FakeStorage()
    binder.bind('DB', db)


class Initializer:
    def setup(self):
        inject.clear_and_configure(configure_test)
        app = make_app()
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
        assert resp.json == {'user_id': 1}

        resp = self.client.post(
            '/users',
            json={'name': 'Andrew Derkach'}
        )
        assert resp.json == {'user_id': 2}

    def test_successful_get_user(self):
        resp = self.client.post(
            '/users',
            json={'name': 'John Doe'}
        )
        user_id = resp.json['user_id']
        resp = self.client.get(f'/users/{user_id}')
        assert resp.status_code == 200
        assert resp.json == {'name': 'John Doe'}

    def test_get_unexist_user(self):
        resp = self.client.get(f'/users/1')
        assert resp.status_code == 404
        assert resp.json == {'error': 'No such user_id 1'}

    def test_unexist_update_user(self):
        resp = self.client.put(
            '/users/1',
            json={'name': 'Johanna Doe'}
        )
        assert resp.status_code == 404
        assert resp.json == {'error': 'No such user_id 1'}


class TestGoods(Initializer):
    TEST_GOODS = (
        ('Milk Happy Cow', 100),
        ('Dirty Monkey soda', 30),
        ('Toilet paper', 3000),
    )

    def _post_goods(self):
        return self.client.post(
            '/goods',
            json=[
                {'name': name, 'price': price}
                for name, price in self.TEST_GOODS
            ]
        )

    def test_create_new(self):
        resp = self._post_goods()
        assert resp.status_code == 201
        assert resp.json == {'number of items created': 3}

    def test_get_goods(self):
        self._post_goods()
        resp = self.client.get('/goods')
        assert resp.status_code == 200
        assert resp.json == [
            {'name': 'Milk Happy Cow', 'price': 100, 'id': 1},
            {'name': 'Dirty Monkey soda', 'price': 30, 'id': 2},
            {'name': 'Toilet paper', 'price': 3000, 'id': 3},
        ]


class TestStore(Initializer):
    def test_succes_post_store(self):
        resp = self.client.post(
            '/users',
            json={'name': 'John Doe'}
        )
        assert resp.status_code == 201
        assert resp.json == {'user_id': 1}

        resp = self.client.post(
            '/store',
            json={'name': 'Mad Cow',
                  'location': 'Lviv',
                  'manager_id': 1}
        )
        assert resp.status_code == 201
        assert resp.json == {'store_id': 1}

    def test_fail_post_store(self):
        resp = self.client.post(
            '/users',
            json={'name': 'John Doe'}
        )
        resp = self.client.get(f'/users/2')
        assert resp.status_code == 404
        assert resp.json == {'error': 'No such user_id 2'}

        resp = self.client.post(
            '/store',
            json={'name': 'Mad Cow',
                  'location': 'Lviv',
                  'manager_id': 2}
        )
        assert resp.status_code == 201
        assert resp.json == {'store_id': 1}

    def test_success_get_store(self):
        resp = self.client.post(
            '/users',
            json={'name': 'John Doe'}
        )
        resp = self.client.post(
            '/store',
            json={'name': 'Mad Cow', 'location': 'Lviv', 'manager_id': 1}
        )
        store_id = resp.json['store_id']
        resp = self.client.get(f'/store/{store_id}')

        assert resp.status_code == 200
        assert resp.json == {'name': 'Mad Cow', 'location': 'Lviv', 'manager_id': 1}

    def test_get_unexist_store(self):
        resp = self.client.get(f'/store/1')
        assert resp.status_code == 404
        assert resp.json == {'error': 'No such store_id 1'}

    def test_successful_update_store(self):
        resp_user = self.client.post(
            '/users',
            json={'name': 'John Doe'}
        )

        user_id = resp_user.json['user_id']

        resp_store = self.client.post(
            '/store',
            json={'name': 'Mad Cow', 'location': 'Lviv', 'manager_id': user_id}
        )

        store_id = resp_store.json['store_id']
        print(store_id)
        resp_store = self.client.put(
            f'/store/{store_id}',
            json={'name': 'Mad Deer', 'location': 'Kiev', 'manager_id': user_id}
        )
        print(resp_store)
        assert resp_store.status_code == 200
        assert resp_store.json == {'status': 'success'}
