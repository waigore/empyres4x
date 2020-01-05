import enum

class GameTurns(enum.Enum):
    Turn1 = 'Turn1'
    Turn2 = 'Turn2'
    Turn3 = 'Turn3'
    Economic = 'Economic'

class GamePhases(enum.Enum):
    Movement = 'Movement'
    Combat = 'Combat'
    Exploration = 'Exploration'
    Economic = 'Economic'
