from PyQt5.QtWidgets import (
    QGraphicsItem
)
from PyQt5.QtCore import (
    Qt,
    QRect,
    QRectF
)
from PyQt5.QtGui import (
    QColor,
    QBrush,
    QPen
)
from empyres.ui.icon import *
from empyres.core.player import PlayerColors
from empyres.exception import PlayerColorInvalidException
from .common import HexBorderColors

class HexFleetIcon(QGraphicsItem):
    def __init__(self, hex):
        super().__init__()
        self.hex = hex
        self.selected = False

    def boundingRect(self):
        return QRectF(-10, -10, 20, 20)

    @property
    def playerColor(self):
        return None if len(self.hex.fleets) == 0 else self.hex.fleets[0].color

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

    def drawSelectedBorder(self, painter):
        bRect = self.borderRect()
        borderColorPen = QPen(HexBorderColors[self.playerColor], 1)
        painter.setPen(borderColorPen)
        painter.drawRect(bRect)

    def drawFleetNumber(self, painter):
        num = '*'
        br = self.boundingRect()
        rect = QRect(int(br.x()+br.width()-5), int(br.y()), 5, 10)
        pen = QPen(QColor(Qt.white), 1)
        painter.setPen(pen)
        painter.drawText(rect, Qt.AlignCenter, num)

    def borderRect(self):
        br = self.boundingRect()
        return QRectF(br.x()+1, br.y()+1, br.width()-1, br.height()-1)

    def paint(self, painter, option, widget):
        self.drawIcon(painter)
        if len(self.hex.fleets) > 1:
            self.drawFleetNumber(painter)
        if self.selected:
            self.drawSelectedBorder(painter)

    def deselect(self):
        self.selected = False
        self.update()

    def mousePressEvent(self, event):
        if self.playerColor:
            self.selected = not self.selected
            if self.selected:
                self.parentItem().mapWidget.hexFleetSelected.emit(self, self.hex, self.playerColor)
            self.update()
