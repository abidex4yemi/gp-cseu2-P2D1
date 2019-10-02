# create a basic Animal class add some getter and setter methods
class Animal:
    def __init__(self, name, number_of_legs):
        self.name = name
        self.number_of_legs = number_of_legs

    def get_name(self):
        return self.name

    def get_number_of_legs(self):
        return self.number_of_legs

    def set_name(self, name):
        self.name = name

    def set_number_of_leg(self, number_of_legs):
        self.number_of_legs = number_of_legs

    def __str__(self):
        return f"Name: {self.name}, Number of legs: {self.number_of_legs}"


Bob = Animal("Bob", 2)
print(Bob)
