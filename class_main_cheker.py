from PyQt5.QtCore import pyqtSignal, QThread
from prettytable import PrettyTable
from main_models import WatchingCRL, WatchingCustomCRL, UC, db
from main_log_system import logs
from main_settings import config
from main_moduls import delta_checker
import datetime
import time
import OpenSSL
import os
import peewee


class MainChecker(QThread):
    current_message = pyqtSignal(str)
    done = pyqtSignal(str)

    def __init__(self, modes):
        QThread.__init__(self)
        self._init = False
        self.modeWork = modes

    def run(self):
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
                # check_current_crl(wc.ID, wc.Name, wc.KeyId)
                self.current_message.emit(check_current_crl(wc.ID, wc.Name, wc.KeyId))
        for wcc in query_2:
            if current_datetime > wcc.next_update > before_current_date:
                # check_custom_crl(wcc.ID, wcc.Name, wcc.KeyId)
                self.current_message.emit(check_custom_crl(wcc.ID, wcc.Name, wcc.KeyId))
        time.sleep(1)
        self.current_message.emit('Проверка завершена')
        self.done.emit('Проверка завершена')

    def check_all(self):
        query_1 = WatchingCRL.select()
        query_2 = WatchingCustomCRL.select()
        self.current_message.emit('Проверяем основной список CRL')
        table = PrettyTable()
        table.field_names = ["Название УЦ", "Идентификатор ключа", "Время жизни CRl", "Время до истечения CRL", "Проверять за"]
        for wc in query_1:
            self.current_message.emit(check_current_crl(wc.ID, wc.Name, wc.KeyId))
            dc = delta_checker(wc.Name, wc.KeyId, wc.last_download, wc.last_update, wc.next_update, wc.download_count)
            if not dc == None:
                dc = dc.split(';')
                table.add_row([dc[0], dc[1], dc[2], dc[3], dc[4]])
        self.current_message.emit('Проверяем свой список CRL')
        for wcc in query_2:
            self.current_message.emit(check_custom_crl(wcc.ID, wcc.Name, wcc.KeyId))
            dc = delta_checker(wcc.Name, wcc.KeyId, wcc.last_download, wcc.last_update, wcc.next_update, wcc.download_count)
            if not dc == None:
                dc = dc.split(';')
                table.add_row([dc[0], dc[1], dc[2], dc[3], dc[4]])
            # table.add_row([])
        self.current_message.emit('Готово')
        self.done.emit('Проверка завершена')
        print(table)


def check_custom_crl(id_custom_crl, name, id_key):
    issuer = {}
    if os.path.isfile(config['Folders']['crls'] + '/' + str(id_key) + '.crl'):
        try:
            crl = OpenSSL.crypto.load_crl(OpenSSL.crypto.FILETYPE_ASN1,
                                          open(config['Folders']['crls'] + str(id_key) + '.crl', 'rb').read())
            crl_crypto = crl.get_issuer()
            cryptography = crl.to_cryptography()

            for var, data in crl_crypto.get_components():
                issuer[var.decode("utf-8")] = data.decode("utf-8")

            query_uc = UC.select().where(UC.OGRN == issuer['OGRN'], UC.INN == issuer['INN'])
            for uc_data in query_uc:
                name = uc_data.Name
            while True:
                try:
                    with db.transaction('exclusive'):
                        (WatchingCustomCRL.update(INN=issuer['INN'], OGRN=issuer['OGRN'],
                                                  status='Info: Filetype good',
                                                  last_update=cryptography.last_update + datetime.timedelta(hours=5),
                                                  next_update=cryptography.next_update + datetime.timedelta(hours=5))
                         .where(WatchingCustomCRL.ID == id_custom_crl)
                         .execute())
                except peewee.OperationalError:
                    print('OperationalError:check_custom_crl:WatchingCustomCRL.update')
                    time.sleep(10)
                else:
                    break
            issuer['INN'] = 'Unknown'
            issuer['OGRN'] = 'Unknown'
        except OpenSSL.crypto.Error:
            logs('Warning: OpenSSL not supported this filetype ' + name, 'errors', '4')
            return 'Проверка завершена c ошибкой, этот файлов не поддерживается'
        else:
            logs('Info: check_custom_crl:success ' + name, 'info', '5')
            return str('Проверяем: ' + name + ' ' + id_key)
    else:
        logs('Info: check_custom_crl:error ' + name + ' file not found', 'info', '5')
        return 'Проверка завершена с ошибкой, нет файлов'


def check_current_crl(id_wc, name_wc, key_id_wc):
    if os.path.isfile(config['Folders']['crls'] + '/' + str(key_id_wc) + '.crl'):
        try:
            crl = OpenSSL.crypto.load_crl(
                OpenSSL.crypto.FILETYPE_ASN1,
                open(config['Folders']['crls'] + '/' + str(key_id_wc) + '.crl', 'rb').read())
            cryptography = crl.to_cryptography()
            while True:
                try:
                    with db.transaction('exclusive'):
                        (WatchingCRL.update(status='Info: Filetype good',
                                            last_update=cryptography.last_update + datetime.timedelta(hours=5),
                                            next_update=cryptography.next_update + datetime.timedelta(hours=5))
                         .where(WatchingCRL.ID == id_wc)
                         .execute())
                except peewee.OperationalError:
                    print('OperationalError:check_current_crl:WatchingCRL.update')
                    time.sleep(10)
                else:
                    break
        except OpenSSL.crypto.Error:
            logs('errors: OpenSSL not supported this filetype ' + name_wc, 'errors', '4')
            return 'Проверка завершена c ошибкой, этот файлов не поддерживается'
        else:
            logs('Info: check_current_crl:success ' + name_wc, 'info', '5')
            return str('Проверяем: ' + name_wc + ' ' + key_id_wc)
    else:
        logs('Info: check_current_crl:error ' + name_wc + ' file not found', 'info', '5')
        return 'Проверка завершена с ошибкой, нет файлов'
