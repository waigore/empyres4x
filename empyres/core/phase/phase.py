from collections import OrderedDict
from transitions import Machine
from .common import *

class GamePhase(object):
    def __init__(self, name, phase, turn):
        self.name = name
        self.turn = turn
        self.phase = phase

    def phaseEnter(self, game):
        pass

    def phaseExit(self, game):
        pass

    def canExit(self, game):
        return True

class RoundStartPhase(GamePhase):
    def __init__(self):
        super(RoundStartPhase, self).__init__(RoundStartP, GamePhases.RoundStart, GameTurns.RoundStart)

class MovementPhase(GamePhase):
    def __init__(self, name, turn):
        super(MovementPhase, self).__init__(name, GamePhases.Movement, turn)

class CombatPhase(GamePhase):
    def __init__(self, name, turn):
        super(CombatPhase, self).__init__(name, GamePhases.Combat, turn)

class ExplorationPhase(GamePhase):
    def __init__(self, name, turn):
        super(ExplorationPhase, self).__init__(name, GamePhases.Exploration, turn)

class EconomicPhase(GamePhase):
    def __init__(self):
        super(EconomicPhase, self).__init__(EconP, GamePhases.Economic, GameTurns.Economic)

AllGamePhases = OrderedDict([
    (RoundStartP, RoundStartPhase()),
    (Turn1MP, MovementPhase(Turn1MP, GameTurns.Turn1)),
    (Turn1EP, ExplorationPhase(Turn1EP, GameTurns.Turn1)),
    (Turn1CP, CombatPhase(Turn1CP, GameTurns.Turn1)),
    (Turn2MP, MovementPhase(Turn2MP, GameTurns.Turn2)),
    (Turn2EP, ExplorationPhase(Turn2EP, GameTurns.Turn2)),
    (Turn2CP, CombatPhase(Turn2CP, GameTurns.Turn2)),
    (Turn3MP, MovementPhase(Turn3MP, GameTurns.Turn3)),
    (Turn3EP, ExplorationPhase(Turn2EP, GameTurns.Turn3)),
    (Turn3CP, CombatPhase(Turn2CP, GameTurns.Turn3)),
    (EconP, EconomicPhase()),
])

def gamePhaseNames():
    return list(AllGamePhases.keys())

def getGamePhaseByName(name):
    return AllGamePhases[name]
