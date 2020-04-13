class Engine:

    def __init__(self, fuel):
        self.fuel = fuel

    def move(self):
        print(f"I am using {self.fuel} to move")


class Transport:

    def __init__(self, number_of_wheel, engine):
        self.engine = engine
        self.number_of_wheel = number_of_wheel

    def move_this(self):
        self.engine.move()


class Truck(Transport):

    def __init__(self, number_of_wheel, engine):
        super().__init__(number_of_wheel, engine)


class Car(Transport):
    def __init__(self, number_of_wheel, engine):
        super().__init__(number_of_wheel, engine)


def check_engine_type(transport):
    print(f"type of {transport.engine}")


class Moto:
    pass


if __name__ == "__main__":
    gasoline_engine = Engine(fuel="gasoline")
    diesel_engine = Engine(fuel="diesel")

    ford = Car(number_of_wheel=4, engine=gasoline_engine)

    optimus_prime = Truck(number_of_wheel=8, engine=diesel_engine)

    ford.move_this()

    optimus_prime.move_this()

    print("\n" * 10)
    check_engine_type(ford)
    check_engine_type(optimus_prime)
    # check_engine_type(Moto())
