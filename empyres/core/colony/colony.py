import enum

class ColonyTypes(enum.Enum):
    Colony = 'Colony'
    Homeworld = 'Homeworld'

class Colony(object):
    def __name__(self, name, type = ColonyTypes.Homeworld):
        self.type = type
        self.name = name
        self.size = self.initialSize
        self.isDestroyed = False

    @property
    def initialSize(self):
        if self.type == ColonyTypes.Colony:
            return 1
        else:
            return 20

    @property
    def growthIncrement(self):
        if self.type == ColonyTypes.Colony:
            return 2
        else:
            return 5

    @property
    def maxSize(self):
        if self.type == ColonyTypes.Colony:
            return 5
        else:
            return 20

    def grow(self):
        if self.size >= self.maxSize:
            return
        self.size += self.growthIncrement

    def shrink(self):
        if self.size <= self.initialSize:
            self.isDestroyed = True
        else:
            self.size -= self.growthIncrement
