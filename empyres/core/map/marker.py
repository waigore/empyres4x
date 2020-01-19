import enum
from empyres.core.phase import GamePhases

class SystemMarkerTypes(enum.Enum):
    Planet = 'Planet'
    Nebulae = 'Nebulae'
    Asteroids = 'Asteroids'
    BlackHole = 'BlackHole'
    Danger = 'Danger'
    Supernova = 'Supernova'
    LostInSpace = 'LostInSpace'
    Minerals = 'Minerals'
    SpaceWreck = 'SpaceWreck'
    EmptySpace = 'EmptySpace'

class PlanetTypes(enum.Enum):
    Barren = 'Barren'
    Fertile = 'Fertile'

class MineralAmounts(enum.Enum):
    Min5 = 'Min5'
    Min10 = 'Min10'
    Min15 = 'Min15'
    Min20 = 'Min20'

class SystemMarker(object):
    def __init__(self, type, **kwargs):
        self.type = type
        self.isRevealed = False
        self._canEnter = kwargs.setdefault('canEnter', True)
        self._hasHighMovementCost = kwargs.setdefault('hasHighMovementCost', False)
        self._providesCover = kwargs.setdefault('providesCover', False)
        self._providesAtkJamming = kwargs.setdefault('providesAtkJamming', False)
        self._providesDefJamming = kwargs.setdefault('providesDefJamming', False)

    #if false, any ships revealing this marker must retreat. Also, no ships may
    #enter into or retreat from this system
    @property
    def canEnter(self):
        return self._canEnter

    #if true, unit must start turn adjacent to marker to be allowed to enter
    @property
    def hasHighMovementCost(self):
        return self._hasHighMovementCost

    #if true, all ships are considered to be E-class during combat
    @property
    def providesCover(self):
        return self._providesCover

    #if true, all ships are considered to have attack tech of 0 during combat
    @property
    def providesAtkJamming(self):
        return self._providesAtkJamming

    #if true, all ships are considered to have defense tech of 0 during combat
    @property
    def providesDefJamming(self):
        return self._providesDefJamming

    def isColonizable(self, game, player):
        return False

    #the effect on the player or unit revealing the marker
    def revealEffect(self, game, player, unit):
        pass

    #the effect on the player or unit entering the system with the marker
    def enterEffect(self, game, player, unit):
        pass

class EmptySpaceMarker(SystemMarker):
    def __init__(self):
        super(EmptySpaceMarker, self).__init__(
            SystemMarkerTypes.EmptySpace
        )

class PlanetMarker(SystemMarker):
    def __init__(self, planetType):
        super(PlanetMarker, self).__init__(
            SystemMarkerTypes.Planet,
        )
        self.planetType = planetType

    def isColonizable(self, game, player):
        #TODO if planet type is barren, check if the player has the requisite tech
        #to init colonization
        return self.planetType != PlanetTypes.Barren

class NebulaeMarker(SystemMarker):
    def __init__(self):
        super(NebulaeMarker, self).__init__(
            SystemMarkerTypes.Nebulae,
            hasHighMovementCost = True,
            providesCover = True,
            providesDefJamming =  True
        )

class AsteroidsMarker(SystemMarker):
    def __init__(self):
        super(AsteroidsMarker, self).__init__(
            SystemMarkerTypes.Asteroids,
            hasHighMovementCost = True,
            providesCover = True,
            providesAtkJamming = True
        )

class BlackHoleMarker(SystemMarker):
    def __init__(self):
        super(BlackHoleMarker, self).__init__(
            SystemMarkerTypes.BlackHole,
        )

class DangerMarker(SystemMarker):
    def __init__(self):
        super(DangerMarker, self).__init__(
            SystemMarkerTypes.Danger,
        )

class SupernovaMarker(SystemMarker):
    def __init__(self):
        super(SupernovaMarker, self).__init__(
            SystemMarkerTypes.Supernova,
            canEnter = False
        )

class LostInSpaceMarker(SystemMarker):
    def __init__(self):
        super(LostInSpaceMarker, self).__init__(
            SystemMarkerTypes.LostInSpace,
        )

class MineralsMarker(SystemMarker):
    def __init__(self, mineralAmount):
        super(MineralsMarker, self).__init__(
            SystemMarkerTypes.Minerals,
        )
        self.mineralAmount = mineralAmount

class SpaceWreckMarker(SystemMarker):
    def __init__(self):
        super(SpaceWreckMarker, self).__init__(
            SystemMarkerTypes.SpaceWreck,
        )
