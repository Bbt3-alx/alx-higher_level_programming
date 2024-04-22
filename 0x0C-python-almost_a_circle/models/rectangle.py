#!/usr/bin/python3
"""Module rectangle"""


from models.base import Base

class Rectangle(Base):
    """class Rectangle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initiate the Rectangle"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Get the area of the Rectangle"""
        return self.__width * self.__height

    def display(self):
        """Prints in stdout the Rectangle instance with the caracter #"""
        for i in range(self.__height):
            for y in range(self.__width):
                print("#", end='')
            print()

    def __str__(self):
        """Overright the __str__ methods"""
        w = self.__width
        h = self.__height
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {w}/{h}"
