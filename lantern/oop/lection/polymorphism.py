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
    pass


if __name__ == "__main__":
    # petya = Cat()
    # print(petya.sound())
    #
    # simba = Lion()
    # print(simba.sound())

    sherhan = Tiger()
    puhh_tigra = Tiger()
    print(sherhan.sound())

    print(f"Type of sherhan is {type(sherhan)}")
    print(f"Type of Tiger is {type(Tiger)}")

    print(f"Id of Tiger {id(Tiger)}")

    print(f"Id of sherhan {id(sherhan)}")
    print(f"Id of puhh_tigra {id(puhh_tigra)}")


