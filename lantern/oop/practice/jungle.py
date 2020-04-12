from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List


class Jungle:
    def __init__(self, predators: List[Predator], herbivorous: List[Herbivorous]):
        self.predators = predators
        self.herbivorous = herbivorous


JUNGLE = Jungle(predators=[], herbivorous=[])


class Animal(ABC):
    def __init__(self, weight, speed):
        self.weight = weight
        self.speed = speed

    @abstractmethod
    def eat(self):
        raise NotImplementedError


class Predator(Animal):
    def __init__(self, weight, speed, power):
        super().__init__(weight, speed)
        self.power = power

    def __hunt(self):
        for herb in JUNGLE.herbivorous:
            if self.is_herb_a_victim(herb):
                return True
        return False

    def speed_of_herb_in_percent(self, herb: Herbivorous):
        return int(herb.speed * 100 / self.speed)

    def is_herb_a_victim(self, herb: Herbivorous):
        return self.power * 3 > herb.weight and self.speed * 1.15 > herb.speed

    def eat(self):
        return self.__hunt()


class Herbivorous(Animal):
    def eat(self):
        pass


if __name__ == "__main__":
    # testing predator's possibility to hunt herbivorous

    simba = Predator(weight=100, speed=100, power=70)
    timon = Herbivorous(weight=10, speed=114)

    JUNGLE.predators.append(simba)
    JUNGLE.herbivorous.append(timon)
    try:
        print(simba.hunt())
    except AttributeError:
        print("Method hunt is hidden")
    # end of testing

    #  testing eat method
    print(simba.eat())

    # test animal of abstract class
    try:
        animal = Animal(weight=5, speed=10)
    except TypeError:
        print("All is OK")
    else:
        print("Something goes wrong. Animal should be abstract")
