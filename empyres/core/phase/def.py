from .common import GameTurns, GamePhases

class GamePhase(object):
    def __init__(self, game, name, turn, phase):
        self.game = game
        self.name = name
        self.turn = turn
        self.phase = phase

    def phaseEnter(self):
        pass

    def phaseExit(self):
        pass

    def nextPhase(self):
        self.game.nextPhase()

    def canExit(self):
        return True

class MovementPhase(GamePhase):
    def __init__(self, game, turn):
        super(MovementPhase, self).__init__(game, GamePhases.Movement, turn)

class CombatPhase(GamePhase):
    def __init__(self, game, turn):
        super(CombatPhase, self).__init__(game, GamePhases.Combat, turn)

class ExplorationPhase(GamePhase):
    def __init__(self, game, turn):
        super(ExplorationPhase, self).__init__(game, GamePhases.Exploration, turn)
