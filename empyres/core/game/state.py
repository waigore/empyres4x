import logging
from transitions import Machine
import empyres.core.phase as phase

logger = logging.getLogger(__name__)

class GameSM(object):
    def __init__(self, game):
        self.game = game
        m = Machine(self, states=phase.gamePhaseNames(), initial=phase.RoundStartP)
        m.add_ordered_transitions()

    def on_enter_RoundStartP(self):
        return getGamePhaseByName(phase.RoundStartP).phaseEnter(self.game)

    def on_exit_RoundStartP(self):
        return getGamePhaseByName(phase.RoundStartP).phaseExit(self.game)

    #Turn 1
    def on_enter_Turn1MP(self):
        return getGamePhaseByName(phase.Turn1MP).phaseEnter(self.game)

    def on_exit_Turn1MP(self):
        return getGamePhaseByName(phase.Turn1MP).phaseExit(self.game)

    def on_enter_Turn1EP(self):
        return getGamePhaseByName(phase.Turn1EP).phaseEnter(self.game)

    def on_exit_Turn1EP(self):
        return getGamePhaseByName(phase.Turn1EP).phaseExit(self.game)

    def on_enter_Turn1CP(self):
        return getGamePhaseByName(phase.Turn1CP).phaseEnter(self.game)

    def on_exit_Turn1CP(self):
        return getGamePhaseByName(phase.Turn1CP).phaseExit(self.game)

    #Turn 2
    def on_enter_Turn2MP(self):
        return getGamePhaseByName(phase.Turn2MP).phaseEnter(self.game)

    def on_exit_Turn2MP(self):
        return getGamePhaseByName(phase.Turn2MP).phaseExit(self.game)

    def on_enter_Turn2EP(self):
        return getGamePhaseByName(phase.Turn2EP).phaseEnter(self.game)

    def on_exit_Turn2EP(self):
        return getGamePhaseByName(phase.Turn2EP).phaseExit(self.game)

    def on_enter_Turn2CP(self):
        return getGamePhaseByName(phase.Turn2CP).phaseEnter(self.game)

    def on_exit_Turn2CP(self):
        return getGamePhaseByName(phase.Turn2CP).phaseExit(self.game)

    #Turn 3
    def on_enter_Turn3MP(self):
        return getGamePhaseByName(phase.Turn3MP).phaseEnter(self.game)

    def on_exit_Turn3MP(self):
        return getGamePhaseByName(phase.Turn3MP).phaseExit(self.game)

    def on_enter_Turn3EP(self):
        return getGamePhaseByName(phase.Turn3EP).phaseEnter(self.game)

    def on_exit_Turn3EP(self):
        return getGamePhaseByName(phase.Turn3EP).phaseExit(self.game)

    def on_enter_Turn3CP(self):
        return getGamePhaseByName(phase.Turn3CP).phaseEnter(self.game)

    def on_exit_Turn3CP(self):
        return getGamePhaseByName(phase.Turn3CP).phaseExit(self.game)

    #Economic
    def on_enter_EconP(self):
        return getGamePhaseByName(phase.EconP).phaseEnter(self.game)

    def on_exit_EconP(self):
        return getGamePhaseByName(phase.EconP).phaseExit(self.game)

    def goToNextPhase(self):
        self.next_state()
