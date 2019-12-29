import math

from .func import *
from .region import (
    HomeRegionYellow,
)
from empyres.core.player import PlayerColors

class Hex(object):
    def __init__(self, map, aPoint, **kwargs):
        self.map = map
        self.aPoint = aPoint

    def containingHomeRegion(self):
        homeRegions = self.map.getAllHomeRegions()
        for homeRegion in homeRegions:
            if homeRegion.contains(self.aPoint):
                return homeRegion
        return None

    def homeRegionBorders(self):
        homeRegion = self.containingHomeRegion()
        if homeRegion is None: return None, []
        if not homeRegion.onBorder(self.aPoint): return homeRegion.name, []
        return homeRegion.name, homeRegion.borderPoints[self.aPoint]

class GameMap(object):
    HexRegionsHome = 'HexRegionsHome'
    def __init__(self, **kwargs):
        self.numCols = kwargs.setdefault('numCols', 13)
        self.numRows = kwargs.setdefault('numCols', 12)
        self.isStaggered = kwargs.setdefault('isStaggered', True)

        self.mapRegions = {}

        self.initHexes()
        self.initHomeRegions()

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

    def getHexAt(self, aPoint):
        q, r = aPoint
        if r < 0 or r >= self.numRows:
            return None
        if q + (r//2) < 0 or q + (r//2) >= self.numCols:
            return None
        return self.hexes[r][q + (r//2)]

    def initHomeRegions(self):
        self.mapRegions[GameMap.HexRegionsHome] = {
            PlayerColors.Yellow: HomeRegionYellow
        }

    def getAllHomeRegions(self):
        return self.mapRegions[GameMap.HexRegionsHome].values()

    def getHomeRegionHexes(self, playerColor):
        homeRegion = self.mapRegions[GameMap.HexRegionsHome][playerColor]
        hexList = []
        for aPoint in homeRegion.aPoints:
            hexList.append(self.getHexAt(aPoint))
        return hexList
