from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QIcon
from ui_sub_main_crl import Ui_Form_crl
from main_models import WatchingCRL, WatchingCustomCRL


class CRLWindow(QWidget):
    def __init__(self, crl_key_id):
        super().__init__()
        self.ui_crl = Ui_Form_crl()
        self.ui_crl.setupUi(self)
        self.setWindowIcon(QIcon('assists/favicon.ico'))
        self.init(crl_key_id)

    def init(self, crl_key_id):
        query_1 = WatchingCRL.select().where(WatchingCRL.KeyId == crl_key_id)
        if query_1.count() == 0:
            query_1 = WatchingCustomCRL.select().where(WatchingCustomCRL.KeyId == crl_key_id)
        for wc in query_1:
            self.ui_crl.lineEdit.setText(str(wc.Name))
            self.ui_crl.lineEdit_2.setText(str(wc.INN))
            self.ui_crl.lineEdit_3.setText(str(wc.OGRN))
            self.ui_crl.lineEdit_4.setText(str(wc.KeyId))
            self.ui_crl.lineEdit_5.setText(str(wc.Stamp))
            self.ui_crl.lineEdit_6.setText(str(wc.SerialNumber))
            self.ui_crl.lineEdit_7.setText(str(wc.UrlCRL))
            self.ui_crl.lineEdit_8.setText(str(wc.last_download))
            self.ui_crl.lineEdit_9.setText(str(wc.last_update))
            self.ui_crl.lineEdit_10.setText(str(wc.next_update))
