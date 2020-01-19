import math
import logging
from PyQt5.QtWidgets import (
    QGraphicsItem,
    QGraphicsPolygonItem,
)
from PyQt5.QtGui import (
    QColor,
    QPainter,
    QPainterPath,
    QBrush,
    QPen,
    QPolygon,
    QPolygonF
)
from PyQt5.QtCore import (
    Qt,
    QRect,
    QRectF,
    QPoint,
    QPointF,
    pyqtSignal
)
from empyres.core.map import (
    SystemMarkerTypes,
    PlanetTypes,
    CPoint
)
from empyres.ui.icon import *
from .common import HexBorderColors

class HexGraphicsItem(QGraphicsPolygonItem):
    Adjust = 0.5

    def __init__(self, mapWidget, hex, center, **kwargs):
        super(HexGraphicsItem, self).__init__()
        self.mapWidget = mapWidget
        self.hex = hex
        self.center = center #CPoint

        self.initParams()
        self.setPolygon(self.pointyHexagon())

    def initParams(self):
        #self.setFlag(QGraphicsItem.ItemIsSelectable, True)
        self.setAcceptHoverEvents(True)

    def pointyHexCorner(self, i, center, size):
        if not size:
            size = self.size
        if not center:
            center = self.center
        angleDeg = 60 * (i%6) - 30
        angleRad = math.pi / 180 * angleDeg
        return CPoint(center.x + size * math.cos(angleRad), center.y + size * math.sin(angleRad))

    def pointyHexagon(self, center = None, size = None):
        return QPolygonF(self.pointyHexagonPoints(center, size))

    def pointyHexagonPoints(self, center = None, size = None, includeInitial = False):
        pts = [self.pointyHexCorner(i, center, size) for i in range(6)]
        if includeInitial:
            pts.append(self.pointyHexCorner(0, center, size))
        return [QPoint(p.x, p.y) for p in pts]

    def getHexBorderColor(self, homeRegionName):
        return HexBorderColors[homeRegionName]

    def drawPointyHexagon(self, painter):
        homeRegionName, borders = self.hex.homeRegionBorders()
        normalPen = QPen(QColor('#5A5A5A'))
        borderPen = QPen(
            self.getHexBorderColor(homeRegionName) if homeRegionName else QColor('#5A5A5A'),
            2)

        painter.setPen(normalPen)
        painter.setBrush(QBrush(Qt.black))
        hexagonPoints = self.pointyHexagonPoints(includeInitial = True)

        #hexagon itself (slightly smaller so no overlap with borders)
        hexagon = self.pointyHexagon(size = self.size - 2)
        painter.drawPolygon(hexagon)

        #hexagon border (with appropriate border colors for home region hexes)
        for i in range(len(hexagonPoints)-1):
            pen = borderPen if i in borders else normalPen
            pt1 = hexagonPoints[i]
            pt2 = hexagonPoints[i+1]
            painter.setPen(pen)
            painter.drawLine(pt1, pt2)

    def drawSystemMarker(self, painter):
        center = self.center
        hex = self.hex
        systemMarker = hex.systemMarker

        target = QRect(center.x-20, center.y-20, 40, 40)
        if not systemMarker.isRevealed:
            self.drawSystemMarkerImage(painter, target, TTUnrevealed)
        elif systemMarker.type == SystemMarkerTypes.EmptySpace:
            pass
        elif systemMarker.type == SystemMarkerTypes.Planet and \
                systemMarker.planetType == PlanetTypes.Fertile:
            self.drawSystemMarkerImage(painter, target, TTFertilePlanet)
        elif systemMarker.type == SystemMarkerTypes.Planet and \
                systemMarker.planetType == PlanetTypes.Barren:
            self.drawSystemMarkerImage(painter, target, TTBarrenPlanet)
        elif systemMarker.type == SystemMarkerTypes.Nebulae:
            self.drawSystemMarkerImage(painter, target, TTNebula)
        elif systemMarker.type == SystemMarkerTypes.Asteroids:
            self.drawSystemMarkerImage(painter, target, TTAsteroids)
        elif systemMarker.type == SystemMarkerTypes.BlackHole:
            self.drawSystemMarkerImage(painter, target, TTBlackHole)
        elif systemMarker.type == SystemMarkerTypes.Danger:
            self.drawSystemMarkerImage(painter, target, TTDanger)
        elif systemMarker.type == SystemMarkerTypes.Supernova:
            self.drawSystemMarkerImage(painter, target, TTSupernova)
        elif systemMarker.type == SystemMarkerTypes.LostInSpace:
            self.drawSystemMarkerImage(painter, target, TTLostInSpace)
        elif systemMarker.type == SystemMarkerTypes.Minerals:
            self.drawSystemMarkerImage(painter, target, TTMinerals)
        elif systemMarker.type == SystemMarkerTypes.SpaceWreck:
            self.drawSystemMarkerImage(painter, target, TTSpaceWreck)

    def drawSystemMarkerImage(self, painter, target, img):
        painter.drawImage(target, img, img.rect())

    def paint(self, painter, option, widget):
        self.drawPointyHexagon(painter)
        if self.hex.systemMarker:
            self.drawSystemMarker(painter)

    @property
    def size(self):
        return self.mapWidget.hexSize

    @property
    def width(self):
        return self.mapWidget.hexWidth

    @property
    def height(self):
        return self.mapWidget.hexHeight
