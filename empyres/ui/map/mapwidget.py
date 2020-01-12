import math
import logging
from PyQt5.QtWidgets import (
    QGraphicsItem,
    QGraphicsPolygonItem,
    QGraphicsScene,
    QGraphicsView,
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
    CPoint
)
from empyres.core.player import PlayerColors
from empyres.ui.icon import *

logger = logging.getLogger(__name__)

HexBorderColors = {
    PlayerColors.Yellow: Qt.yellow,
    PlayerColors.Green: Qt.green,
    PlayerColors.Red: Qt.red,
    PlayerColors.Blue: Qt.cyan,
}

SystemMarkerIcons = {
    SystemMarkerTypes.Planet: TTBarrenPlanet
}

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
        target = QRect(center.x-15, center.y-15, 30, 30)
        painter.drawImage(target, TTUnrevealed, TTUnrevealed.rect())
        #qpainter.drawImage()

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


class GameMapWidget(QGraphicsView):
    def __init__(self, gameMap, **kwargs):
        super().__init__()
        self.gameMap = gameMap
        self.hexSize = kwargs.setdefault('hexSize', 60)

        self.initScene()
        self.initParams()
        self.initHexItems()

    def initScene(self):
        w = self.colWidth
        h = self.rowHeight
        width = (self.numCols+0.5)*w
        height = self.numRows*h + self.hexHeight*0.25
        logger.info('width: {} height: {}'.format(width, height))

        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0, 0, width, height)
        self.setScene(self.scene)

    def initParams(self):
        self.setRenderHint(QPainter.Antialiasing)
        self.setCacheMode(QGraphicsView.CacheBackground)
        self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)
        self.setBackgroundBrush(QBrush(QColor('#042B48')))

    def initHexItems(self):
        for i in range(self.numRows):
            for j in range(self.numCols):
                hex = self.hexes[i][j]
                if hex is None:
                    continue
                centerX = self.colWidth*(j+1)
                if i % 2 == 0:
                    centerX -= self.hexWidth*0.5
                centerY = self.rowHeight*(i+1)-self.hexHeight*0.25
                center = CPoint(centerX, centerY)
                hexItem = HexGraphicsItem(self, hex, center)
                self.scene.addItem(hexItem)

    @property
    def hexes(self):
        return self.gameMap.hexes

    @property
    def numCols(self):
        return self.gameMap.numCols

    @property
    def numRows(self):
        return self.gameMap.numRows

    @property
    def colWidth(self):
        return math.sqrt(3) * self.hexSize

    @property
    def rowHeight(self):
        return self.hexSize * 1.5

    @property
    def hexWidth(self):
        return math.sqrt(3) * self.hexSize

    @property
    def hexHeight(self):
        return self.hexSize * 2
