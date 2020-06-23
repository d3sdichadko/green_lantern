from itertools import count

from errors import NoSuchUserError, NoSuchStoreError


class Repository:
    def __init__(self):
        self._db = {}
        self._id_counter = count(1)

    def add(self, item):
        item_id = next(self._id_counter)
        self._db[item_id] = item
        return item_id


class FakeStorage:
    def __init__(self):
        self._users = FakeUsers()
        self._goods = FakeGoods()
        self._stores = FakeStores()

    @property
    def users(self):
        return self._users

    @property
    def goods(self):
        return self._goods

    @property
    def stores(self):
        return self._stores


class FakeUsers(Repository):
    def get_user_by_id(self, user_id):
        try:
            return self._db[user_id]
        except KeyError:
            raise NoSuchUserError(user_id)

    def update_user_by_id(self, user_id, user):
        if user_id in self._db:
            self._db[user_id] = user
        else:
            raise NoSuchUserError(user_id)


class FakeGoods(Repository):
    def add_many(self, items):
        for item in items:
            self.add(item)
        return len(items)

    def get_all(self):
        return [
            {**item, 'id': item_id} for item_id, item in self._db.items()
        ]


class FakeStores(Repository):

    def get_store_by_id(self, store_id):
        try:
            return self._db[store_id]
        except KeyError:
            raise NoSuchStoreError(store_id)

    def update_store_by_id(self, store_id, store):
        if store_id in self._db:
            self._db[store_id] = store
        else:
            raise NoSuchStoreError(store_id)
