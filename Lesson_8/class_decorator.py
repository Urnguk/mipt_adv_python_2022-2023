class Dot:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    # def dist(self, other):
    #     d_x = self.get_x() - other.get_x()
    #     d_y = self.get_y() - other.get_y()
    #     return (d_x ** 2 + d_y ** 2) ** 0.5

    @staticmethod
    def dist(c, d):
        d_x = c.get_x() - d.get_x()
        d_y = c.get_y() - d.get_y()
        return (d_x ** 2 + d_y ** 2) ** 0.5

    @classmethod
    def init_from_tuple(cls, pair):
        return cls(pair[0], pair[1])


# def dist(c, d):
#     d_x = c.get_x() - d.get_x()
#     d_y = c.get_y() - d.get_y()
#     return (d_x ** 2 + d_y ** 2) ** 0.5


a = Dot()
b = Dot(4, 3)
p = (3, 7)
print(Dot.dist(a, b))
s = Dot.init_from_tuple(p)
print(s.get_x(), s.get_y())
# print(dist(a, b))
# print(a.dist(b))
