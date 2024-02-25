#!/usr/bin/python3
'''square, defining a rect subcl square'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Square. representing it'''
    def __init__(self, size):
        '''init a new one'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''area of the square.'''
        return self.__size * self.__size
