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
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Area.

        Returns:
            size.
        """
        return self.__size ** 2
