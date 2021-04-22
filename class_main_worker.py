from PyQt5.QtCore import pyqtSignal, QThread
from main_settings import config
from main_log_system import logs
from class_main_downloader import MainDownloader
import datetime
import time
import math
import re
import threading


class MainWorker(QThread):
    print(threading.get_ident(), "MainWorker")
    threadMessageSender = pyqtSignal(str)
    threadTimerSender = pyqtSignal(str)
    threadButtonStartE = pyqtSignal(str)
    threadButtonStopE = pyqtSignal(str)
    threadButtonStartD = pyqtSignal(str)
    threadButtonStopD = pyqtSignal(str)
    threadInfoMessage = pyqtSignal(str)
    threadBefore = pyqtSignal(str)
    threadAfter = pyqtSignal(str)

    def __init__(self):
        QThread.__init__(self)
        self._step = 0
        self._seconds = 0
        self._minutes = 0
        self._hour = 0
        self._day = 0
        self._isRunning = True

    def run(self):
        print(threading.get_ident(), "MainWorker run")
        timer_getting = config['Schedule']['timeUpdate']
        r = re.compile(r"([0-9]+)([a-zA-Z]+)")
        m = r.match(timer_getting)

        if m.group(2) == 'S':
            sec_to_get = int(m.group(1))
        elif m.group(2) == 'M':
            sec_to_get = int(m.group(1)) * 60
        elif m.group(2) == 'H':
            sec_to_get = int(m.group(1)) * 60 * 60
        elif m.group(2) == 'D':
            sec_to_get = int(m.group(1)) * 60 * 60 * 24
        else:
            print('error')
            sec_to_get = 0

        day_get = math.floor(sec_to_get / 60 / 60 / 24)
        hour_get = math.floor(sec_to_get / 60 / 60)
        minutes_get = math.floor(sec_to_get / 60)
        sec_get = math.floor(sec_to_get)

        day_start = 0
        hour_start = 0
        minutes_start = 0
        sec_start = 0
        if day_get > 0:
            day_start = day_get
        else:
            if hour_get > 0:
                hour_start = hour_get
            else:
                if minutes_get > 0:
                    minutes_start = minutes_get
                else:
                    if sec_get > 0:
                        sec_start = sec_get
                    else:
                        print('error')

        print('Info: Start monitoring CRL')
        logs('Info: Start monitoring CRL', 'info', '6')
        self.threadInfoMessage.emit('Мониторинг CRL запущен')
        self.threadButtonStartD.emit('True')
        self.threadButtonStopE.emit('True')
        timer_b = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        timer_a = datetime.datetime.now() + datetime.timedelta(seconds=sec_to_get)
        timer_a = datetime.datetime.strftime(timer_a, '%Y-%m-%d %H:%M:%S')
        self.threadBefore.emit(timer_b)
        self.threadAfter.emit(timer_a)
        if not self._isRunning:
            self._isRunning = True
            self._step = 0
            self._seconds = 0
            self._minutes = 0
            self._hour = 0
            self._day = 0
        while self._isRunning:
            self._step += 1
            self._seconds += 1
            if day_start == 0:
                hour_start -= 1
            if hour_start == 0:
                hour_start = 60
                day_start -= 1
            if minutes_start == 0:
                minutes_start = 60
                hour_start -= 1
            if sec_start == 0:
                sec_start = 60
                minutes_start -= 1
            if self._seconds == 60:
                self._minutes += 1
                self._seconds = 0
            if self._minutes == 60:
                self._hour += 1
                self._minutes = 0
            if self._hour == 24:
                self._day += 1
                self._hour = 0
            sec_c = str(self._seconds)
            min_c = str(self._minutes)
            hou_c = str(self._hour)
            day_c = str(self._day)
            if self._seconds < 10:
                sec_c = '0' + sec_c
            if self._minutes < 10:
                min_c = '0' + min_c
            if self._hour < 10:
                hou_c = '0' + hou_c
            if self._day < 10:
                day_c = '0' + day_c
            # ---------------------------------------------------
            timer = day_c + ' ' + hou_c + ':' + min_c + ':' + sec_c

            self.threadTimerSender.emit(timer)
            if self._step == int(sec_to_get) - 1:
                self.downloader('mon')
                timer_b = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                timer_a = datetime.datetime.now() + datetime.timedelta(seconds=sec_to_get)
                timer_a = datetime.datetime.strftime(timer_a, '%Y-%m-%d %H:%M:%S')
                self.threadBefore.emit(timer_b)
                self.threadAfter.emit(timer_a)
                self._step = 0
            sec_start -= 1
            time.sleep(1)
        print('Info: Monitoring is stopped')
        logs('Info: Monitoring is stopped', 'info', '6')
        self.threadInfoMessage.emit('Мониторинг CRL остановлен')
        self.threadButtonStartE.emit('True')
        self.threadButtonStopD.emit('True')

    def downloader(self, mode):
        self._download = MainDownloader(mode)
        self._download.download_message.connect(lambda: print('test'))
        self._download.start()

    def stop(self):
        self._isRunning = False
