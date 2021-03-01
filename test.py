# import requests, datetime, OpenSSL
# resp = requests.get('http://uc2.srmfc.ru/crl/srmfc_gost12_2019.crl')
# crl = OpenSSL.crypto.load_crl(OpenSSL.crypto.FILETYPE_ASN1, resp.content)
# crl_crypto = crl.get_issuer()
# cryptography = crl.to_cryptography()
# offset = datetime.timedelta(hours=5)
# for type, data in crl_crypto.get_components():
#     print(type.decode("utf-8"), data.decode("utf-8"))
# print(datetime.datetime.strptime(str(cryptography.last_update), '%Y-%m-%d %H:%M:%S')+datetime.timedelta(hours=5))
# print(datetime.datetime.strptime(str(cryptography.next_update), '%Y-%m-%d %H:%M:%S')+datetime.timedelta(hours=5))

import time, sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Worker(QObject):
    'Object managing the simulation'

    stepIncreased = Signal(int)

    def __init__(self):
        super(Worker, self).__init__()
        self._step = 0
        self._isRunning = True
        self._maxSteps = 20

    def task(self):
        if not self._isRunning:
            self._isRunning = True
            self._step = 0

        while self._step < self._maxSteps and self._isRunning == True:
            self._step += 1
            self.stepIncreased.emit(self._step)
            time.sleep(0.1)

        print("finished...")

    def stop(self):
        self._isRunning = False


class SimulationUi(QDialog):
    def __init__(self):
        super(SimulationUi, self).__init__()

        self.btnStart = QPushButton('Start')
        self.btnStop = QPushButton('Stop')
        self.currentStep = QSpinBox()

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.btnStart)
        self.layout.addWidget(self.btnStop)
        self.layout.addWidget(self.currentStep)
        self.setLayout(self.layout)

        self.thread = QThread()
        self.thread.start()

        self.worker = Worker()
        self.worker.moveToThread(self.thread)
        self.worker.stepIncreased.connect(self.currentStep.setValue)

        self.btnStop.clicked.connect(lambda: self.worker.stop())
        self.btnStart.clicked.connect(self.worker.task)

        self.finished.connect(self.stop_thread)

    def stop_thread(self):
        self.worker.stop()
        self.thread.quit()
        self.thread.wait()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    simul = SimulationUi()
    simul.show()
    sys.exit(app.exec_())
