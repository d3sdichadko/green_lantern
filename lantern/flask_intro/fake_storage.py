from itertools import count
from store_app import NoSuchUserError, NoSuchGoodError, NoSuchStoreError


class FakeStorage:
    def __init__(self):
        self._users = FakeUsers()
        self._goods = FakeGoods()
        self._store = FakeStores()

    @property
    def users(self):
        return self._users

    @property
    def goods(self):
        return self._goods

    @property
    def store(self):
        return self._store


class FakeUsers:
    def __init__(self):
        self._users = {}
        self._id_counter = count()

    def add(self, user):
        user_id = next(self._id_counter)
        self._users[user_id] = user
        return user_id

    def get_user_by_id(self, user_id):
        try:
            return self._users[user_id]
        except KeyError:
            raise NoSuchUserError(user_id)

    def update_user_by_id(self, user_id, user):
        if user_id in self._users:
            self._users[user_id] = user
        else:
            raise NoSuchUserError(user_id)


class FakeGoods:
    def __init__(self):
        self._goods = {}
        self._id_goods = count()

    def add(self, good):
        good_id = next(self._id_goods)
        self._goods[good_id] = good
        return good_id

    def get_good_by_id(self, good_id):
        try:
            return self._goods[good_id]
        except KeyError:
            raise NoSuchGoodError(good_id)

    def update_good_by_id(self, good_id, good):
        # __import__("pdb").set_trace()
        if good_id in self._goods:
            self._goods[good_id] = good
        else:
            return f"No such {good}"


class FakeStores:
    def __init__(self):
        self._store = {}
        self._id_stores = count()

    def add(self, store):
        store_id = next(self._id_stores)
        self._store[store_id] = store
        return store_id

    def get_store_by_id(self, store_id):
        try:
            return self._store[store_id]
        except KeyError:
            raise NoSuchStoreError(store_id)

    def update_store_by_id(self, store_id, store):
        # __import__("pdb").set_trace()
        if store_id in self._store:
            self._store[store_id] = store
        else:
            return f"No such {store}"
