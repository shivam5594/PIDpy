import sys
import logging as log
from PyQt5 import QtWidgets
import pyqtgraph as pg
from GUI import dashboard


class PIDpyUI(QtWidgets.QMainWindow, dashboard.Ui_PIDpy):
    def __init__(self, parent=None):
        super(PIDpyUI, self).__init__(parent)
        self.setupUi(self)

        # Registering function calls for click actions
        self.kp.valueChanged.connect(self.kpchanged)
        self.ki.valueChanged.connect(self.kichanged)
        self.kd.valueChanged.connect(self.kdchanged)
        self.setpoint.valueChanged.connect(self.setpointchanged)
        self.startButton.clicked.connect(self.startclicked)

        # Initializing local variables
        self.Kp = self.Ki = self.Kd = self.SetPoint = 0

        # Initialize
        self.xAxis = list(range(100))
        self.pTerm = [0] * 100
        self.iTerm = [0] * 100
        self.dTerm = [0] * 100
        self.currentTerm = [0] * 100
        self.errorTerm = [0] * 100

        # See if this can be put in layout.py
        penUpLeft = pg.mkPen(color=(255, 255, 255), width=2)
        penUpRight = pg.mkPen(color=(255, 255, 255), width=2)
        penBottomLeft = pg.mkPen(color=(255, 0, 0), width=2)
        penBottomCentre = pg.mkPen(color=(0, 255, 0), width=2)
        penBottomRight = pg.mkPen(color=(0, 0, 255), width=2)

        # Initial Plot
        self.UpLeft = self.KpGraph.plot(self.xAxis, self.currentTerm, pen=penUpLeft)
        self.UpRight = self.KiGraph.plot(self.xAxis, self.errorTerm, pen=penUpRight)
        self.BottomLeft = self.KdGraph.plot(self.xAxis, self.pTerm, pen=penBottomLeft)
        self.BottomCenter = self.ErrorGraph.plot(self.xAxis, self.iTerm, pen=penBottomCentre)
        self.BottomRight = self.OutputGraph.plot(self.xAxis, self.dTerm, pen=penBottomRight)

    def startclicked(self):
        if self.startButton.text() == "Start":
            self.startButton.setText("Stop")
            log.info("Start clicked")
        else:
            self.startButton.setText("Start")
            log.info("Stop clicked")

    def kpchanged(self):
        log.info(f"Kp value :{self.kp.value()}")

    def kichanged(self):
        log.info(f"Ki value :{self.ki.value()}")

    def kdchanged(self):
        log.info(f"Kd value :{self.kd.value()}")

    def setpointchanged(self):
        log.info(f"Setpoint value :{self.setpoint.value()}")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = PIDpyUI()
    mainWindow.show()
    app.exec_()
