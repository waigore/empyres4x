from PyQt5.QtWidgets import (
    QGraphicsItem
)
from PyQt5.QtCore import (
    QRect,
    QRectF
)
from empyres.ui.icon import *
from empyres.core.player import PlayerColors
from empyres.exception import PlayerColorInvalidException

class HexFleetIcon(QGraphicsItem):
    def __init__(self, hex):
        super().__init__()
        self.hex = hex

    def boundingRect(self):
        return QRectF(-10, -10, 20, 20)

    @property
    def playerColor(self):
        return None if self.hex.fleet is None else self.hex.fleet.color

    def drawIcon(self, painter):
        if self.playerColor is None:
            return
        br = self.boundingRect()
        target = QRect(int(br.x()), int(br.y()), int(br.width()), int(br.height()))
        if self.playerColor == PlayerColors.Red:
            painter.drawImage(target, FleetRed, FleetRed.rect())
        elif self.playerColor == PlayerColors.Green:
            painter.drawImage(target, FleetGreen, FleetRed.rect())
        elif self.playerColor == PlayerColors.Blue:
            painter.drawImage(target, FleetBlue, FleetRed.rect())
        elif self.playerColor == PlayerColors.Yellow:
            painter.drawImage(target, FleetYellow, FleetRed.rect())

    def paint(self, painter, option, widget):
        self.drawIcon(painter)

    def mousePressEvent(self, event):
        if self.playerColor:
            print('fleet icon clicked: %s' % (self.playerColor))
