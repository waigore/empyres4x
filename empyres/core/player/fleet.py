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
        self.fleetLocations = {}

    def __iter__(self):
        return GenericIterator(self.fleets)

    def createFleetAt(self, aPoint, shipGroups = None):
        fleet = Fleet(shipGroups)
        self.fleets.append(fleet)
        self.fleetLocations[fleet.uuid] = aPoint
