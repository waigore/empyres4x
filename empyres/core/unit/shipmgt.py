from .ship import MaxGroupSizes

class Ship(object):
    def __init__(self, damage = 0):
        self.damage = damage

class ShipGroup(object):
    def __init__(self, shipType, techLevels, numShips = 0):
        self.shipType = shipType
        self.ships = []
        self.techLevels = techLevels #dict of {PlayerTechTypes: *Techs.I/II/III...}
        self.movementPointsAtStart = 0
        self.movementPoints = 0

        for i in range(numShips):
            self.addShip()

    def resetMovementPoints(self, newMP):
        self.movementPointsAtStart = newMP
        self.movementPoints = newMP

    def decrMovement(self):
        if self.movementPoints == 0:
            raise ValueError('Ship has no movement points left!')
        self.movementPoints -= 1

    def addShip(self):
        if self.maxGroupSize == MaxGroupSizes.One:
            raise ValueError('Too many ships in group: maxGroupSize = {}'.format(self.maxGroupSize))
        self.ships.append(Ship())

    def removeShip(self, i = None):
        if len(self.ships) == 0:
            raise ValueError('No ships left in group!')
        if i is None:
            self.ships.pop()
        else:
            self.ships.pop(i)

    def setTechLevels(self, newTechLevels):
        self.techLevels = newTechLevels

    @property
    def maxGroupSize(self):
        return self.shipType.maxGroupSize

    @property
    def numShips(self):
        return len(self.ships)

class Fleet(object):
    def __init__(self, name = 'Fleet', shipGroups = None):
        self.name = name
        self.shipGroups = [] if shipGroups is None else shipGroups

    def addShipGroup(self, shipGroup):
        self.shipGroups.append(shipGroup)
