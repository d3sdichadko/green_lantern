class Asteroid:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Robot:
    def __init__(self, x, y, asteroid):
        self.x = x
        self.y = y
        self.asteroid = asteroid
        if self.x > self.asteroid.x:
            raise MissAsteroidError()


class MissAsteroidError(Exception):
    pass
