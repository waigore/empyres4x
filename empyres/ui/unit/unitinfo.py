from PyQt5.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QLabel
)
from PyQt5.QtGui import (
    QFont
)

BoldFont = QFont()
BoldFont.setBold(True)

class ShipGroupInfoWidget(QWidget):
    def __init__(self, shipGroup, parent=None):
        super().__init__(parent)

        self.shipGroup = shipGroup
        self.initFromShipGroup()

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

        movementPoints = 'Movement: %d/%d' % (shipGroup.movementPoints, shipGroup.movementPointsAtStart)
        movementLabel = QLabel(movementPoints)

        additInfo = '%s %d-%d x%d' % (shipTypeInfo.combatClass.name, \
                        shipTypeInfo.baseAttackStrength, \
                        shipTypeInfo.baseDefenseStrength,
                        shipTypeInfo.hullSize)
        additInfoLabel = QLabel(additInfo)

        layout = QVBoxLayout()
        layout.addWidget(shipGroupTypeLabel)
        layout.addWidget(movementLabel)
        layout.addWidget(additInfoLabel)
        self.setLayout(layout)

    def initNoShipGroup(self):
        label = QLabel('<No ship group>')

        layout = QHBoxLayout()
        layout.addWidget(label)

        self.setLayout(layout)
