# create a Motor class and create a Car class that "Has A" Motor


class Motor:
    def __init__(self, make, cubic_centimeters):
        self.make = make
        self.cubic_centimeters = cubic_centimeters


class Car:
    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        self.engine = engine


car = Car("Honda", "civic", Motor("Honder", 120))

print(car.engine.cubic_centimeters)
