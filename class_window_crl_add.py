from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QIcon
from ui_sub_main_add import Ui_Form_add
from main_settings import config
from main_log_system import logs
from main_models import UC, CERT, WatchingCRL, WatchingCustomCRL, WatchingDeletedCRL


class AddCRLWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui_add = Ui_Form_add()
        self.ui_add.setupUi(self)
        self.setWindowIcon(QIcon('assists/favicon.ico'))
        self.ui_add.lineEdit.textChanged[str].connect(self.init)
        self.ui_add.pushButton.pressed.connect(self.set_fields)
        self.ui_add.pushButton_2.pressed.connect(self.query_fields)
        self.init()

    def init(self, text=''):
        self.ui_add.comboBox.clear()
        query = CERT.select().where(CERT.Registration_Number.contains(text)
                                    | CERT.Name.contains(text)
                                    | CERT.KeyId.contains(text)
                                    | CERT.Stamp.contains(text)
                                    | CERT.SerialNumber.contains(text)).limit(config['Listing']['cert'])
        for row in query:
            self.ui_add.comboBox.addItem(row.Name, row.KeyId)

    def set_fields(self):
        id_cert = self.ui_add.comboBox.currentData()
        query = CERT.select().where(CERT.KeyId == id_cert)
        registration_number = 0
        for row_cert in query:
            registration_number = row_cert.Registration_Number
            self.ui_add.lineEdit_6.setText(str(row_cert.Name))
            self.ui_add.lineEdit_3.setText(str(row_cert.KeyId))
            self.ui_add.lineEdit_8.setText(str(row_cert.Stamp))
            self.ui_add.lineEdit_4.setText(str(row_cert.SerialNumber))
            self.ui_add.lineEdit_5.setText(str(row_cert.Registration_Number))
        query_2 = UC.select().where(UC.Registration_Number == registration_number)
        for row_uc in query_2:
            self.ui_add.lineEdit_7.setText(str(row_uc.INN))
            self.ui_add.lineEdit_2.setText(str(row_uc.OGRN))

    def query_fields(self):
        if CERT.select().where(CERT.KeyId == self.ui_add.lineEdit_3.text()
                               or CERT.Stamp == self.ui_add.lineEdit_8.text()
                               or CERT.SerialNumber == self.ui_add.lineEdit_4.text()).count() > 0:
            if WatchingCRL.select().where(WatchingCRL.KeyId == self.ui_add.lineEdit_3.text()
                                          or WatchingCRL.Stamp == self.ui_add.lineEdit_8.text()
                                          or WatchingCRL.SerialNumber == self.ui_add.lineEdit_4.text()
                                          or WatchingCRL.UrlCRL == self.ui_add.lineEdit_9.text()).count() > 0:
                print('Info: CRL is exists in WatchingCRL')
                logs('Info: CRL is exists in WatchingCRL', 'info', '7')
                self.ui_add.label_10.setText('CRL уже есть в основном списке отслеживания')
            elif WatchingCustomCRL.select().where(WatchingCustomCRL.KeyId == self.ui_add.lineEdit_3.text()
                                                  or WatchingCustomCRL.Stamp == self.ui_add.lineEdit_8.text()
                                                  or WatchingCustomCRL.SerialNumber == self.ui_add.lineEdit_4.text()
                                                  or WatchingCustomCRL.UrlCRL == self.ui_add.lineEdit_9.text()) \
                    .count() > 0:
                print('Info: CRL is exist in WatchingCustomCRL')
                logs('Info: CRL is exist in WatchingCustomCRL', 'info', '7')
                self.ui_add.label_10.setText('CRL уже есть в своем списке отслеживания')
            elif WatchingDeletedCRL.select().where(WatchingDeletedCRL.KeyId == self.ui_add.lineEdit_3.text()
                                                   or WatchingDeletedCRL.Stamp == self.ui_add.lineEdit_8.text()
                                                   or WatchingDeletedCRL.SerialNumber == self.ui_add.lineEdit_4.text()
                                                   or WatchingDeletedCRL.UrlCRL == self.ui_add.lineEdit_9.text()) \
                    .count() > 0:
                print('Info: CRL is exist in WatchingDeletedCRL')
                logs('Info: CRL is exist in WatchingDeletedCRL', 'info', '7')
                self.ui_add.label_10.setText('CRL уже есть в удаленных, или удалите полностью или верните обратно')
            else:
                name = self.ui_add.lineEdit_6.text()
                inn = self.ui_add.lineEdit_7.text()
                ogrn = self.ui_add.lineEdit_2.text()
                key_id = self.ui_add.lineEdit_3.text()
                stamp = self.ui_add.lineEdit_8.text()
                serial_number = self.ui_add.lineEdit_4.text()
                url_crl = self.ui_add.lineEdit_9.text()
                if name == '' or inn == '' or ogrn == '' or key_id == '' or stamp == '' or serial_number == '' or url_crl == '':
                    print('Заполните все поля')
                    print('Info: The fields should not be empty')
                    logs('Info: The fields should not be empty', 'info', '6')
                    self.ui_add.label_10.setText('Заполните все поля')
                else:
                    query = WatchingCustomCRL(Name=name,
                                              INN=inn,
                                              OGRN=ogrn,
                                              KeyId=key_id,
                                              Stamp=stamp,
                                              SerialNumber=serial_number,
                                              UrlCRL=url_crl,
                                              status='Unknown',
                                              download_status='Unknown',
                                              download_count='0',
                                              last_download='1970-01-01 00:00:00',
                                              last_update='1970-01-01 00:00:00',
                                              next_update='1970-01-01 00:00:00')
                    query.save()
                    # check_custom_crl(query.ID, name, key_id)
                    print('Info: CRL added in WatchingCustomCRL')
                    logs('Info: CRL added in WatchingCustomCRL', 'info', '7')
                    self.ui_add.label_10.setText('CRL "' + name + '" добавлен в список отслеживания')
        else:
            print('Warning: Cert not found')
            logs('Warning: Cert not found', 'warn', '4')
            self.ui_add.label_10.setText('Не найден квалифицированный сертификат УЦ')
