import os
from PyQt5.QtGui import QImage

def loadIcon(name):
    return QImage(os.path.join(os.path.dirname(__file__), name + '.png'))

TTUnrevealed = loadIcon('tt_unrevealed')
TTBarrenPlanet = loadIcon('tt_barrenplanet')
