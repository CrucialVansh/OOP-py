"""Module for class"""
class Car:
    """Class for Car
    """
    def __init__(self, colour, odometer):
        self.colour = colour
        self.odometer = odometer

    def __str__(self):
        return f"The {self.colour} car has {self.odometer} kilometers"