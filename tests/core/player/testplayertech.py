import unittest
from empyres.core.player import (
    PlayerTechnology,
    PlayerTechTypes
)
from empyres.core.tech import (
    ShipSizeTechs,
    AttackTechs
)

class TestPlayerTech(unittest.TestCase):
    def setUp(self):
        self.playerTech = PlayerTechnology()

    def test_techUpgradeWorks(self):
        shipSizeTech = self.playerTech.getTech(PlayerTechTypes.ShipSize)
        self.assertTrue(shipSizeTech == ShipSizeTechs.I)
        self.assertTrue(self.playerTech.techUpgradable(PlayerTechTypes.ShipSize))

        self.playerTech.upgradeTech(PlayerTechTypes.ShipSize)
        shipSizeTech = self.playerTech.getTech(PlayerTechTypes.ShipSize)
        self.assertTrue(shipSizeTech == ShipSizeTechs.II)

        #II -> VI
        self.playerTech.upgradeTech(PlayerTechTypes.ShipSize)
        self.playerTech.upgradeTech(PlayerTechTypes.ShipSize)
        self.playerTech.upgradeTech(PlayerTechTypes.ShipSize)
        self.playerTech.upgradeTech(PlayerTechTypes.ShipSize)
        self.assertTrue(not self.playerTech.techUpgradable(PlayerTechTypes.ShipSize))

        attackTech = self.playerTech.getTech(PlayerTechTypes.Attack)
        self.assertTrue(attackTech == AttackTechs.O)
