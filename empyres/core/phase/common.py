import enum

class GameTurns(enum.Enum):
    RoundStart = 'RoundStart'
    Turn1 = 'Turn1'
    Turn2 = 'Turn2'
    Turn3 = 'Turn3'
    Economic = 'Economic'

class GamePhases(enum.Enum):
    RoundStart = 'RoundStart'
    Movement = 'Movement'
    Combat = 'Combat'
    Exploration = 'Exploration'
    Economic = 'Economic'

RoundStartP = 'RoundStartP'
Turn1MP = 'Turn1MP'
Turn1EP = 'Turn1EP'
Turn1CP = 'Turn1CP'
Turn2MP = 'Turn2MP'
Turn2EP = 'Turn2EP'
Turn2CP = 'Turn2CP'
Turn3MP = 'Turn3MP'
Turn3EP = 'Turn3EP'
Turn3CP = 'Turn3CP'
EconP = 'EconP'
