from PyQt5.QtCore import pyqtSignal, QThread
import time
import threading


class Watchdog(QThread):
    print(threading.get_ident(), "Watchdog")
    current_message = pyqtSignal(str)
    push = pyqtSignal(str)

    def __init__(self):
        QThread.__init__(self)
        self._init = False
        self._isRunning = True
        self._step = 0

    def run(self):
        print(threading.get_ident(), "Watchdog run")
        if not self._isRunning:
            self._isRunning = True
            self._step = 0
        while self._isRunning:
            self._step += 1
            # print('Watch..')
            print(threading.active_count(), "количество живых потоков")
            print(threading.current_thread(), "текущий поток")
            print(threading.get_ident(), "Watchdog run")
            print(threading.enumerate(), "список объектов всех живых потоков")
            print(threading.main_thread(), "объект основной потока")
            self.push.emit('')
            time.sleep(1)

    def stop(self):
        self._isRunning = False