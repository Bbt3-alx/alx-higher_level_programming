#!/usr/bin/python3
"""The square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """A class that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialization of the Square"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Get size"""
        return self.width

    @size.setter
    def size(self, value):
        """ Set size """
        self.width = value
        self.height = value

    def __str__(self):
        """Overwrite the method str"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        """assigns attributes: *args and **kwargs"""
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.size = args[1]
        if len(args) >= 3:
            self.x = args[2]
        if len(args) >= 4:
            self.y = args[3]
        else:
            self.id = kwargs.get('id', self.id)
            self.size = kwargs.get('size', self.size)
            self.x = kwargs.get('x', self.x)
            self.y = kwargs.get('y', self.y)

    def to_dictionary(self):
        """Return the dictionary representation of a Square"""
        return {'x' : self.x,
                'y' : self.y,
                'size' : self.size,
                'id' : self.id
                }
