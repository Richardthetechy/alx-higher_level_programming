#!/usr/bin/python3
class Square:
    """Square Class"""
    def __init__(self, size=0):
        """Initialize Square with size
            Args:
                size (int)
        """
        self.size = size
    
    @property
    def size(self):
        """Return __size"""
        return self.__size
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    def area(self):
        """Compute area of squar"""
        return self.__size ** 2
