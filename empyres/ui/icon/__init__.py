import os
from PyQt5.QtGui import QImage

def loadIcon(name):
    return QImage(os.path.join(os.path.dirname(__file__), name + '.png'))

TTUnrevealed = loadIcon('tt_unrevealed')
TTAsteroids = loadIcon('tt_asteroids')
TTBarrenPlanet = loadIcon('tt_barrenplanet')
TTBlackHole = loadIcon('tt_blackhole')
TTDanger = loadIcon('tt_danger')
TTFertilePlanet = loadIcon('tt_fertileplanet')
TTLostInSpace = loadIcon('tt_lostinspace')
TTMinerals = loadIcon('tt_minerals')
TTNebula  = loadIcon('tt_nebula')
TTSpaceWreck = loadIcon('tt_spacewreck')
TTSupernova = loadIcon('tt_supernova')
