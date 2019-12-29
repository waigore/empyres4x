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
from empyres.core.map import CPoint

logger = logging.getLogger(__name__)

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
        self.setFlag(QGraphicsItem.ItemIsSelectable, True)
        self.setAcceptHoverEvents(True)

    def pointyHexCorner(self, i, center):
        size = self.size
        if not center:
            center = self.center
        angleDeg = 60 * (i%6) - 30
        angleRad = math.pi / 180 * angleDeg
        return CPoint(center.x + size * math.cos(angleRad), center.y + size * math.sin(angleRad))

    def pointyHexagon(self, center = None):
        pts = [self.pointyHexCorner(i, center) for i in range(6)]
        qpts = [QPoint(p.x, p.y) for p in pts]
        return QPolygonF(qpts)

    def drawPointyHexagon(self, painter):
        painter.setPen(QPen(
                QColor('#5A5A5A'),
                2 if self.isSelected() else 1,
                Qt.SolidLine))
        painter.setBrush(QBrush(Qt.black))
        hexagonPoints = self.pointyHexagon()
        painter.drawPolygon(self.pointyHexagon())

    def paint(self, painter, option, widget):
        self.drawPointyHexagon(painter)

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
