import logging


class Cat:

    def __init__(self, name):
        self._name = name
        self.__name = name

    def get_name(self):
        return self._name


class SmallCat(Cat):

    def get_private_name(self):
        return self._name


if __name__ == "__main__":
    cat = Cat(name="Simba")
    print(cat.get_name())
    print(cat._name)

    small_cat = SmallCat(name="Petya")
    print(small_cat.get_private_name())
