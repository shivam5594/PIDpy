import sys
import logging as log
from PyQt5 import QtWidgets
import pyqtgraph as pg
from GUI import dashboard


class PIDpyUI(QtWidgets.QMainWindow, dashboard.Ui_PIDpy):
    def __init__(self, parent=None):
        super(PIDpyUI, self).__init__(parent)
        self.setupUi(self)

        # Setting default logging level
        log.getLogger().setLevel(log.DEBUG)

        # Registering function calls for click actions
        self.kp.valueChanged.connect(self.kpchanged)
        self.ki.valueChanged.connect(self.kichanged)
        self.kd.valueChanged.connect(self.kdchanged)
        self.setpoint.valueChanged.connect(self.setpointchanged)
        self.startButton.clicked.connect(self.startclicked)

        # Initializing local variables
        self.Kp = self.Ki = self.Kd = self.SetPoint = 0

        # Setup timer to update values on graph
        self.timer = pg.QtCore.QTimer(self)

        # Initialize terms for graphs
        # Creating lists since plot function takes list as an input
        self.xAxis = list(range(100))
        self.pTerm = [0] * 100
        self.iTerm = [0] * 100
        self.dTerm = [0] * 100
        self.opTerm = [0] * 100
        self.errorTerm = [0] * 100

        # Creating marker pens for each graph with different colors
        self.outputpen = pg.mkPen(color=(255, 255, 255), width=2)
        self.errorpen = pg.mkPen(color=(255, 255, 255), width=2)
        self.kppen = pg.mkPen(color=(255, 0, 0), width=2)
        self.kipen = pg.mkPen(color=(0, 255, 0), width=2)
        self.kdpen = pg.mkPen(color=(0, 0, 255), width=2)

        # Initial Plot on start-up
        self.KpGraph.plot(self.xAxis, self.pTerm, pen=self.kppen)
        self.KiGraph.plot(self.xAxis, self.iTerm, pen=self.kipen)
        self.KdGraph.plot(self.xAxis, self.dTerm, pen=self.kdpen)
        self.ErrorGraph.plot(self.xAxis, self.errorTerm, pen=self.errorpen)
        self.OutputGraph.plot(self.xAxis, self.opTerm, pen=self.outputpen)

    # Setting all controls for changing Ki, Kp, Kd and set point values
    # to inactive to avoid any changes during the run
    def setcontrolsinactive(self):
        self.kp.setEnabled(False)
        self.ki.setEnabled(False)
        self.kd.setEnabled(False)
        self.setpoint.setEnabled(False)

    # Setting all controls back to active once the plotting is stopped
    def setcontrolsactive(self):
        self.kp.setEnabled(True)
        self.ki.setEnabled(True)
        self.kd.setEnabled(True)
        self.setpoint.setEnabled(True)

    # Initialize timer for certain milliseconds which calls registered function at timeout
    def inittimer(self):
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.refreshplot)

    # Start or stop the initiated timer
    def toggletimer(self):
        if not self.timer.isActive():
            self.timer.start(0)
        else:
            self.timer.stop()

    def startclicked(self):
        if self.startButton.text() == "Start":
            self.setcontrolsinactive()
            self.inittimer()
            self.toggletimer()
            self.startButton.setText("Stop")
            log.info("Start clicked")
        else:
            self.setcontrolsactive()
            self.toggletimer()
            self.startButton.setText("Start")
            log.info("Stop clicked")

    # This function is called by timer everytime it times out.
    # TODO: Read data from input pipe of given interface (COM port, UDP, TCP, WiFi, Bluetooth)
    #       Compute Error and controller output
    #       Update all value lists for plotting
    #       Plot all values
    def refreshplot(self):
        # Update all value lists for plotting
        self.pTerm = self.pTerm[1:]
        self.pTerm.append(self.xAxis[-1])
        self.iTerm = self.iTerm[1:]
        self.iTerm.append(self.xAxis[-1] - self.xAxis[-2])
        self.dTerm = self.dTerm[1:]
        self.dTerm.append(self.xAxis[-2] + self.xAxis[-3])
        self.xAxis = self.xAxis[1:]
        self.xAxis.append(self.xAxis[-1] + 1)
        self.errorTerm = self.errorTerm[1:]
        self.errorTerm.append(self.pTerm[-1] - self.iTerm[-1] - self.dTerm[-1])
        self.opTerm = self.opTerm[1:]
        self.opTerm.append(self.errorTerm[-1])

        # Plot all values
        self.KpGraph.plot(self.xAxis, self.pTerm, pen=self.kppen)
        self.KiGraph.plot(self.xAxis, self.iTerm, pen=self.kipen)
        self.KdGraph.plot(self.xAxis, self.dTerm, pen=self.kdpen)
        self.ErrorGraph.plot(self.xAxis, self.errorTerm, pen=self.errorpen)
        self.OutputGraph.plot(self.xAxis, self.opTerm, pen=self.outputpen)

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
