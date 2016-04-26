from . import utils

class Point(object):
    def __init__(self, x, y, mark={}):
        self.x = x
        self.y = y
        self.mark = mark

    #implement magic methods

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __neg__(self):
        return Point(-self.x, -self.y)

    def coincidentPoint(self, point1):
        point2 = (self.x, self.y)
        return utils.check_coincident(point1, point2)

    def shiftPoint(self,xShift, yShift):
        thePoint = (self.x, self.y)
        self.x, self.y = utils.shift_point(thePoint,xShift,yShift)