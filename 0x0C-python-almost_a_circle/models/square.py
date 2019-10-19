#!/usr/bin/python3
""" class Square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                self.y, self.width))

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        lenofargs = len(args)
        if lenofargs > 0:
            self.id = args[0]
            lenofargs -= 1
        if lenofargs > 0:
            self.size = args[1]
            lenofargs -= 1
        if lenofargs > 0:
            self.x = args[2]
            lenofargs -= 1
        if lenofargs > 0:
            self.y = args[3]
        if kwargs:
            for key, value in kwargs.items():
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value
                if key == 'size':
                    self.width = value
                if key == 'id':
                    self.id = value

    def to_dictionary(self):
        dic1 = {}
        for key, value in self.__dict__.items():
            if 'x' in key:
                dic1['x'] = value
            if 'y' in key:
                dic1['y'] = value
            if 'id' in key:
                dic1['id'] = value
            if 'width' in key:
                dic1['size'] = value
        return dic1
