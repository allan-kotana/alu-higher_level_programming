#!/usr/bin/python3
"""Module that defines the Student class with filtered JSON export."""


class Student:
    """Class that defines a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the Student."""
        if attrs is None:
            return self.__dict__
        return {
            key: self.__dict__[key] for key in attrs if key in self.__dict__
        }
