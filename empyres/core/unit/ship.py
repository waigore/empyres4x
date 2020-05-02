import enum

class ShipTypes(enum.Enum):
    Colony = 'Colony'
    Battleship = 'Battleship'
    Battlecruiser = 'Battlecruiser'
    Cruiser = 'Cruiser'
    Destroyer = 'Destroyer'
    Decoy = 'Decoy'
    Dreadnaught = 'Dreadnaught'
    Scout = 'Scout'

class CombatClasses(enum.Enum):
    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'
    E = 'E'
    F = 'F'
    NonCombat = 'NonCombat'

    @staticmethod
    def ordered():
        return [
            CombatClasses.A,
            CombatClasses.B,
            CombatClasses.C,
            CombatClasses.D,
            CombatClasses.E,
            CombatClasses.F,
            CombatClasses.NonCombat,
        ]

class MaxMovementSpeeds(enum.Enum):
    One = 'One'
    Inf = 'Inf'

class MaxGroupSizes(enum.Enum):
    One = 'One'
    Inf = 'Inf'

class ShipType(object):
    def __init__(self, type, combatClass, abbrev, displayName, **kwargs):
        self.type = type
        self.combatClass = combatClass
        self.abbrev = abbrev
        self.displayName = displayName
        self.maxGroupSize = kwargs.setdefault('maxGroupSize', MaxGroupSizes.Inf)
        self.maxMovementSpeed = kwargs.setdefault('maxMovementSpeed', MaxMovementSpeeds.Inf)
        self.baseAttackStrength = kwargs.setdefault('baseAttackStrength', 0)
        self.baseDefenseStrength = kwargs.setdefault('baseDefenseStrength', 0)
        self.hullSize = kwargs.setdefault('hullSize', 1)
        self.buildCost = kwargs.setdefault('buildCost', 1)
        self.maintenanceCost = kwargs.setdefault('maintenanceCost', 1)

ColonyShipType = ShipType(ShipTypes.Colony, CombatClasses.NonCombat,
        'CO', 'Colony Ship',
        maxGroupSize = MaxGroupSizes.One,
        maxMovementSpeed = MaxMovementSpeeds.One,
        baseAttackStrength = 0,
        baseDefenseStrength = 0,
        buildCost = 8,
        hullSize = 1,
        maintenanceCost = 0)
BattleshipShipType = ShipType(ShipTypes.Battleship, CombatClasses.A,
        'BB', 'Battleship',
        baseAttackStrength = 5,
        baseDefenseStrength = 2,
        buildCost = 20,
        hullSize = 3,
        maintenanceCost = 3)
BattlecruiserShipType = ShipType(ShipTypes.Battlecruiser, CombatClasses.B,
        'BC', 'Battlecruiser',
        baseAttackStrength = 5,
        baseDefenseStrength = 1,
        buildCost = 15,
        hullSize = 2,
        maintenanceCost = 2)
CruiserShipType = ShipType(ShipTypes.Cruiser, CombatClasses.C,
        'CA', 'Cruiser',
        baseAttackStrength = 4,
        baseDefenseStrength = 1,
        buildCost = 12,
        hullSize = 2,
        maintenanceCost = 2)
DestroyerShipType = ShipType(ShipTypes.Destroyer, CombatClasses.D,
        'DD', 'Destroyer',
        baseAttackStrength = 4,
        baseDefenseStrength = 0,
        buildCost = 9,
        hullSize = 1,
        maintenanceCost = 1)
DreadnaughtShipType = ShipType(ShipTypes.Dreadnaught, CombatClasses.A,
        'DN', 'Dreadnaught',
        baseAttackStrength = 6,
        baseDefenseStrength = 3,
        buildCost = 24,
        hullSize = 3,
        maintenanceCost = 3)
DecoyShipType = ShipType(ShipTypes.Decoy, CombatClasses.NonCombat,
        'Decoy', 'Decoy',
        baseAttackStrength = 0,
        baseDefenseStrength = 0,
        buildCost = 1,
        hullSize = 0,
        maintenanceCost = 0)
ScoutShipType = ShipType(ShipTypes.Scout, CombatClasses.E,
        'SC', 'Scout',
        baseAttackStrength = 3,
        baseDefenseStrength = 0,
        buildCost = 6,
        hullSize = 1,
        maintenanceCost = 1)

AllShipTypes = {
    ShipTypes.Colony: ColonyShipType,
    ShipTypes.Battleship: BattleshipShipType,
    ShipTypes.Battlecruiser: BattlecruiserShipType,
    ShipTypes.Cruiser: CruiserShipType,
    ShipTypes.Destroyer: DestroyerShipType,
    ShipTypes.Decoy: DecoyShipType,
    ShipTypes.Dreadnaught: DreadnaughtShipType,
    ShipTypes.Scout: ScoutShipType,
}

def getShipTypeInfo(shipType):
    return AllShipTypes[shipType]
