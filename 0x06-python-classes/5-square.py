#!/usr/bin/python3
"""this is square module"""


class Square:
    """ defining it"""
    
    def __init__(self, size):
        """Constructor.

        Args:
            size: length of the side.
        """
        self.__size = size

    @property
    def size(self):
        """ the property.

        Raises:
            TypeError: size != int
            ValueError: size < 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Area.

        Returns:
            square size.
        """
        return self.__size ** 2

    def my_print(self):
        """ square printer"""
        for i in range(self.size):
            for j in range(self.size):
                print('#', end="\n" if j is self.size - 1 and i != j else "")
        print()
