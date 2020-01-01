import enum
import functools
from .func import APoint, AxialDirections, hexNeighbor
from empyres.core.player import PlayerColors

class MapRegionType(enum.Enum):
    HomeRegion = 'HomeRegion'

class MapRegion(object):
    def __init__(self, name, regionType, aPoints):
        self.name = name
        self.regionType = regionType
        self.aPoints = aPoints

        self.initBorderPoints()

    def initBorderPoints(self):
        pts = self.allBorderPoints()
        self.borderPoints = {}
        for pt in pts:
            self.borderPoints[pt] = self.calcPointBorders(pt)

    def onBorder(self, aPoint):
        neighbors = aPoint.allHexNeighbors()
        for neighbor in neighbors:
            if neighbor not in self.aPoints:
                return True
        return False

    def contains(self, aPoint):
        return aPoint in self.aPoints

    def allBorderPoints(self):
        return [p for p in self.aPoints if self.onBorder(p)]

    def calcPointBorders(self, aPoint):
        borders = []
        for i in range(len(AxialDirections)):
            neighbor = hexNeighbor(aPoint, i)
            if not self.contains(neighbor):
                borders.append(i)
        return borders

class HomeRegion(MapRegion):
    def __init__(self, name, aPoints):
        super(HomeRegion, self).__init__(name, MapRegionType.HomeRegion, aPoints)

p = APoint

HomeRegionYellow = HomeRegion(PlayerColors.Yellow, [
    p(7, 0), p(8, 0), p(9, 0), p(10, 0), p(11, 0), p(12, 0),
    p(7, 1), p(8, 1), p(9, 1), p(10, 1), p(11, 1),
    p(7, 2), p(8, 2), p(9, 2), p(10, 2), p(11, 2),
    p(6, 3), p(7, 3), p(8, 3), p(9, 3), p(10, 3),
    p(6, 4), p(7, 4), p(8, 4), p(9, 4), p(10, 4),
])

HomeRegionGreen = HomeRegion(PlayerColors.Green, [
    p(0, 0), p(1, 0), p(2, 0), p(3, 0), p(4, 0),
    p(0, 1), p(1, 1), p(2, 1), p(3, 1), p(4, 1),
    p(-1, 2), p(0, 2), p(1, 2), p(2, 2), p(3, 2), p(4, 2),
    p(-1, 3), p(0, 3), p(1, 3), p(2, 3), p(3, 3),
    p(-2, 4), p(-1, 4), p(0, 4), p(1, 4), p(2, 4),
])

HomeRegionRed = HomeRegion(PlayerColors.Red, [
    p(-3, 7), p(-2, 7), p(-1, 7), p(0, 7), p(1, 7),
    p(-4, 8), p(-3, 8), p(-2, 8), p(-1, 8), p(0, 8),
    p(-4, 9), p(-3, 9), p(-2, 9), p(-1, 9), p(0, 9),
    p(-5, 10), p(-4, 10), p(-3, 10), p(-2, 10), p(-1, 10), p(0, 10),
    p(-5, 11), p(-4, 11), p(-3, 11), p(-2, 11), p(-1, 11),
])

HomeRegionBlue = HomeRegion(PlayerColors.Blue, [
    p(4, 7), p(5, 7), p(6, 7), p(7, 7), p(8, 7),
    p(3, 8), p(4, 8), p(5, 8), p(6, 8), p(7, 8), p(8, 8),
    p(3, 9), p(4, 9), p(5, 9), p(6, 9), p(7, 9),
    p(3, 10), p(4, 10), p(5, 10), p(6, 10), p(7, 10),
    p(2, 11), p(3, 11), p(4, 11), p(5, 11), p(6, 11),
])
