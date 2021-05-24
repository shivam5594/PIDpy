import logging as log
import threading, time

class PID:
    pvalue = ivalue = dvalue = 0
    errorvlaue = 0
    setpoint = 0
    sampletime = 0
    timer = 0

    def __init__(self, _pvalue = 0, _ivalue = 0, _dvalue = 0, _sampletime = 0):
        self.pvalue = _pvalue
        self.ivalue = _ivalue
        self.dvalue = _dvalue
        self.sampletime = _sampletime

    def initsetpoint(self, _setpoint = 0):
        self.setpoint = _setpoint

    def resetsetpoint(self):
        self.setpoint = 0

    def initkp(self, _pvalue = 0):
        self.pvalue = _pvalue

    def initki(self, _ivalue=0):
        self.ivalue = _ivalue

    def initkd(self, _dvalue = 0):
        self.dvalue = _dvalue

    def updatepidvalues(self, _pvalue, _ivalue, _dvalue, _setpoint):
        self.pvalue = _pvalue
        self.ivalue = _ivalue
        self.dvalue = _dvalue
        self.setpoint = _setpoint

    def initsampletime(self, _sampletime = 0):
        self.sampletime = _sampletime

    def getparams(self):
        log.critical(f"Kp :{self.pvalue}")
        log.critical(f"Ki :{self.ivalue}")
        log.critical(f"Kd :{self.dvalue}")
        log.critical(f"Sample time :{self.sampletime} sec")
        log.critical(f"Set point :{self.setpoint}")
        log.critical(f"Callback function :{self.callbackfunction}")

    def callbackfunction(self):
        self.startcontroller()
        log.critical("did something")

    def startcontroller(self):
        self.timer = threading.Timer(self.sampletime, self.callbackfunction)
        self.timer.start()

    def stopcontroller(self):
        self.timer.cancel()
