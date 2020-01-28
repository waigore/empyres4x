import unittest
from empyres.core.game import Game
from empyres.core.phase import RoundStartP
from empyres.core.player import PlayerColors

class TestGameWithPlayers(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_playerDefOrdering(self):
        playerColors = [p.color for p in self.game.iterPlayers()]
        self.assertListEqual(playerColors, PlayerColors.ordered())

    def test_initialGamePhase(self):
        phase = self.game.currentGamePhase
        self.assertEqual(phase.name, RoundStartP)
