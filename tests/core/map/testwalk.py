import unittest
from empyres.core.map.walk import (
    CostBoundedWalk
)
from empyres.core.map import (
    SystemMarkerGen,
    GameMap
)
from empyres.core.map.func import (
    APoint
)

def walkCost(fromPoint, toPoint):
    return 1

def containsAllPoints(results, points):
    return len(set(points).difference(set(results))) == 0

class TestWalk(unittest.TestCase):
    def setUp(self):
        self.map = GameMap()
        systemMarkerGen = SystemMarkerGen(self.map)
        systemMarkerGen.populateMap()

    def test_walkWorks(self):
        walk = CostBoundedWalk(APoint(1, 1), 1, self.map.isOob, walkCost)
        results = walk.do()
        self.assertTrue(containsAllPoints(results, [APoint(1, 0), APoint(2, 0), APoint(2, 1), APoint(1, 2), APoint(0, 2), APoint(0, 1)]))

    def test_walkWorksFor2(self):
        walk = CostBoundedWalk(APoint(1, 1), 2, self.map.isOob, walkCost)
        results = walk.do()
        self.assertTrue(APoint(3, 1) in results)
        self.assertTrue(APoint(1, 2) in results)
        self.assertTrue(APoint(1, -1) not in results)
