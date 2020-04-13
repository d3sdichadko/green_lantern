class Engine:

    def __init__(self, fuel):
        self.fuel = fuel

    def move(self):
        print(f"I am using {self.fuel} to move")


class Transport:

    def __init__(self, number_of_wheel, engine):
        self.engine = engine
        self.number_of_wheel = number_of_wheel

    def move(self):
        self.engine.move()


# diesel
# gasoline

class Truck(Transport):

    def __init__(self, number_of_wheel):
        engine = Engine(fuel="Diesel")
        super().__init__(number_of_wheel, engine)


class Car(Transport):
    def __init__(self, number_of_wheel):
        engine = Engine(fuel="gasoline")
        super().__init__(number_of_wheel, engine)


if __name__ == "__main__":

    ford = Car(number_of_wheel=4)

    optimus_prime = Truck(number_of_wheel=8)

    ford.move()

    optimus_prime.move()
