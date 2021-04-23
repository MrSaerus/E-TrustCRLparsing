from PyQt5.QtCore import QThread
import time


class DBQuerying(QThread):
    def __init__(self):
        QThread.__init__(self)
        self._init = False
        self._isRunning = True
        self._step = 0

    def run(self):
        if not self._isRunning:
            self._isRunning = True
            self._step = 0
        while self._isRunning:
            self._step += 1
            time.sleep(1)

    def stop(self):
        self._isRunning = False
