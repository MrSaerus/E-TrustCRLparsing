from PyQt5.QtCore import pyqtSignal, QThread
from models import WatchingCRL, WatchingCustomCRL, UC, db
from log_system import logs
from config import config
import datetime
import time
import OpenSSL
import os
import threading


class MainChecker(QThread):
    print(threading.get_ident(), "MainChecker")
    current_message = pyqtSignal(str)
    done = pyqtSignal(str)

    def __init__(self, modes):
        QThread.__init__(self)
        self._init = False
        self.modeWork = modes

    def run(self):
        print(threading.get_ident(), "MainChecker run")
        if self.modeWork == 'all':
            print('mode all')
        elif self.modeWork == 'check_all':
            self.check_all()
        elif self.modeWork == 'check_mon':
            self.check_mon()
        elif self.modeWork == 'current':
            print('mode all')
        elif self.modeWork == 'custom':
            print('mode all')
        else:
            print('else')

    def check_mon(self):
        self.current_message.emit('Начинаем проверку')
        current_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        current_datetime = datetime.datetime.strptime(current_datetime, '%Y-%m-%d %H:%M:%S')
        before_current_date = datetime.datetime.now() - datetime.timedelta(days=5)
        query_1 = WatchingCRL.select()
        query_2 = WatchingCustomCRL.select()
        for wc in query_1:
            if current_datetime > wc.next_update > before_current_date:
                self.check_current_crl(wc.ID, wc.Name, wc.KeyId)
        for wcc in query_2:
            if current_datetime > wcc.next_update > before_current_date:
                self.check_custom_crl(wcc.ID, wcc.Name, wcc.KeyId)
        time.sleep(1)
        self.current_message.emit('Проверка завершена')
        self.done.emit('Проверка завершена')

    def check_all(self):
        query_1 = WatchingCRL.select()
        query_2 = WatchingCustomCRL.select()
        self.current_message.emit('Проверяем основной список CRL')
        for wc in query_1:
            self.check_current_crl(wc.ID, wc.Name, wc.KeyId)
        self.current_message.emit('Проверяем свой список CRL')
        for wcc in query_2:
            self.check_custom_crl(wcc.ID, wcc.Name, wcc.KeyId)
        self.current_message.emit('Готово')
        self.done.emit('Проверка завершена')

    def check_custom_crl(self, id_custom_crl, name, id_key):
        issuer = {}
        if os.path.isfile(config['Folders']['crls'] + '/' + str(id_key) + '.crl'):
            try:
                crl = OpenSSL.crypto.load_crl(OpenSSL.crypto.FILETYPE_ASN1,
                                              open('crls/' + str(id_key) + '.crl', 'rb').read())
                crl_crypto = crl.get_issuer()
                cryptography = crl.to_cryptography()

                for var, data in crl_crypto.get_components():
                    issuer[var.decode("utf-8")] = data.decode("utf-8")

                query_uc = UC.select().where(UC.OGRN == issuer['OGRN'], UC.INN == issuer['INN'])
                for uc_data in query_uc:
                    name = uc_data.Name
                print(threading.get_ident(), "check_custom_crl")
                with db.transaction('exclusive'):
                    (WatchingCustomCRL
                     .update(INN=issuer['INN'], OGRN=issuer['OGRN'],
                             status='Info: Filetype good',
                             last_update=cryptography.last_update + datetime.timedelta(hours=5),
                             next_update=cryptography.next_update + datetime.timedelta(hours=5))
                     .where(WatchingCustomCRL.ID == id_custom_crl)
                     .execute())
                issuer['INN'] = 'Unknown'
                issuer['OGRN'] = 'Unknown'
            except OpenSSL.crypto.Error:
                print('Warning: OpenSSL not supported this filetype ' + name)
                logs('Warning: OpenSSL not supported this filetype ' + name, 'errors', '4')
                self.current_message.emit('Проверка завершена c ошибкой')
            else:
                print('Info: check_custom_crl()::success ' + name + ' next update in ' +
                      str(cryptography.next_update + datetime.timedelta(hours=5)))
                logs('Info: check_custom_crl()::success ' + name, 'info', '5')
                self.current_message.emit('Проверяем: ' + name + ' ' + id_key)
        else:
            print('Info: check_current_crl:error ' + name + ' file not found')
            logs('Info: check_current_crl:error ' + name + ' file not found', 'info', '5')
            self.current_message.emit('Проверка завершена')

    def check_current_crl(self, id_wc, name_wc, key_id_wc):
        if os.path.isfile(config['Folders']['crls'] + '/' + str(key_id_wc) + '.crl'):
            try:
                crl = OpenSSL.crypto.load_crl(
                    OpenSSL.crypto.FILETYPE_ASN1,
                    open(config['Folders']['crls'] + '/' + str(key_id_wc) + '.crl', 'rb').read())
                cryptography = crl.to_cryptography()
                print(threading.get_ident(), "check_current_crl")
                with db.transaction('exclusive'):
                    (WatchingCRL
                     .update(status='Info: Filetype good',
                            last_update=cryptography.last_update + datetime.timedelta(hours=5),
                            next_update=cryptography.next_update + datetime.timedelta(hours=5))
                     .where(WatchingCRL.ID == id_wc)
                     .execute())
                print('Info: check_current_crl:success ' + name_wc + ' next update in ' +
                      str(cryptography.next_update + datetime.timedelta(hours=5)))
                logs('Info: check_current_crl:success ' + name_wc, 'info', '5')
            except OpenSSL.crypto.Error:
                print('errors: OpenSSL not supported this filetype ' + name_wc)
                logs('errors: OpenSSL not supported this filetype ' + name_wc, 'errors', '4')
                self.current_message.emit('Проверка завершена c ошибкой')
                self.done.emit('Проверка завершена c ошибкой')
            else:
                print('Info: check_custom_crl()::success ' + name_wc + ' next update in ' +
                      str(cryptography.next_update + datetime.timedelta(hours=5)))
                logs('Info: check_custom_crl()::success ' + name_wc, 'info', '5')
                self.current_message.emit('Проверяем: ' + name_wc + ' ' + key_id_wc)
        else:
            print('Info: check_current_crl:error ' + name_wc + ' file not found')
            logs('Info: check_current_crl:error ' + name_wc + ' file not found', 'info', '5')
            self.current_message.emit('Проверка завершена')
