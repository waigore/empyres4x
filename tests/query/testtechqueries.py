import unittest
from empyres.query.tech import QueryPlayerTechCanBuildShip
from empyres.core.unit import ShipTypes
from empyres.core.game import Game
from empyres.core.player import PlayerColors

class TestTechQueries(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_queryPlayerTechCanBuildScout(self):
        pRed = self.game.getPlayer(PlayerColors.Red)
        q = QueryPlayerTechCanBuildShip(ShipTypes.Scout)
        val = q.execute(self.game, pRed)

        self.assertTrue(val)

    def test_queryPlayerTechCanbuildDreadnaught(self):
        pRed = self.game.getPlayer(PlayerColors.Red)
        q = QueryPlayerTechCanBuildShip(ShipTypes.Dreadnaught)
        val = q.execute(self.game, pRed)

        self.assertFalse(val)
