import sys
from PyQt5.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QMainWindow,
    QShortcut,
    QWidget
)
from empyres.core.player import (
    PlayerFleets,
    PlayerTechnology,
    PlayerColors
)
from empyres.core.unit import (
    ShipGroup,
    ScoutShipType,
    DestroyerShipType
)
from empyres.ui.unit import (
    ShipGroupInfoWidget,
    FleetInfoWidget
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Test unit info')

        playerTech = PlayerTechnology(PlayerColors.Red)
        shipGroup = ShipGroup(ScoutShipType, playerTech.snapshot())
        shipGroup.addShip()
        shipGroup2 = ShipGroup(DestroyerShipType, playerTech.snapshot())

        playerFleets = PlayerFleets(PlayerColors.Red)
        fleet = playerFleets.createFleet([shipGroup, shipGroup2])

        fleetInfoWidget = FleetInfoWidget(fleet)

        layout = QHBoxLayout()
        layout.addWidget(fleetInfoWidget)

        w = QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
