import enum
from .tech import PlayerTechnology
from .fleet import PlayerFleets
from empyres.core.util import GameObject

class PlayerColors(enum.Enum):
    Green = 'Green'
    Yellow = 'Yellow'
    Red = 'Red'
    Blue = 'Blue'

    @staticmethod
    def ordered():
        return [
            PlayerColors.Green,
            PlayerColors.Yellow,
            PlayerColors.Red,
            PlayerColors.Blue
        ]

class Player(GameObject):
    def __init__(self, name, color, homeRegion):
        super().__init__('Player')
        self.name = name
        self.color = color
        self.homeRegion = homeRegion
        self.technology = PlayerTechnology(self.color)
        self.fleets = PlayerFleets(self.color)
