import sys
from PyQt5 import QtWidgets
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

    def startclicked(self):
        print("start clicked")

    def kpchanged(self):
        print(f"Kp value :{self.kp.value()}")

    def kichanged(self):
        print(f"Ki value :{self.ki.value()}")

    def kdchanged(self):
        print(f"Kd value :{self.kd.value()}")

    def setpointchanged(self):
        print(f"Setpoint value :{self.setpoint.value()}")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = PIDpyUI()
    mainWindow.show()
    app.exec_()
