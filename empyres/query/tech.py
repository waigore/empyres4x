from empyres.core.tech import *
from empyres.core.player.tech import PlayerTechTypes
from empyres.core.unit.ship import *

class QueryPlayerTechCanBuildShip(object):
    BuildableShipTypes = {
        ShipTypes.Colony: ShipSizeTechs.I,
        ShipTypes.Battleship: ShipSizeTechs.V,
        ShipTypes.Battlecruiser: ShipSizeTechs.IV,
        ShipTypes.Cruiser: ShipSizeTechs.III,
        ShipTypes.Destroyer: ShipSizeTechs.II,
        ShipTypes.Decoy: ShipSizeTechs.I,
        ShipTypes.Dreadnaught: ShipSizeTechs.VI,
        ShipTypes.Scout: ShipSizeTechs.I,
    }

    def __init__(self, shipType):
        self.shipType = shipType
        if self.shipType not in self.BuildableShipTypes:
            raise ValueError('{} not a buildable ship type!'.format(self.shipType))

    def execute(self, game, player):
        playerTechs = player.technology
        requiredTech = self.BuildableShipTypes[self.shipType]
        playerShipTech = playerTechs.getTech(PlayerTechTypes.ShipSize)
        shipTechOrdered = ShipSizeTechs.ordered()

        return shipTechOrdered.index(playerShipTech) >= shipTechOrdered.index(requiredTech)
