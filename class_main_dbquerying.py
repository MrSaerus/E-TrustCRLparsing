from PyQt5.QtCore import QThread
from main_models import db
import threading
import time


class DBQuerying(QThread):
    print(threading.get_ident(), "DBQuerying")
    def __init__(self):
        QThread.__init__(self)
        self._init = False
        self._isRunning = True
        self._step = 0

    def run(self):
        print(threading.get_ident(), "DBQuerying run")
        db.connect()
        print(threading.get_ident(), "db connected in")
        if not self._isRunning:
            self._isRunning = True
            self._step = 0
        while self._isRunning:
            self._step += 1
            print("DBQuerying runer id", threading.get_ident(), ' name ', threading.currentThread().getName())
            time.sleep(1)

    def stop(self):
        self._isRunning = False
