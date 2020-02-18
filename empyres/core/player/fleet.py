class PlayerFleetIterator(object):
    def __init__(self, fleets):
        self.fleets = fleets
        self.count = 0

    def __next__(self):
        if self.count >= len(self.fleets):
            raise StopIteration

        fleet = self.fleets[self.count]
        self.count += 1
        return fleet

class PlayerFleets(object):
    def __init__(self):
        self.fleets = []

    def __iter__(self):
        return PlayerFleetIterator(self.fleets)

    def addShipGroup(self, sg):
        self.fleets.append(sg)
