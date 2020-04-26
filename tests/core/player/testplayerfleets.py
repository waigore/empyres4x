import unittest
from empyres.core.player import (
    PlayerFleets,
    PlayerTechnology,
    PlayerColors
)
from empyres.core.unit import (
    ShipGroup,
    ScoutShipType,
    DestroyerShipType
)
from empyres.core.map import (
    APoint
)

class TestPlayerFleets(unittest.TestCase):
    def setUp(self):
        self.playerFleets = PlayerFleets(PlayerColors.Red)
        self.playerTech = PlayerTechnology(PlayerColors.Red)

    def test_addShips(self):
        shipGroup = ShipGroup(ScoutShipType, self.playerTech.snapshot())
        for i in range(5):
            shipGroup.addShip()
        self.assertTrue(shipGroup.numShips == 5)

        for i in range(5):
            shipGroup.removeShip()
        self.assertTrue(shipGroup.numShips == 0)

    def test_addFleet(self):
        shipGroup = ShipGroup(DestroyerShipType, self.playerTech.snapshot())
        self.playerFleets.createFleetAt(APoint(1, 1), shipGroup)
