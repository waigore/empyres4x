import enum

class AttackTechs(enum.Enum):
    O = 'O'
    I = 'I'
    II = 'II'
    III = 'III'

    @staticmethod
    def ordered():
        return [
            AttackTechs.O,
            AttackTechs.I,
            AttackTechs.II,
            AttackTechs.III
        ]

    @staticmethod
    def initial():
        return AttackTechs.O

class DefenseTechs(enum.Enum):
    O = 'O'
    I = 'I'
    II = 'II'
    III = 'III'

    @staticmethod
    def ordered():
        return [
            DefenseTechs.O,
            DefenseTechs.I,
            DefenseTechs.II,
            DefenseTechs.III
        ]

    @staticmethod
    def initial():
        return DefenseTechs.O

class ShipSizeTechs(enum.Enum):
    I = 'I'
    II = 'II'
    III = 'III'
    IV = 'IV'
    V = 'V'
    VI = 'VI'

    @staticmethod
    def ordered():
        return [
            ShipSizeTechs.I,
            ShipSizeTechs.II,
            ShipSizeTechs.III,
            ShipSizeTechs.IV,
            ShipSizeTechs.V,
            ShipSizeTechs.VI,
        ]

    @staticmethod
    def initial():
        return ShipSizeTechs.I

class TacticsTechs(enum.Enum):
    O = 'O'
    I = 'I'
    II = 'II'
    III = 'III'

    @staticmethod
    def ordered():
        return [
            TacticsTechs.O,
            TacticsTechs.I,
            TacticsTechs.II,
            TacticsTechs.III
        ]

    @staticmethod
    def initial():
        return TacticsTechs.O

class MovementTechs(enum.Enum):
    I = 'I'
    II = 'II'
    III = 'III'
    IV = 'IV'
    V = 'V'
    VI = 'VI'

    @staticmethod
    def ordered():
        return [
            MovementTechs.I,
            MovementTechs.II,
            MovementTechs.III,
            MovementTechs.IV,
            MovementTechs.V,
            MovementTechs.VI,
        ]

    @staticmethod
    def initial():
        return MovementTechs.I

class TerraformTechs(enum.Enum):
    O = 'O'
    I = 'I'

    @staticmethod
    def ordered():
        return [
            TerraformTechs.O,
            TerraformTechs.I,
        ]

    @staticmethod
    def initial():
        return TerraformTechs.O

class ExplorationTechs(enum.Enum):
    O = 'O'
    I = 'I'

    @staticmethod
    def ordered():
        return [
            ExplorationTechs.O,
            ExplorationTechs.I,
        ]

    @staticmethod
    def initial():
        return ExplorationTechs.O

class ShipyardTechs(enum.Enum):
    I = 'I'
    II = 'II'
    III = 'III'

    @staticmethod
    def ordered():
        return [
            ShipyardTechs.I,
            ShipyardTechs.II,
            ShipyardTechs.III,
        ]

    @staticmethod
    def initial():
        return ShipyardTechs.I
