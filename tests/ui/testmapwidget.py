import logging
import sys
from PyQt5.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QMainWindow,
    QWidget
)
from empyres.core.map import GameMap
from empyres.ui.map import GameMapWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Test game map')

        layout = QHBoxLayout()

        gameMap = GameMap()
        gameMapWidget = GameMapWidget(gameMap)
        layout.addWidget(gameMapWidget)

        w = QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
