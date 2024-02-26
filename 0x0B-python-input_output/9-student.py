#!/usr/bin/python3
"""student class."""


class Student:
    """student rep."""

    def __init__(self, first_name, last_name, age):
        """new Student init"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """dict rep of the Student."""
        return self.__dict__
