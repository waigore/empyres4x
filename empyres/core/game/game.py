import logging
from .state import GameSM
from empyres.core.phase import (
    getGamePhaseByName
)
from empyres.core.player import (
    Player,
    PlayerColors
)
from empyres.core.map.region import (
    HomeRegionRed,
    HomeRegionBlue,
    HomeRegionGreen,
    HomeRegionYellow
)

logger = logging.getLogger(__name__)

class GamePlayerIterator(object):
    def __init__(self, playerOrder, players):
        self.playerOrder = playerOrder
        self.players = players

    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        if self.count >= len(self.playerOrder):
            raise StopIteration
        playerColor = self.playerOrder[self.count]
        self.count += 1
        return self.players[playerColor]


class Game(object):
    def __init__(self):
        self.sm = GameSM(self)
        self.initPlayers()

        #logger.info('Game set up with {} players'.format(len(self.playerOrder)))

    def initPlayers(self):
        pGreen = Player('Green', PlayerColors.Green, HomeRegionGreen)
        pYellow = Player('Yellow', PlayerColors.Yellow, HomeRegionYellow)
        pBlue = Player('Blue', PlayerColors.Blue, HomeRegionBlue)
        pRed = Player('Red', PlayerColors.Red, HomeRegionRed)

        self.players = {
            PlayerColors.Green: pGreen,
            PlayerColors.Yellow: pYellow,
            PlayerColors.Blue: pBlue,
            PlayerColors.Red: pRed
        }
        self.playerOrder = [c for c in PlayerColors.ordered()]

    def iterPlayers(self):
        return GamePlayerIterator(self.playerOrder, self.players)

    @property
    def currentGamePhase(self):
        return getGamePhaseByName(self.sm.state)
