import enum

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

class Player(object):
    def __init__(self, name, color, homeRegion):
        self.name = name
        self.color = color
        self.homeRegion = homeRegion
