#!/usr/bin/python3
'''Rectangle class, defining a class rectangle that inherit from base geometryy'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Subclass, that represents a rectangle using base geometryy'''
    def __init__(self, width, height):
        '''A new contructor'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''this function will return the area of rectangle.'''
        return self.__width * self.__height

    def __str__(self):
        '''String  that represnts rectangle'''
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
