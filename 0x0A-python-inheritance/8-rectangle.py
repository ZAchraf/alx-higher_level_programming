#!/usr/bin/python3
'''Rectangle class. Defining a class rectangle that inherit from base geometryy'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Subclass That represents a rectangle.'''
    def __init__(self, width, height):
        '''Iniatializing a Rectangle.'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
