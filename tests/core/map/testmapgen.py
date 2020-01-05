import unittest
from empyres.core.map import (
    SystemMarkerGen,
    GameMap
)

class TestMapGen(unittest.TestCase):
    def setUp(self):
        self.map = GameMap()
        systemMarkerGen = SystemMarkerGen(self.map)
        systemMarkerGen.populateMap()

    def test_generateMapWithNormalProfile(self):
        for row in self.map.hexes:
            for hex in row:
                if hex is not None:
                    self.assertTrue(hex is not None)
