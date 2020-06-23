from abc import ABC, abstractmethod


class Animal(ABC):

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    @abstractmethod
    def sound(self):
        pass


class BitCat:

    def say_bug_mya(self):
        return "Roooar"


class Dog(Animal):

    def sound(self):
        return "Bark"


class Cat(Animal, BitCat):

    def sound(self):
        return "Meow"


if __name__ == "__main__":
    dog = Dog(name="Rex", weight=50)
    cat = Cat(name="Simba", weight=100)

    print(f"{dog.name} say {dog.sound()}")
    print(f"{cat.name} say {cat.sound()}")

    print(cat.say_bug_mya())