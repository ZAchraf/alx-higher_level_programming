#!/usr/bin/python3
"""Defining a funct that add attr to objects."""


def add_attribute(object, attr, val):
    """Adding a new attribute to object.
    Args:
        object (any): The object to which we should ass an attribute.
        attr (str): name of  attribute we should add to obj.
        val (any): att's value.
    Raises:
        TypeError: If the attribute can't be added.
    """
    if not hasattr(object, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(object, attr, val)
