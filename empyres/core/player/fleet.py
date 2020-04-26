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
        fleet = Fleet(self.color, shipGroups)
        self.fleets.append(fleet)
        return fleet
