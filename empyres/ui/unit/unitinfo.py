from PyQt5.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QPushButton,
    QStyle
)
from PyQt5.QtGui import (
    QFont,
    QImage,
    QPainter,
    QPixmap
)
from PyQt5.QtCore import (
    QSize
)
from empyres.ui.map.common import HexBorderColors
from empyres.ui.util import clearLayoutSpacing

BoldFont = QFont()
BoldFont.setBold(True)

class ShipGroupInfoWidget(QWidget):
    def __init__(self, shipGroup, parent=None):
        super().__init__(parent)

        self.shipGroup = shipGroup
        self.initFromShipGroup()

    def minimumSizeHint(self):
        return QSize(200, 0)

    def initFromShipGroup(self):
        if self.shipGroup is None:
            self.initNoShipGroup()
            return
        shipGroup = self.shipGroup
        shipTypeInfo = shipGroup.shipType

        shipGroupType = shipTypeInfo.displayName
        if len(shipGroup.ships) > 1:
            shipGroupType += ' * %d' % (len(shipGroup.ships))
        shipGroupTypeLabel = QLabel(shipGroupType)
        shipGroupTypeLabel.setFont(BoldFont)

        movementPoints = 'M: %d/%d ' % (shipGroup.movementPoints, shipGroup.movementPointsAtStart)
        movementLabel = QLabel(movementPoints)
        info = '%s %d-%d x%d' % (shipTypeInfo.combatClass.name, \
                        shipTypeInfo.baseAttackStrength, \
                        shipTypeInfo.baseDefenseStrength,
                        shipTypeInfo.hullSize)
        infoLabel = QLabel(info)

        infoHBox = QHBoxLayout()
        infoHBox.addWidget(movementLabel)
        infoHBox.addWidget(infoLabel)
        infoHBox.addStretch(1)
        clearLayoutSpacing(infoHBox)

        layout = QVBoxLayout()
        layout.addWidget(shipGroupTypeLabel)
        layout.addLayout(infoHBox)
        layout.setContentsMargins(5, 0, 0, 0)
        layout.setSpacing(0)
        self.setLayout(layout)

    def initNoShipGroup(self):
        label = QLabel('<No ship group>')

        layout = QHBoxLayout()
        layout.addWidget(label)

        self.setLayout(layout)

class FleetInfoWidget(QWidget):
    def __init__(self, fleet, parent=None):
        super().__init__(parent)

        self.fleet = fleet
        self.initFromFleet()

    def initFromFleet(self):
        fleet = self.fleet
        if fleet is None:
            self.initNoFleet(self)
            return

        fleetNameLabel = QLabel(fleet.name)
        fleetIcon = self.createPixmap(fleet.color)
        fleetIconLabel = QLabel()
        fleetIconLabel.setPixmap(fleetIcon)

        splitIcon = self.style().standardIcon(QStyle.SP_FileDialogNewFolder)
        splitButton = QPushButton()
        splitButton.setIcon(splitIcon)

        fleetHeaderHBox = QHBoxLayout()
        fleetHeaderHBox.addWidget(fleetIconLabel)
        fleetHeaderHBox.addWidget(fleetNameLabel)
        fleetHeaderHBox.addStretch(1)
        fleetHeaderHBox.addWidget(splitButton)

        listVBox = self.createShipGroupListVBox()

        layout = QVBoxLayout()
        layout.addLayout(fleetHeaderHBox)
        layout.addLayout(listVBox)
        layout.addStretch(1)
        self.setLayout(layout)

    def createShipGroupListVBox(self):
        listVBox = QVBoxLayout()
        for shipGroup in self.fleet.shipGroups:
            shipGroupInfoWidget = ShipGroupInfoWidget(shipGroup)
            listVBox.addWidget(shipGroupInfoWidget)
        return listVBox

    def createPixmap(self, playerColor):
        qtColor = HexBorderColors[playerColor]
        tileSize = 20
        tile = QImage(tileSize, tileSize, QImage.Format_ARGB32_Premultiplied)

        painter = QPainter()
        painter.begin(tile)
        painter.fillRect(0, 0, tileSize, tileSize, qtColor)
        painter.end()

        pixmap = QPixmap.fromImage(tile)
        return pixmap

    def initNoFleet(self):
        label = QLabel('<No fleet>')

        layout = QHBoxLayout()
        layout.addWidget(label)

        self.setLayout(layout)
