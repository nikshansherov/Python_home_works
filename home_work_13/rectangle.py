from my_except import MyValueError


class Rectangle:
    def __init__(self, length, width=None):
        self.length = length
        if self.length <= 0:
            raise MyValueError(self.length)
        if width is None:
            self.width = length
        else:
            self.width = width
            if self.width <= 0:
                raise MyValueError(self.width)

    def ge_perim(self):
        return 2 * (self.width + self.length)

    def sq(self):
        return 2 * (self.width + self.length)


r = Rectangle(2, -3)
print(r.ge_perim())
