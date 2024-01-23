#!/usr/bin/python3
"""this is square module"""


class Square:
    """ defining it"""
    
    def __init__(self, size=0):
        """Constructor.

        Args:
            size: length of the side.
        
        Raises:
            TypeError: size != integer
            ValueError: size < 0
        """
        if not isinstance(size, int):
            raise TypeError('the size should be int')
        if size < 0:
            raise ValueError('size should be bigger or equal to 0')
        self.__size = size
