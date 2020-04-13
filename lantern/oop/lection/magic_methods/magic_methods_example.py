class Cat(object):
    # pass

    def sound(self):
        return "Meow"


class Killer:

    def sound(self):
        return "Die!!!"


class Lion(Cat):
    pass

    # def sound(self):
    #     return "Roar"


class Tiger(Lion, Killer):
    def __init__(self, weight):
        # print(f"Id of self {id(self)}")
        self.weight = weight

    # def __del__(self):
    #     print(f"object dying")

    def __str__(self):
        return f"I am tiger! And my weight is {self.weight}; Be scared of me"

    def __gt__(self, other):
        return self.weight > other.weight

    def __eq__(self, other):
        return self.weight == other.weight


if __name__ == "__main__":
    sherhan = Tiger(weight=200)
    sherhan_2 = Tiger(weight=200)

    # print(f"Id of sherhan {id(sherhan)}")

    puhh_tigra = Tiger(weight=5)

    # print(f"Weight of sherhan is {sherhan.weight}")
    # print(f"Weight of puhh_tigra is {puhh_tigra.weight}")

    print(sherhan)

    print(sherhan == puhh_tigra)
    print(sherhan == sherhan_2)


