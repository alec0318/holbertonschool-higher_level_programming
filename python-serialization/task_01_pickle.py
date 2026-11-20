#!/usr/bin/env python3
import pickle

"""class CustomObject"""


class CustomObject:

    """instance method"""
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    """display method"""
    def display(self):
        print(
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Is Student: {self.is_student}"
        )

    """serialize method"""
    def serialize(self, filename):
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except (OSError, pickle.PickleError):
            return None

    """deserialize class method"""
    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except (OSError, pickle.PickleError, EOFError):
            return None
