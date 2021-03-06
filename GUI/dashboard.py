# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dashboard.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PIDpy(object):
    def setupUi(self, PIDpy):
        PIDpy.setObjectName("PIDpy")
        PIDpy.resize(1020, 883)
        PIDpy.setInputMethodHints(QtCore.Qt.ImhNone)
        self.centralwidget = QtWidgets.QWidget(PIDpy)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 60, 301, 81))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(40, 180, 951, 621))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.OutputGraph = PlotWidget(self.widget)
        self.OutputGraph.setAutoFillBackground(True)
        self.OutputGraph.setObjectName("OutputGraph")
        self.verticalLayout_2.addWidget(self.OutputGraph)
        self.ErrorGraph = PlotWidget(self.widget)
        self.ErrorGraph.setAutoFillBackground(True)
        self.ErrorGraph.setObjectName("ErrorGraph")
        self.verticalLayout_2.addWidget(self.ErrorGraph)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.KpGraph = PlotWidget(self.widget)
        self.KpGraph.setAutoFillBackground(True)
        self.KpGraph.setObjectName("KpGraph")
        self.verticalLayout.addWidget(self.KpGraph)
        self.KiGraph = PlotWidget(self.widget)
        self.KiGraph.setAutoFillBackground(True)
        self.KiGraph.setObjectName("KiGraph")
        self.verticalLayout.addWidget(self.KiGraph)
        self.KdGraph = PlotWidget(self.widget)
        self.KdGraph.setAutoFillBackground(True)
        self.KdGraph.setObjectName("KdGraph")
        self.verticalLayout.addWidget(self.KdGraph)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(560, 43, 353, 122))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.kpLabel = QtWidgets.QLabel(self.widget1)
        self.kpLabel.setObjectName("kpLabel")
        self.horizontalLayout_3.addWidget(self.kpLabel)
        self.kp = QtWidgets.QDoubleSpinBox(self.widget1)
        self.kp.setEnabled(True)
        self.kp.setMinimum(-99.99)
        self.kp.setObjectName("kp")
        self.horizontalLayout_3.addWidget(self.kp)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.kiLabel = QtWidgets.QLabel(self.widget1)
        self.kiLabel.setObjectName("kiLabel")
        self.horizontalLayout_4.addWidget(self.kiLabel)
        self.ki = QtWidgets.QDoubleSpinBox(self.widget1)
        self.ki.setMinimum(-99.99)
        self.ki.setObjectName("ki")
        self.horizontalLayout_4.addWidget(self.ki)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.kdLabel = QtWidgets.QLabel(self.widget1)
        self.kdLabel.setObjectName("kdLabel")
        self.horizontalLayout_5.addWidget(self.kdLabel)
        self.kd = QtWidgets.QDoubleSpinBox(self.widget1)
        self.kd.setMinimum(-99.99)
        self.kd.setObjectName("kd")
        self.horizontalLayout_5.addWidget(self.kd)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.setPointLabel = QtWidgets.QLabel(self.widget1)
        self.setPointLabel.setObjectName("setPointLabel")
        self.horizontalLayout_2.addWidget(self.setPointLabel)
        self.setpoint = QtWidgets.QDoubleSpinBox(self.widget1)
        self.setpoint.setMinimum(-99.99)
        self.setpoint.setObjectName("setpoint")
        self.horizontalLayout_2.addWidget(self.setpoint)
        self.startButton = QtWidgets.QPushButton(self.widget1)
        self.startButton.setObjectName("startButton")
        self.horizontalLayout_2.addWidget(self.startButton)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_2)
        PIDpy.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(PIDpy)
        self.statusbar.setObjectName("statusbar")
        PIDpy.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(PIDpy)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1020, 24))
        self.menubar.setObjectName("menubar")
        PIDpy.setMenuBar(self.menubar)

        self.retranslateUi(PIDpy)
        QtCore.QMetaObject.connectSlotsByName(PIDpy)

    def retranslateUi(self, PIDpy):
        _translate = QtCore.QCoreApplication.translate
        PIDpy.setWindowTitle(_translate("PIDpy", "PIDpy"))
        self.label.setText(_translate("PIDpy", "PID Visualizer"))
        self.OutputGraph.setWhatsThis(_translate("PIDpy", "Live graph of the output value for the plant(robot)"))
        self.ErrorGraph.setWhatsThis(_translate("PIDpy", "Live graph of error(difference between set point and current sensor value)"))
        self.KpGraph.setWhatsThis(_translate("PIDpy", "Live graph of proportional term Kp"))
        self.KiGraph.setWhatsThis(_translate("PIDpy", "Live graph of proportional term Ki"))
        self.KdGraph.setWhatsThis(_translate("PIDpy", "Live graph of proportional term Kd"))
        self.kpLabel.setText(_translate("PIDpy", "Kp"))
        self.kiLabel.setText(_translate("PIDpy", "Ki"))
        self.kdLabel.setText(_translate("PIDpy", "Kd"))
        self.setPointLabel.setText(_translate("PIDpy", "Set point"))
        self.startButton.setText(_translate("PIDpy", "Start"))
from pyqtgraph import PlotWidget
