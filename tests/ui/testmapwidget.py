import logging
import sys
from PyQt5.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QMainWindow,
    QShortcut,
    QWidget
)
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QKeySequence
from empyres.core.map import (
    SystemMarkerGen,
    GameMap,
    APoint
)
from empyres.core.unit import Fleet
from empyres.core.player import PlayerColors
from empyres.ui.map import GameMapWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Test game map')

        layout = QHBoxLayout()

        self.gameMap = GameMap()
        systemMarkerGen = SystemMarkerGen(self.gameMap, seed=30)
        systemMarkerGen.populateMap()

        self.gameMap.getHexAt(APoint(1, 3)).fleets.append(Fleet(PlayerColors.Red))
        self.gameMap.getHexAt(APoint(1, 3)).fleets.append(Fleet(PlayerColors.Red))
        self.gameMap.getHexAt(APoint(1, 3)).fleets.append(Fleet(PlayerColors.Red))
        self.gameMap.getHexAt(APoint(2, 4)).fleets.append(Fleet(PlayerColors.Blue))

        self.gameMapWidget = GameMapWidget(self.gameMap, debug=True)
        self.gameMapWidget.hexFleetSelected.connect(self.handleMapWidgetHexFleetSelected)
        self.lastSelectedHexFleetIcon = None
        layout.addWidget(self.gameMapWidget)

        self.revealShortcut = QShortcut(QKeySequence("R"), self)
        self.revealShortcut.activated.connect(self.reveal)
        self.hideShortcut = QShortcut(QKeySequence("U"), self)
        self.hideShortcut.activated.connect(self.hide)

        w = QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w)

        self.show()

    @pyqtSlot()
    def reveal(self):
        self.gameMapWidget.revealAllHexes()

    @pyqtSlot()
    def hide(self):
        self.gameMapWidget.hideAllHexes()

    @pyqtSlot(object, object, object)
    def handleMapWidgetHexFleetSelected(self, icon, hex, color):
        if self.lastSelectedHexFleetIcon:
            self.lastSelectedHexFleetIcon.deselect()
        self.lastSelectedHexFleetIcon = icon
        print('icon selected: %s %s' % (str(hex.aPoint), color))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
