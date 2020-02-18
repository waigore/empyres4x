import unittest
from empyres.core.player import (
    PlayerFleets,
    PlayerTechnology,
)
from empyres.core.unit import (
    ShipGroup,
    ScoutShipType,
    DestroyerShipType
)

class TestPlayerFleets(unittest.TestCase):
    def setUp(self):
        self.playerFleets = PlayerFleets()
        self.playerTech = PlayerTechnology()

    def test_addShips(self):
        shipGroup = ShipGroup(ScoutShipType, self.playerTech.snapshot())
        for i in range(5):
            shipGroup.addShip()
        self.assertTrue(shipGroup.numShips == 5)

        for i in range(5):
            shipGroup.removeShip()
        self.assertTrue(shipGroup.numShips == 0)

    def test_addShipGroup(self):
        shipGroup = ShipGroup(DestroyerShipType, self.playerTech.snapshot())
        self.playerFleets.addShipGroup(shipGroup)
        
