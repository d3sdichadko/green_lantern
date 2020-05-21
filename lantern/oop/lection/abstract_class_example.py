from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    @abstractmethod
    def sound(self):
        pass

    def get_weight(self):
        return self.weight


class BitCat:

    def say_bug_mya(self):
        return "Roooar"


class Dog(Animal):

    def sound(self):
        return "Bark"


if __name__ == "__main__":
    animal = Animal(name="H", weight=2)
