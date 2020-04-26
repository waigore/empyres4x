import collections

class CPoint(collections.namedtuple('CPoint', ['x', 'y'])):
    __slots__ = ()

    def __str__(self):
        return '(%d, %d)' % (self.x, self.y)

class APoint(collections.namedtuple('APoint', ['q', 'r'])):
    __slots__ = ()

    def allHexNeighbors(self):
        return [APoint(self.q + d.q, self.r + d.r) for d in AxialDirections]

    def __str__(self):
        return '(%d, %d)' % (self.q, self.r)

AxialDirections = [
    APoint(1, 0), APoint(0, 1), APoint(-1, 1),
    APoint(-1, 0), APoint(0, -1), APoint(1, -1),
]

def hexDirection(d):
    return AxialDirections[d]

def hexNeighbor(aPoint, i):
    _d = hexDirection(i)
    return APoint(aPoint.q + _d.q, aPoint.r + _d.r)
