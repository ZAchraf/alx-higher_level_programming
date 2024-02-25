#!/usr/bin/python3
'''BaseGeometry. Defining a base geometry'''


class BaseGeometry:
    '''represents BaseGeometry class.'''
    def area(self):
        '''not implemeented yet.'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''Validating value type.'''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
