from empyres.core.util import (
    GameObject,
    GenericIterator
)
from empyres.core.unit.shipmgt import Fleet

class PlayerFleets(GameObject):
    def __init__(self, color):
        super().__init__('PlayerFleets')
        self.color = color
        self.fleets = []

    def __iter__(self):
        return GenericIterator(self.fleets)

    def createFleet(self, shipGroups = None):
        name = 'Fleet #%d' % (len(self.fleets)+1)
        fleet = Fleet(self.color, name, shipGroups = shipGroups)
        self.fleets.append(fleet)
        return fleet
