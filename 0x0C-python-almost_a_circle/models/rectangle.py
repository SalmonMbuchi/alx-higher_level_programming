#!/usr/bin/python3
"""write a class that inherits from Base"""

from models.base import Base


class Rectangle(Base):
    """inherits from base, contains private attributes"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """call super() to access Base class attributes"""
        super().__init__(id)
        if type(width) != int:
            raise TypeError('width must be an integer')
        if type(height) != int:
            raise TypeError('height must be an integer')
        if type(x) != int:
            raise TypeError('x must be an integer')
        if type(y) != int:
            raise TypeError('y must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        if height <= 0:
            raise ValueError('height must be > 0')
        if x < 0:
            raise ValueError('x must be >= 0')
        if y < 0:
            raise ValueError('y must be >= 0')

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    # getter for width
    @property
    def width(self):
        """get the width"""
        return self.__width

    # setter for width
    @width.setter
    def width(self, value):
        """set the width"""
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    # getter for height
    @property
    def height(self):
        """get the height"""
        return self.__height

    # setter for height
    @height.setter
    def height(self, value):
        """get the height"""
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')

        self.__height = value

    # getter for x
    @property
    def x(self):
        """get value of x"""
        return self.__x

    # setter for x
    @x.setter
    def x(self, value):
        """set the value of x"""
        if type(value) != int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    # getter for y
    @property
    def y(self):
        """get the value of y"""
        return self.__y

    # setter for y
    @y.setter
    def y(self, value):
        """set the value for y"""
        if type(value) != int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    # public method to get the area
    def area(self):
        """return rectangle area"""
        return self.__width * self.__height

    # print the rectangle instance to stdout
    def display(self):
        """print instance using #"""
        for row in range(self.__height):
            for col in range(self.__width):
                print('#', end='')
            print()

    # update attributes via non-keyword arguments
    def update(self, *args):
        """update rectangle instance"""
        if len(args) == 1:
            self.id = args[0]
        if len(args) == 2:
            self.id = args[0]
            self.__width = args[1]
        if len(args) == 3:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
        if len(args) == 4:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
            self.__x = args[3]
        if len(args) == 5:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
            self.__x = args[3]
            self.__y = args[4]

    # return the dictionary representation of a Rectangle
    def to_dictionary(self):
        return {'x': self.__x, 'y': self.__y, 'id': self.id,
                'height': self.__height, 'width': self.__width}

    # print out readable format of rectangle instance
    def __str__(self):
        """print readable format"""
        return '[Rectangle]({}) {}/{() - {}/{}' .format(self.id,
                                                        self.__y,
                                                        self.__width,
                                                        self.__height)