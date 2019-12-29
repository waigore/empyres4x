import math

from .func import *

class Hex(object):
    def __init__(self, map, aPoint, **kwargs):
        self.map = map
        self.aPoint = aPoint

class GameMap(object):
    def __init__(self, **kwargs):
        self.numCols = kwargs.setdefault('numCols', 13)
        self.numRows = kwargs.setdefault('numCols', 12)
        self.isStaggered = kwargs.setdefault('isStaggered', True)

        self.initHexes()

    def initHexes(self):
        self.hexes = []
        for i in range(self.numRows):
            row = []
            for j in range(self.numCols):
                if self.isStaggered and j == self.numCols - 1 and i % 2 != 0:
                    row.append(None)
                else:
                    aPoint = APoint(-(i//2)+j, i)
                    hex = Hex(self, aPoint)
                    row.append(hex)
            self.hexes.append(row)
