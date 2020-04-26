from empyres.exception import MapOutOfBoundsException

class ActionCreateFleet(object):
    def __init__(self, aPoint, shipGroups = None):
        self.aPoint = aPoint
        self.shipGroups = shipGroups

    def execute(self, game, player):
        fleet = player.fleets.createFleet(self.shipGroups)

        hex = game.map.getHexAt(self.aPoint)
        if hex is None:
            raise MapOutOfBoundsException(hex)
        hex.fleets.append(fleet)
