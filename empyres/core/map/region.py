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
