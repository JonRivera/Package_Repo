""" Package1 - a collection of Car Classes """


class Car:
    """makes a car class"""

    def __init__(self, mpg=40, horsepower=170, price=25000, color='red'):
        self.mpg = mpg
        self.horsepower = horsepower
        self.price = price
        self.color = color

    def sound(self):
        return "ROOOM"


class Ferrari(Car):
    """ Uses class enheritance to make Ferrari"""

    def __init__(self, mpg, horsepower, price, color, edition='sport'):
        super().__init__(mpg, horsepower, price, color)
        self.edition = edition

    def sound(self):
        return "boom --VROOM"
