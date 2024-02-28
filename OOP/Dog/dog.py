"""Module to make classes"""

class Dog:
    """Class representing a Dog"""
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def descriptions(self):
        """Return formatted string with dog's name and age"""
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        """Return the sound of the dog"""
        return f"{self.name} says {sound}"
    