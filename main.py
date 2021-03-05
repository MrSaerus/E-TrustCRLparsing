from PyQt5.QtWidgets import QPushButton, QWidget, QTableWidgetItem, QHeaderView, QFileDialog
from PyQt5.QtCore import pyqtSignal, QThread
from urllib import request, error
from ui_sub_main import *
from lxml import etree
from ui_sub_main_add import *
from ui_main import *
from peewee import *
import OpenSSL
import base64
import configparser
import datetime
import math
import os
import re
import shutil
import sqlite3
import sys
import time

config = configparser.ConfigParser()
if os.path.isfile('settings.ini'):
    config.read('settings.ini')
else:
    open('settings.ini', 'w').close()
    config['Folders'] = {'certs': 'certs/',
                         'crls': 'crls/',
                         'tmp': 'temp/',
                         'logs': 'logs/',
                         'to_uc': 'uc/'}

    config['MainWindow'] = {'width ': '1200',
                            'height ': '600',
                            'saveWidth': 'No',
                            'AllowResize': 'Yes'}
    config['Bd'] = {'type': 'sqlite3',
                    'name': 'cert_crl.db'}
    config['Socket'] = {'timeout ': 'No'}
    config['Listing'] = {'uc': '500',
                         'crl': '500',
                         'cert': '500',
                         'watch': '500'}
    # windowsvista, Windows, Fusion
    config['Style'] = {'window': 'Fusion',
                       'extendetColorInfo': 'No'}
    config['Proxy'] = {'proxyOn': 'No',
                       'ip': '',
                       'port': '',
                       'login': '',
                       'password': ''}
    config['Update'] = {'priority': 'custom',
                        'advancedChecking': 'Yes',
                        'viewingCRLlastNextUpdate': 'Yes'}
    config['Backup'] = {'backUPbyStart': 'Yes'}
    config['Tabs'] = {'ucLimit': '500',
                      'ucAllowDelete': 'No',
                      'crlLimit': '500',
                      'crlAllowDelete': 'No',
                      'certLimit': '500',
                      'certAllowDelete': 'No',
                      'wcLimit': '500',
                      'wcAllowDelete': 'No',
                      'wccLimit': '500',
                      'wccAllowDelete': 'No',
                      'wcdLimit': '500',
                      'wcdAllowDelete': 'No'}
    config['Schedule'] = {'allowSchedule': 'No',
                          'weekUpdate': 'All',
                          'timeUpdate': '10M',
                          'periodUpdate': '9:00; 12:00; 16:00',
                          'allowUpdateTSLbyStart': 'No',
                          'allowUpdateCRLbyStart': 'No',
                          'rangeUpdateCRL': '5day'}
    config['Sec'] = {'allowImportCRL': 'No',
                     'allowExportCRL': 'No',
                     'allowDeleteWatchingCRL': 'No',
                     'allowDownloadButtonCRL': 'Yes',
                     'allowCheckButtonCRL': 'Yes'}
    with open('settings.ini', 'w') as configfile:
        config.write(configfile)

try:
    os.makedirs(config['Folders']['certs'])
except OSError:
    pass
try:
    os.makedirs(config['Folders']['crls'])
except OSError:
    pass
try:
    os.makedirs(config['Folders']['tmp'])
except OSError:
    pass
try:
    os.makedirs(config['Folders']['to_uc'])
except OSError:
    pass
try:
    os.makedirs(config['Folders']['logs'])
except OSError:
    pass


def logs(body, t=''):
    if t == 'errors':
        with open(config['Folders']['logs'] + "/error_" + datetime.datetime.now().strftime('%Y%m%d') + ".log",
                  "a") as file:
            file.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '    ' + body + '\n')
        file.close()
    else:
        with open(config['Folders']['logs'] + "/log_" + datetime.datetime.now().strftime('%Y%m%d') + ".log",
                  "a") as file:
            file.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '    ' + body + '\n')
        file.close()


bd_backup_name = str('cert_crl.db_') + datetime.datetime.now().strftime('%Y%m%d') + '.bkp'
if os.path.isfile(bd_backup_name):
    print('Info: ' + bd_backup_name + ' exist')
    logs('Info: ' + bd_backup_name + ' exist')
else:
    try:
        shutil.copy2('cert_crl.db', bd_backup_name)
        print('Info: ' + bd_backup_name + ' created')
        logs('Info: ' + bd_backup_name + ' created')
    except Exception:
        print('Error: cert_crl.db NOT FOUND')
        logs('Error: cert_crl.db NOT FOUND', 'errors')
try:
    connect = sqlite3.connect(config['Bd']['name'])
    db = SqliteDatabase(config['Bd']['name'])
except Exception:
    print('Error: Connect to BD failed')
    logs('Error: Connect to BD failed', 'errors')


class UC(Model):
    ID = IntegerField(primary_key=True)
    Registration_Number = IntegerField()
    INN = IntegerField()
    OGRN = IntegerField()
    Full_Name = CharField()
    Email = CharField()
    Name = CharField()
    URL = CharField()
    AddresCode = CharField()
    AddresName = CharField()
    AddresIndex = CharField()
    AddresAddres = CharField()
    AddresStreet = CharField()
    AddresTown = CharField()

    class Meta:
        database = db


class CERT(Model):
    ID = IntegerField(primary_key=True)
    Registration_Number = IntegerField()
    Name = CharField()
    KeyId = CharField()
    Stamp = CharField()
    SerialNumber = CharField()
    Data = CharField()

    class Meta:
        database = db


class CRL(Model):
    ID = IntegerField(primary_key=True)
    Registration_Number = IntegerField()
    Name = CharField()
    KeyId = CharField()
    Stamp = CharField()
    SerialNumber = CharField()
    UrlCRL = CharField()

    class Meta:
        database = db


class WatchingCRL(Model):
    ID = IntegerField(primary_key=True)
    Name = CharField()
    INN = IntegerField()
    OGRN = IntegerField()
    KeyId = CharField()
    Stamp = CharField()
    SerialNumber = CharField()
    UrlCRL = CharField()
    status = CharField()
    download_status = CharField()
    download_count = CharField()
    last_download = DateTimeField()
    last_update = DateTimeField()
    next_update = DateTimeField()

    class Meta:
        database = db


class WatchingCustomCRL(Model):
    ID = IntegerField(primary_key=True)
    Name = CharField()
    INN = IntegerField()
    OGRN = IntegerField()
    KeyId = CharField()
    Stamp = CharField()
    SerialNumber = CharField()
    UrlCRL = CharField()
    status = CharField()
    download_status = CharField()
    download_count = CharField()
    last_download = DateTimeField()
    last_update = DateTimeField()
    next_update = DateTimeField()

    class Meta:
        database = db


class WatchingDeletedCRL(Model):
    ID = IntegerField(primary_key=True)
    Name = CharField()
    INN = IntegerField()
    OGRN = IntegerField()
    KeyId = CharField()
    Stamp = CharField()
    SerialNumber = CharField()
    UrlCRL = CharField()
    status = CharField()
    download_status = CharField()
    download_count = CharField()
    last_download = DateTimeField()
    last_update = DateField()
    next_update = DateField()

    class Meta:
        database = db


class Settings(Model):
    ID = IntegerField(primary_key=True)
    name = IntegerField()
    value = CharField()

    class Meta:
        database = db


if not UC.table_exists():
    UC.create_table()
if not CERT.table_exists():
    CERT.create_table()
if not CRL.table_exists():
    CRL.create_table()
if not Settings.table_exists():
    Settings.create_table()
    Settings(name='ver', value=0).save()
    Settings(name='data_update', value='1970-01-01 00:00:00').save()
if not WatchingCRL.table_exists():
    WatchingCRL.create_table()
if not WatchingCustomCRL.table_exists():
    WatchingCustomCRL.create_table()
if not WatchingDeletedCRL.table_exists():
    WatchingDeletedCRL.create_table()


def progressbar(cur, total=100):
    percent = '{:.2%}'.format(cur / total)
    sys.stdout.write('\r')
    # sys.stdout.write("[%-50s] %s" % ('=' * int(math.floor(cur * 50 / total)),percent))
    sys.stdout.write("[%-100s] %s" % ('=' * int(cur), percent))
    sys.stdout.flush()


def schedule(block_num, block_size, total_size):
    QCoreApplication.processEvents()
    if total_size == 0:
        percent = 0
    else:
        percent = block_num * block_size / total_size
    if percent > 1.0:
        percent = 1.0
    percent = percent * 100
    print("\n download : %.2f%%" % (percent))
    progressbar(percent)


def get_info_xlm(type_data, xml_file='tsl.xml'):
    current_version = 'unknown'
    last_update = 'unknown'
    with open(xml_file, "rt", encoding="utf-8") as obj:
        xml = obj.read().encode()

    root = etree.fromstring(xml)
    for row in root.getchildren():
        if row.text:
            if row.tag == 'Версия':
                current_version = row.text
        if row.text:
            if row.tag == 'Дата':
                last_update = row.text
    if type_data == 'current_version':
        return current_version
    if type_data == 'last_update':
        return last_update


def save_cert(key_id):
    try:
        for certs in CERT.select().where(CERT.KeyId == key_id):
            with open(config['Folders']['certs'] + "/" + certs.KeyId + ".cer", "wb") as file:
                file.write(base64.decodebytes(certs.Data.encode()))
        os.startfile(os.path.realpath(config['Folders']['certs'] + "/"))
    except Exception:
        print('Error: save_cert(key_id)')


def open_file(file_name, file_type, url='None'):
    # open_file(sn + ".cer", "cer")
    # CryptExtAddCER «файл» Добавляет сертификат безопасности.
    # CryptExtAddCRL «файл» Добавляет список отзыва сертификатов.
    # CryptExtAddCTL «файл» Добавляет список доверия сертификатов.
    # CryptExtAddP7R «файл» Добавляет файл ответа на запрос сертификата.
    # CryptExtAddPFX «файл» Добавляет файл обмена личной информацией.
    # CryptExtAddSPC «файл» Добавляет сертификат PCKS #7.
    type_crypto_dll = ''
    folder = ''
    if file_type == 'cer':  # CryptExtOpenCER «файл» Открывает сертификат безопасности.
        type_crypto_dll = 'CryptExtOpenCER'
        folder = 'certs'
    elif file_type == 'crl':  # CryptExtOpenCRL «файл» Открывает список отзыва сертификатов.
        type_crypto_dll = 'CryptExtOpenCRL'
        folder = 'crls'
    elif file_type == 'cat':  # CryptExtOpenCAT «файл» Открывает каталог безопасности.
        type_crypto_dll = 'CryptExtOpenCAT'
        folder = 'cats'
    elif file_type == 'ctl':  # CryptExtOpenCTL «файл» Открывает список доверия сертификатов.
        type_crypto_dll = 'CryptExtOpenCTL'
        folder = 'ctls'
    elif file_type == 'p10':  # CryptExtOpenP10 «файл» Открывает запрос на сертификат.
        type_crypto_dll = 'CryptExtOpenP10'
        folder = 'p10s'
    elif file_type == 'p7r':  # CryptExtOpenP7R «файл» Открывает файл ответа на запрос сертификата.
        type_crypto_dll = 'CryptExtOpenP7R'
        folder = 'p7rs'
    elif file_type == 'pkcs7':  # CryptExtOpenPKCS7 «файл» Открывает сертификат PCKS #7.
        type_crypto_dll = 'CryptExtOpenPKCS7'
        folder = 'pkcs7s'
    elif file_type == 'str':  # CryptExtOpenSTR «файл» Открывает хранилище сериализированных сертификатов.
        type_crypto_dll = 'CryptExtOpenSTR'
        folder = 'strs'

    run_dll = "%SystemRoot%\\System32\\rundll32.exe cryptext.dll," + type_crypto_dll
    path = os.path.realpath(config['Folders'][folder] + "/" + file_name + "." + file_type)
    print(path)
    if not os.path.exists(path):
        if file_type == 'cer':
            save_cert(file_name)
        elif file_type == 'crl':
            download_file(url, file_name + '.crl', config['Folders']['crls'])
    else:
        open_crl = run_dll + "  " + path
        os.system(open_crl)


def check_custom_crl(id_custom_crl, name, id_key):
    try:
        QCoreApplication.processEvents()
        issuer = {}
        print('----------------------------------------------------')
        try:
            crl = OpenSSL.crypto.load_crl(OpenSSL.crypto.FILETYPE_ASN1,
                                          open('crls/' + str(id_key) + '.crl', 'rb').read())
            crl_crypto = crl.get_issuer()
            cryptography = crl.to_cryptography()
            try:
                for var, data in crl_crypto.get_components():
                    issuer[var.decode("utf-8")] = data.decode("utf-8")
            except Exception:
                print('Error: get_components()')
                logs('Error: check_custom_crl()::get_components()', 'errors')
            query_uc = UC.select().where(UC.OGRN == issuer['OGRN'], UC.INN == issuer['INN'])
            for uc_data in query_uc:
                name = uc_data.Name
            query_update = WatchingCustomCRL.update(INN=issuer['INN'],
                                                    OGRN=issuer['OGRN'],
                                                    status='Info: Filetype good',
                                                    last_update=cryptography.last_update +
                                                                datetime.timedelta(hours=5),
                                                    next_update=cryptography.next_update +
                                                                datetime.timedelta(hours=5)). \
                where(WatchingCustomCRL.ID == id_custom_crl)
            query_update.execute()
            print(id_custom_crl, name, cryptography.last_update, cryptography.next_update)
            issuer['INN'] = 'Unknown'
            issuer['OGRN'] = 'Unknown'
        except Exception:
            query_update = WatchingCustomCRL.update(status='Warning: FILETYPE ERROR',
                                                    last_update='1970-01-01',
                                                    next_update='1970-01-01').where(
                WatchingCustomCRL.ID == id_custom_crl)
            query_update.execute()
            print('Warning: FILETYPE ERROR')
            logs('Warning: check_custom_crl()::FILETYPE_ERROR')
    except Exception:
        print('Error: check_custom_crl()')
        logs('Error: check_custom_crl()', 'errors')


def check_crl(id_wc, name_wc, key_id_wc):
    try:
        print('----------------------------------------------------')
        try:
            crl = OpenSSL.crypto.load_crl(OpenSSL.crypto.FILETYPE_ASN1,
                                          open('crls/' + str(key_id_wc) + '.crl', 'rb').read())
            cryptography = crl.to_cryptography()
            print(cryptography.next_update)
            query_update = WatchingCRL.update(status='Info: Filetype good',
                                              last_update=cryptography.last_update + datetime.timedelta(hours=5),
                                              next_update=cryptography.next_update + datetime.timedelta(hours=5)).where(
                WatchingCRL.ID == id_wc)
            query_update.execute()
            print(id_wc, name_wc, cryptography.last_update, cryptography.next_update)
        except Exception:
            query_update = WatchingCRL.update(status='Warning: FILETYPE ERROR',
                                              last_update='1970-01-01',
                                              next_update='1970-01-01').where(WatchingCRL.ID == id_wc)
            query_update.execute()
            print('Warning: FILETYPE ERROR')
            logs('Warning: check_crl()::FILETYPE_ERROR')
    except Exception:
        print('Error: check_crl()')
        logs('Error: check_crl()', 'errors')


def check_for_import_in_uc():
    try:
        folder = config['Folders']['crls']
        current_datetime = datetime.datetime.now()
        before_current_datetime = datetime.datetime.now() - datetime.timedelta(days=5)
        query_1 = WatchingCRL.select().where(
            WatchingCRL.last_update.between(before_current_datetime, current_datetime)
        )
        query_2 = WatchingCustomCRL.select().where(
            WatchingCustomCRL.last_update.between(before_current_datetime, current_datetime)
        )
        # datetime.datetime.strptime(last_date_copy, '%Y-%m-%d %H:%M:%S')
        count = 0
        for wc in query_1:
            if current_datetime > wc.next_update:
                print('1 Need to download', wc.Name, current_datetime, wc.last_download, wc.last_update, wc.next_update)
                download_file(wc.UrlCRL, wc.KeyId + '.crl', folder, 'current', wc.ID, 'Yes')
                try:
                    shutil.copy2('crls/' + wc.KeyId + '.crl',
                                 config['Folders']['to_uc'] + 'current_' + wc.KeyId + '.crl')
                    check_crl(wc.ID, wc.Name, wc.KeyId)
                except Exception:
                    print('Error: check_for_import_in_uc()::error_copy_current')
                    logs('Error: check_for_import_in_uc()::error_copy_current', 'errors')
                count = count + 1
        for wcc in query_2:
            if current_datetime > wcc.next_update:
                print('2 Need to download', wcc.Name, current_datetime, wcc.last_download, wcc.last_update,
                      wcc.next_update)
                download_file(wcc.UrlCRL, wcc.KeyId + '.crl', folder, 'custome', wcc.ID, 'Yes')
                try:
                    shutil.copy2('crls/' + wcc.KeyId + '.crl',
                                 config['Folders']['to_uc'] + 'custom_' + wcc.KeyId + '.crl')
                    check_custom_crl(wcc.ID, wcc.Name, wcc.KeyId)
                except Exception:
                    print('Error: check_for_import_in_uc()::error_copy_custom')
                    logs('Error: check_for_import_in_uc()::error_copy_custom', 'errors')
                count = count + 1
        if count > 0:
            print('Info: Copied ' + str(count) + ' count\'s CRL')
            logs('Info: Copied ' + str(count) + ' count\'s CRL')
        else:
            print('Info: Needed CRL not found')
            logs('Info: Needed CRL not found')
    except Exception:
        print('Error: check_for_import_in_uc()')
        logs('Error: check_for_import_in_uc()', 'errors')


def download_file(file_url, file_name, folder, type_download='', w_id='', set_dd='No'):
    try:
        path = folder + '/' + file_name  # + '.' + type_file
        try:
            if config['Proxy']['proxyon'] == 'Yes':
                proxy = request.ProxyHandler({'https': 'https://10.2.248.50:8080', 'http': 'http://10.2.248.50:8080'})
                opener = request.build_opener(proxy)
                request.install_opener(opener)
                logs('Info: Used proxy')
            request.urlretrieve(file_url, path, schedule)
        except Exception:
            print('\r\n' + file_url + ' download failed!' + '\r\n')
            logs('Info: ' + file_url + ' download failed!')
            if set_dd == 'Yes':
                if type_download == 'current':
                    query_update = WatchingCRL.update(download_status='Error: Download failed',
                                                      last_download=datetime.datetime.now()
                                                      ).where(WatchingCRL.ID == w_id)
                    query_update.execute()
                elif type_download == 'custome':
                    query_update = WatchingCustomCRL.update(download_status='Error: Download failed',
                                                            last_download=datetime.datetime.now()
                                                            ).where(WatchingCustomCRL.ID == w_id)
                    query_update.execute()
            else:
                if type_download == 'current':
                    query_update = WatchingCRL.update(download_status='Error: Download failed'
                                                      ).where(WatchingCRL.ID == w_id)
                    query_update.execute()
                elif type_download == 'custome':
                    query_update = WatchingCustomCRL.update(download_status='Error: Download failed'
                                                            ).where(WatchingCustomCRL.ID == w_id)
                    query_update.execute()
        else:
            print('\r\n' + file_url + ' download successfully!')
            logs('Info: ' + file_url + ' download successfully!')
            if set_dd == 'Yes':
                if type_download == 'current':
                    query_update = WatchingCRL.update(download_status='Info: Download successfully',
                                                      last_download=datetime.datetime.now()
                                                      ).where(WatchingCRL.ID == w_id)
                    query_update.execute()
                elif type_download == 'custome':
                    query_update = WatchingCustomCRL.update(download_status='Info: Download successfully',
                                                            last_download=datetime.datetime.now()
                                                            ).where(WatchingCustomCRL.ID == w_id)
                    query_update.execute()
                # os.startfile(os.path.realpath(config['Folders']['crls'] + "/"))
            else:
                if type_download == 'current':
                    query_update = WatchingCRL.update(download_status='Info: Download successfully'
                                                      ).where(WatchingCRL.ID == w_id)
                    query_update.execute()
                elif type_download == 'custome':
                    query_update = WatchingCustomCRL.update(download_status='Info: Download successfully'
                                                            ).where(WatchingCustomCRL.ID == w_id)
                    query_update.execute()
    except Exception:
        print('Error: download_file()')
        logs('Error: download_file()', 'errors')


def export_all_watching_crl():
    query = WatchingCRL.select()
    query_2 = WatchingCustomCRL.select()
    with open(r"crl_list.txt", "w") as file:
        for url in query:
            file.write(url.UrlCRL + '\n')
    file.close()
    with open(r"crl_list.txt", "a") as file:
        for url in query_2:
            file.write(url.UrlCRL + '\n')
    file.close()


def exist_crl_in_custom_watch():
    query = WatchingCRL.select()
    for row in query:
        if WatchingCustomCRL.select().where(WatchingCustomCRL.KeyId == row.KeyId).count() > 0:
            print(row.KeyId, ' exist')


def set_value_in_property_file(file_path, section, key, value):
    set_config = configparser.ConfigParser()
    set_config.read(file_path)
    set_config.set(section, key, value)
    configfile = open(file_path, 'w')
    set_config.write(configfile, space_around_delimiters=False)  # use flag in case case you need to avoid white space.
    configfile.close()


class Worker(QObject):
    try:
        threadTimerSender = pyqtSignal(str)
        threadButtonStartE = pyqtSignal(str)
        threadButtonStopE = pyqtSignal(str)
        threadButtonStartD = pyqtSignal(str)
        threadButtonStopD = pyqtSignal(str)
        threadInfoMessage = pyqtSignal(str)
        threadBefore = pyqtSignal(str)
        threadAfter = pyqtSignal(str)

        def __init__(self):
            try:
                super(Worker, self).__init__()
                self._step = 0
                self._seconds = 0
                self._minutes = 0
                self._hour = 0
                self._day = 0
                self._isRunning = True
            except Exception:
                print('Error: Worker(QObject)::__init__')
                logs('Error: Worker(QObject)::__init__', 'errors')

        def task(self):
            try:
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
                logs('Info: Start monitoring CRL')
                self.threadInfoMessage.emit('Info: Start monitoring CRL')
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

                    # ---------------------------------------------------
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
                    # ---------------------------------------------------
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

                    # print('Дне ', day_start)
                    # print('Час ', hour_start)
                    # print('Мин ', minutes_start)
                    # print('Сек ', sec_start)
                    self.threadTimerSender.emit(timer)
                    if self._step == int(sec_to_get) - 1:
                        check_for_import_in_uc()
                        timer_b = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        timer_a = datetime.datetime.now() + datetime.timedelta(seconds=sec_to_get)
                        timer_a = datetime.datetime.strftime(timer_a, '%Y-%m-%d %H:%M:%S')
                        self.threadBefore.emit(timer_b)
                        self.threadAfter.emit(timer_a)
                        self._step = 0
                    sec_start -= 1
                    time.sleep(1)
                print('Info: Monitoring is stopped')
                logs('Info: Monitoring is stopped')
                self.threadInfoMessage.emit('Info: Monitoring is stopped')
                self.threadButtonStartE.emit('True')
                self.threadButtonStopD.emit('True')
            except Exception:
                print('Error: Worker(QObject)::task(self)')
                logs('Error: Worker(QObject)::task(self)', 'errors')

        def stop(self):
            try:
                self._isRunning = False
            except Exception:
                print('Error: Worker(QObject)::top(self)')
                logs('Error: Worker(QObject)::top(self)', 'errors')
    except Exception:
        print('Error: Worker(QObject)')
        logs('Error: Worker(QObject)', 'errors')


class Downloader(QThread):
    try:
        pre_progress = pyqtSignal(int)
        progress = pyqtSignal(int)
        done = pyqtSignal(str)
        downloading = pyqtSignal(str)

        def __init__(self, file_url, file_name):
            QThread.__init__(self)
            # Флаг инициализации
            self._init = False
            self.fileUrl = file_url
            self.fileName = file_name
            print(file_url)
            print(file_name)

        def run(self):
            try:
                logs('Info: Downloading TSL')
                if config['Proxy']['proxyon'] == 'Yes':
                    proxy = request.ProxyHandler(
                        {'https': 'https://10.2.248.50:8080', 'http': 'http://10.2.248.50:8080'})
                    opener = request.build_opener(proxy)
                    request.install_opener(opener)
                    logs('Info: Used proxy')
                request.urlretrieve(self.fileUrl, self.fileName, self._progress)
            except error.HTTPError as e:
                print(e)
                self.done.emit('Ошибка загрузки')
                logs('Info: download failed')
            except Exception:
                self.done.emit('Ошибка загрузки')
                logs('Info: download failed')
            else:
                print('Загрузка завершена')
                logs('Info: Downloading successfully')

                query_get_settings = Settings.select()
                ver_from_tsl = get_info_xlm('current_version')
                ver = 0
                for settings in query_get_settings:
                    ver = settings.value
                    break
                if int(ver) == int(ver_from_tsl):
                    print('Info: update not need')
                    logs('Info: update not need')
                    self.done.emit('Загрузка завершена, обновление не требуется')
                else:
                    print('Info: Need update')
                    logs('Info: Need update, new version ' + ver_from_tsl + ', old ' + ver)
                    self.done.emit('Загрузка завершена, требуются обновления Базы УЦ и сертификатов. Новая версия '
                                   + ver_from_tsl + ' текущая версия ' + ver)

                # get_info_xlm('last_update')
                size_tls = os.path.getsize("tsl.xml")
                self.pre_progress.emit(size_tls)
                self.progress.emit(size_tls)

        def _progress(self, block_num, block_size, total_size=int('15000000')):
            total_size = int('15000000')
            print(block_num, block_size, total_size)
            self.downloading.emit('Загрузка.')
            if not self._init:
                self.pre_progress.emit(total_size)
                self._init = True
            # Расчет текущего количества данных
            downloaded = block_num * block_size
            if downloaded < total_size:
                # Отправляем промежуток
                self.progress.emit(downloaded)
            else:
                # Чтобы было 100%
                self.progress.emit(total_size)
    except Exception:
        print('Error: Downloader(QThread)')
        logs('Error: Downloader(QThread)', 'errors')


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('assists/favicon.ico'))
        self.window_uc = None
        self.window_add_crl = None
        self.init_settings()
        self.tab_info()
        self.tab_uc()
        self.ui.lineEdit.textChanged[str].connect(self.tab_uc)
        self.tab_cert()
        self.ui.lineEdit_2.textChanged[str].connect(self.tab_cert)
        self.tab_crl()
        self.ui.lineEdit_3.textChanged[str].connect(self.tab_crl)
        self.tab_watching_crl()
        self.sub_tab_watching_crl()
        self.ui.lineEdit_4.textChanged[str].connect(self.sub_tab_watching_crl)
        self.sub_tab_watching_custom_crl()
        self.ui.lineEdit_5.textChanged[str].connect(self.sub_tab_watching_custom_crl)
        self.sub_tab_watching_off_crl()
        self.ui.lineEdit_6.textChanged[str].connect(self.sub_tab_watching_off_crl)

    def tab_info(self):
        try:
            ucs = UC.select()
            certs = CERT.select()
            crls = CRL.select()
            watching_crl = WatchingCRL.select()
            watching_custom_crl = WatchingCustomCRL.select()
            settings_ver = '0'
            settings_update_date = '0'
            query = Settings.select()
            for data in query:
                if data.name == 'ver':
                    settings_ver = data.value
                if data.name == 'data_update':
                    settings_update_date = data.value

            self.ui.label_3.setText(" Версия базы: " + settings_ver)
            self.ui.label_2.setText(" Дата выпуска базы: " + settings_update_date.replace('T', ' ').split('.')[0])
            self.ui.label.setText(" Всего УЦ: " + str(ucs.count()))
            self.ui.label_4.setText(" Всего Сертификатов: " + str(certs.count()))
            self.ui.label_5.setText(" Всего CRL: " + str(crls.count()))
            self.ui.label_6.setText(" CRL будет загружено: "
                                    + str(int(watching_crl.count())
                                          + int(watching_custom_crl.count())))
            self.ui.pushButton.clicked.connect(self.download_xml)
            self.ui.pushButton_2.clicked.connect(self.init_xml)
            self.ui.pushButton_13.clicked.connect(self.export_crl)
            self.ui.pushButton_6.pressed.connect(self.import_crl_list)

            watching_crl = WatchingCRL.select().order_by(WatchingCRL.next_update).where(
                WatchingCRL.OGRN == '1047702026701')
            self.ui.tableWidget_7.resizeColumnsToContents()
            self.ui.tableWidget_7.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
            count = 0
            self.ui.tableWidget_7.setRowCount(watching_crl.count())
            for guc in watching_crl:
                self.ui.tableWidget_7.setItem(count, 0, QTableWidgetItem(str(guc.KeyId)))
                self.ui.tableWidget_7.setItem(count, 1, QTableWidgetItem(str(guc.last_download)))
                self.ui.tableWidget_7.setItem(count, 2, QTableWidgetItem(str(guc.last_update)))
                self.ui.tableWidget_7.setItem(count, 3, QTableWidgetItem(str(guc.next_update)))
                count = count + 1
            self.ui.tableWidget_7.setColumnWidth(1, 180)
            self.ui.tableWidget_7.setColumnWidth(2, 180)
            self.ui.tableWidget_7.setColumnWidth(3, 180)
            self.ui.tableWidget_7.resizeColumnsToContents()
            self.ui.tableWidget_7.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)

            watching_crl = WatchingCRL.select().order_by(WatchingCRL.next_update).where(
                WatchingCRL.OGRN == '1020203227263')
            self.ui.tableWidget_8.resizeColumnsToContents()
            self.ui.tableWidget_8.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
            count = 0
            self.ui.tableWidget_8.setRowCount(watching_crl.count())
            for you_self in watching_crl:
                self.ui.tableWidget_8.setItem(count, 0, QTableWidgetItem(str(you_self.KeyId)))
                self.ui.tableWidget_8.setItem(count, 1, QTableWidgetItem(str(you_self.last_download)))
                self.ui.tableWidget_8.setItem(count, 2, QTableWidgetItem(str(you_self.last_update)))
                self.ui.tableWidget_8.setItem(count, 3, QTableWidgetItem(str(you_self.next_update)))
                count = count + 1
            self.ui.tableWidget_8.setColumnWidth(1, 180)
            self.ui.tableWidget_8.setColumnWidth(2, 180)
            self.ui.tableWidget_8.setColumnWidth(3, 180)
            self.ui.tableWidget_8.resizeColumnsToContents()
            self.ui.tableWidget_8.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)

            self.thread = QThread()
            self.thread.start()
            self.worker = Worker()
            self.worker.moveToThread(self.thread)

            self.worker.threadTimerSender.connect(lambda y: self.ui.label_36.setText('Время в работе: ' + str(y)))
            self.worker.threadBefore.connect(
                lambda msg: self.ui.label_37.setText('Предыдущее обновление: : ' + str(msg)))
            self.worker.threadAfter.connect(lambda msg: self.ui.label_38.setText('Следующее обновление: ' + str(msg)))
            self.worker.threadButtonStartD.connect(lambda x: self.ui.pushButton_19.setDisabled(True))
            self.worker.threadButtonStopD.connect(lambda z: self.ui.pushButton_20.setDisabled(True))
            self.worker.threadButtonStartE.connect(lambda r: self.ui.pushButton_19.setEnabled(True))
            self.worker.threadButtonStopE.connect(lambda t: self.ui.pushButton_20.setEnabled(True))
            self.worker.threadInfoMessage.connect(lambda msg: self.ui.label_7.setText(msg))
            self.worker.threadInfoMessage.connect(lambda msg: self.ui.label_7.setText(msg))
            self.worker.threadInfoMessage.connect(lambda msg: self.ui.label_7.setText(msg))
            self.ui.pushButton_20.clicked.connect(lambda: self.worker.stop() and self.stop_thread)
            self.ui.pushButton_19.clicked.connect(self.worker.task)
        except Exception:
            print('Error: tab_info()')
            logs('Error: tab_info()', 'errors')

    def tab_uc(self, text=''):
        try:
            # self.ui.label_8.setText('Ищем: ' + text)
            # self.ui.label_8.adjustSize()

            self.ui.pushButton_7.pressed.connect(lambda: self.ui.lineEdit.setText(''))

            query = UC.select().where(UC.Registration_Number.contains(text)
                                      | UC.INN.contains(text)
                                      | UC.OGRN.contains(text)
                                      | UC.Name.contains(text)
                                      | UC.Full_Name.contains(text)).limit(config['Listing']['uc'])
            count_all = UC.select().where(UC.Registration_Number.contains(text)
                                          | UC.INN.contains(text)
                                          | UC.OGRN.contains(text)
                                          | UC.Name.contains(text)
                                          | UC.Full_Name.contains(text)).limit(config['Listing']['uc']).count()
            self.ui.tableWidget.setRowCount(count_all)
            count = 0

            for row in query:
                self.ui.tableWidget.setItem(count, 0, QTableWidgetItem(str(row.Registration_Number)))
                self.ui.tableWidget.setItem(count, 1, QTableWidgetItem(str(row.INN)))
                self.ui.tableWidget.setItem(count, 2, QTableWidgetItem(str(row.OGRN)))
                self.ui.tableWidget.setItem(count, 3, QTableWidgetItem(str(row.Full_Name)))
                button_info = QPushButton()
                button_info.setFixedSize(100, 30)
                button_info.setText("Подробнее")
                reg_num = row.Registration_Number
                button_info.pressed.connect(lambda rg=reg_num: self.open_sub_window_info_uc(rg))
                self.ui.tableWidget.setCellWidget(count, 4, button_info)
                count = count + 1
            self.ui.tableWidget.resizeColumnsToContents()
            self.ui.tableWidget.horizontalHeader().setSectionResizeMode(3, QHeaderView.Stretch)
        except Exception:
            print('Error: tab_uc()')
            logs('Error: tab_uc()', 'errors')

    def tab_cert(self, text=''):
        try:
            self.ui.pushButton_8.pressed.connect(lambda: self.ui.lineEdit_2.setText(''))

            query = CERT.select().where(CERT.Registration_Number.contains(text)
                                        | CERT.Name.contains(text)
                                        | CERT.KeyId.contains(text)
                                        | CERT.Stamp.contains(text)
                                        | CERT.SerialNumber.contains(text)).limit(config['Listing']['cert'])
            count_all = CERT.select().where(CERT.Registration_Number.contains(text)
                                            | CERT.Name.contains(text)
                                            | CERT.KeyId.contains(text)
                                            | CERT.Stamp.contains(text)
                                            | CERT.SerialNumber.contains(text)).limit(config['Listing']['cert']).count()
            self.ui.tableWidget_2.setRowCount(count_all)
            count = 0
            for row in query:
                self.ui.tableWidget_2.setItem(count, 0, QTableWidgetItem(str(row.Registration_Number)))
                self.ui.tableWidget_2.setItem(count, 1, QTableWidgetItem(str(row.Name)))
                self.ui.tableWidget_2.setItem(count, 2, QTableWidgetItem(str(row.KeyId)))
                self.ui.tableWidget_2.setItem(count, 3, QTableWidgetItem(str(row.Stamp)))
                self.ui.tableWidget_2.setItem(count, 4, QTableWidgetItem(str(row.SerialNumber)))

                self.button_cert = QPushButton()
                self.button_cert.setFixedSize(150, 30)
                self.button_cert.setText("Просмотр сертификата")
                ki = row.KeyId
                self.button_cert.pressed.connect(lambda key_id=ki: open_file(key_id, "cer"))
                self.ui.tableWidget_2.setCellWidget(count, 5, self.button_cert)

                button_cert_save = QPushButton()
                button_cert_save.setFixedSize(100, 30)
                button_cert_save.setText("Сохранить")
                ki = row.KeyId
                button_cert_save.pressed.connect(lambda key_id=ki: save_cert(key_id))
                self.ui.tableWidget_2.setCellWidget(count, 6, button_cert_save)
                count = count + 1
            self.ui.tableWidget_2.resizeColumnToContents(0)
            self.ui.tableWidget_2.setColumnWidth(1, 150)
            self.ui.tableWidget_2.setColumnWidth(2, 150)
            self.ui.tableWidget_2.setColumnWidth(3, 150)
            self.ui.tableWidget_2.horizontalHeader().setSectionResizeMode(4, QHeaderView.Stretch)
            self.ui.tableWidget_2.resizeColumnToContents(5)
        except Exception:
            print('Error: tab_cert()')
            logs('Error: tab_cert()', 'errors')

    def tab_crl(self, text=''):
        try:
            self.ui.pushButton_9.pressed.connect(lambda: self.ui.lineEdit_3.setText(''))

            query = CRL.select().where(CRL.Registration_Number.contains(text)
                                       | CRL.Name.contains(text)
                                       | CRL.KeyId.contains(text)
                                       | CRL.Stamp.contains(text)
                                       | CRL.SerialNumber.contains(text)
                                       | CRL.UrlCRL.contains(text)).limit(config['Listing']['crl'])
            count_all = CRL.select().where(CRL.Registration_Number.contains(text)
                                           | CRL.Name.contains(text)
                                           | CRL.KeyId.contains(text)
                                           | CRL.Stamp.contains(text)
                                           | CRL.SerialNumber.contains(text)
                                           | CRL.UrlCRL.contains(text)).limit(config['Listing']['crl']).count()
            self.ui.tableWidget_3.setRowCount(count_all)
            count = 0
            for row in query:
                self.ui.tableWidget_3.setItem(count, 0, QTableWidgetItem(str(row.Registration_Number)))
                self.ui.tableWidget_3.setItem(count, 1, QTableWidgetItem(str(row.Name)))
                self.ui.tableWidget_3.setItem(count, 2, QTableWidgetItem(str(row.KeyId)))
                self.ui.tableWidget_3.setItem(count, 3, QTableWidgetItem(str(row.Stamp)))
                self.ui.tableWidget_3.setItem(count, 4, QTableWidgetItem(str(row.SerialNumber)))
                self.ui.tableWidget_3.setItem(count, 5, QTableWidgetItem(str(row.UrlCRL)))
                button_crl_save = QPushButton()
                button_crl_save.setFixedSize(100, 30)
                button_crl_save.setText("Скачать")
                button_crl_save.pressed.connect(
                    lambda u=row.UrlCRL, s=row.KeyId: download_file(u, s + '.crl', config['Folders']['crls']))
                self.ui.tableWidget_3.setCellWidget(count, 6, button_crl_save)

                button_add_to_watch = QPushButton()
                button_add_to_watch.setFixedSize(100, 30)
                button_add_to_watch.setText("Отслеживать")
                rb = row.Registration_Number
                ki = row.KeyId
                st = row.Stamp
                sn = row.SerialNumber
                uc = row.UrlCRL
                button_add_to_watch.pressed.connect(lambda registration_number=rb,
                                                           keyid=ki,
                                                           stamp=st,
                                                           serial_number=sn,
                                                           url_crl=uc: self.add_watch_cert_crl(registration_number,
                                                                                               keyid,
                                                                                               stamp,
                                                                                               serial_number,
                                                                                               url_crl))
                self.ui.tableWidget_3.setCellWidget(count, 7, button_add_to_watch)

                count = count + 1
            self.ui.tableWidget_3.resizeColumnToContents(0)
            self.ui.tableWidget_3.setColumnWidth(1, 150)
            self.ui.tableWidget_3.setColumnWidth(2, 150)
            self.ui.tableWidget_3.setColumnWidth(3, 150)
            self.ui.tableWidget_3.setColumnWidth(4, 150)
            self.ui.tableWidget_3.horizontalHeader().setSectionResizeMode(5, QHeaderView.Stretch)
        except Exception:
            print('Error: tab_crl()')
            logs('Error: tab_crl()', 'errors')

    def tab_watching_crl(self):
        self.ui.pushButton_4.pressed.connect(self.download_all_crls)
        self.ui.pushButton_5.clicked.connect(self.check_all_crl)
        self.ui.pushButton_3.clicked.connect(self.export_crl_to_uc)

    def sub_tab_watching_crl(self, text=''):
        try:
            self.ui.label_8.setText('Ищем: ' + text)
            self.ui.label_8.adjustSize()

            self.ui.pushButton_10.pressed.connect(lambda: self.ui.lineEdit_4.setText(''))

            query = WatchingCRL.select().where(WatchingCRL.Name.contains(text)
                                               | WatchingCRL.INN.contains(text)
                                               | WatchingCRL.OGRN.contains(text)
                                               | WatchingCRL.KeyId.contains(text)
                                               | WatchingCRL.Stamp.contains(text)
                                               | WatchingCRL.SerialNumber.contains(text)
                                               | WatchingCRL.UrlCRL.contains(text)).limit(config['Listing']['watch'])
            count_all = WatchingCRL.select().where(WatchingCRL.Name.contains(text)
                                                   | WatchingCRL.INN.contains(text)
                                                   | WatchingCRL.OGRN.contains(text)
                                                   | WatchingCRL.KeyId.contains(text)
                                                   | WatchingCRL.Stamp.contains(text)
                                                   | WatchingCRL.SerialNumber.contains(text)
                                                   | WatchingCRL.UrlCRL.contains(text)).limit(
                config['Listing']['watch']).count()
            self.ui.tableWidget_4.setRowCount(count_all)
            count = 0
            brush = QBrush(QColor(0, 255, 0, 255))
            brush.setStyle(Qt.SolidPattern)
            for row in query:
                self.ui.tableWidget_4.setItem(count, 0, QTableWidgetItem(str(row.Name)))
                self.ui.tableWidget_4.setItem(count, 1, QTableWidgetItem(str(row.INN)))
                self.ui.tableWidget_4.setItem(count, 2, QTableWidgetItem(str(row.OGRN)))
                self.ui.tableWidget_4.setItem(count, 3, QTableWidgetItem(str(row.KeyId)))
                self.ui.tableWidget_4.setItem(count, 4, QTableWidgetItem(str(row.Stamp)))
                self.ui.tableWidget_4.setItem(count, 5, QTableWidgetItem(str(row.SerialNumber)))
                self.ui.tableWidget_4.setItem(count, 6, QTableWidgetItem(str(row.UrlCRL)))
                if row.status == 'Info: Filetype good':
                    self.ui.tableWidget_4.setItem(count, 7, QTableWidgetItem('Dwn'))
                else:
                    self.ui.tableWidget_4.setItem(count, 7, QTableWidgetItem('Err'))

                button_delete_watch = QPushButton()
                button_delete_watch.setFixedSize(100, 30)
                button_delete_watch.setText("Убрать")
                id_row = row.ID
                button_delete_watch.pressed.connect(lambda o=id_row: self.move_watching_to_passed(o, 'current'))
                self.ui.tableWidget_4.setCellWidget(count, 8, button_delete_watch)
                count = count + 1
            self.ui.tableWidget_4.setColumnWidth(1, 150)
            self.ui.tableWidget_4.setColumnWidth(1, 100)
            self.ui.tableWidget_4.setColumnWidth(2, 100)
            self.ui.tableWidget_4.setColumnWidth(3, 150)
            self.ui.tableWidget_4.setColumnWidth(4, 150)
            self.ui.tableWidget_4.setColumnWidth(5, 150)
            self.ui.tableWidget_4.horizontalHeader().setSectionResizeMode(6, QHeaderView.Stretch)
            self.ui.tableWidget_4.setColumnWidth(7, 20)
        except Exception:
            print('Error: sub_tab_watching_crl()')
            logs('Error: sub_tab_watching_crl()', 'errors')

    def sub_tab_watching_custom_crl(self, text=''):
        try:
            self.ui.label_8.setText('Ищем: ' + text)
            self.ui.label_8.adjustSize()

            self.ui.pushButton_11.pressed.connect(lambda: self.ui.lineEdit_5.setText(''))
            self.ui.pushButton_25.pressed.connect(lambda: self.open_sub_window_add())

            query = WatchingCustomCRL.select().where(WatchingCustomCRL.Name.contains(text)
                                                     | WatchingCustomCRL.INN.contains(text)
                                                     | WatchingCustomCRL.OGRN.contains(text)
                                                     | WatchingCustomCRL.KeyId.contains(text)
                                                     | WatchingCustomCRL.Stamp.contains(text)
                                                     | WatchingCustomCRL.SerialNumber.contains(text)
                                                     | WatchingCustomCRL.UrlCRL.contains(text)). \
                limit(config['Listing']['watch'])
            count_all = WatchingCustomCRL.select().where(WatchingCustomCRL.Name.contains(text)
                                                         | WatchingCustomCRL.INN.contains(text)
                                                         | WatchingCustomCRL.OGRN.contains(text)
                                                         | WatchingCustomCRL.KeyId.contains(text)
                                                         | WatchingCustomCRL.Stamp.contains(text)
                                                         | WatchingCustomCRL.SerialNumber.contains(text)
                                                         | WatchingCustomCRL.UrlCRL.contains(text)). \
                limit(config['Listing']['watch']).count()
            self.ui.tableWidget_5.setRowCount(count_all)
            count = 0
            for row in query:
                self.ui.tableWidget_5.setItem(count, 0, QTableWidgetItem(str(row.Name)))
                self.ui.tableWidget_5.setItem(count, 1, QTableWidgetItem(str(row.INN)))
                self.ui.tableWidget_5.setItem(count, 2, QTableWidgetItem(str(row.OGRN)))
                self.ui.tableWidget_5.setItem(count, 3, QTableWidgetItem(str(row.KeyId)))
                self.ui.tableWidget_5.setItem(count, 4, QTableWidgetItem(str(row.Stamp)))
                self.ui.tableWidget_5.setItem(count, 5, QTableWidgetItem(str(row.SerialNumber)))
                self.ui.tableWidget_5.setItem(count, 6, QTableWidgetItem(str(row.UrlCRL)))
                if row.status == 'Info: Filetype good':
                    self.ui.tableWidget_5.setItem(count, 7, QTableWidgetItem('Dwn'))
                else:
                    self.ui.tableWidget_5.setItem(count, 7, QTableWidgetItem('Err'))

                button_delete_watch = QPushButton()
                button_delete_watch.setFixedSize(100, 30)
                button_delete_watch.setText("Убрать")
                # id = row.ID
                # button_delete_watch.pressed.connect(lambda i=id: self.delete_watching(i))
                self.ui.tableWidget_5.setCellWidget(count, 8, button_delete_watch)

                count = count + 1

            self.ui.tableWidget_5.setColumnWidth(1, 150)
            self.ui.tableWidget_5.setColumnWidth(1, 100)
            self.ui.tableWidget_5.setColumnWidth(2, 100)
            self.ui.tableWidget_5.setColumnWidth(3, 150)
            self.ui.tableWidget_5.setColumnWidth(4, 150)
            self.ui.tableWidget_5.horizontalHeader().setSectionResizeMode(6, QHeaderView.Stretch)
            self.ui.tableWidget_5.setColumnWidth(7, 20)
        except Exception:
            print('Error: sub_tab_watching_custom_crl()')
            logs('Error: sub_tab_watching_custom_crl()', 'errors')

    def sub_tab_watching_off_crl(self, text=''):
        try:
            self.ui.label_8.setText('Ищем: ' + text)
            self.ui.label_8.adjustSize()

            self.ui.pushButton_12.pressed.connect(lambda: self.ui.lineEdit_6.setText(''))

            query = WatchingDeletedCRL.select().where(WatchingDeletedCRL.Name.contains(text)
                                                      | WatchingDeletedCRL.INN.contains(text)
                                                      | WatchingDeletedCRL.OGRN.contains(text)
                                                      | WatchingDeletedCRL.KeyId.contains(text)
                                                      | WatchingDeletedCRL.Stamp.contains(text)
                                                      | WatchingDeletedCRL.SerialNumber.contains(text)
                                                      | WatchingDeletedCRL.UrlCRL.contains(text)). \
                limit(config['Listing']['watch'])
            count_all = WatchingDeletedCRL.select().where(WatchingDeletedCRL.Name.contains(text)
                                                          | WatchingDeletedCRL.INN.contains(text)
                                                          | WatchingDeletedCRL.OGRN.contains(text)
                                                          | WatchingDeletedCRL.KeyId.contains(text)
                                                          | WatchingDeletedCRL.Stamp.contains(text)
                                                          | WatchingDeletedCRL.SerialNumber.contains(text)
                                                          | WatchingDeletedCRL.UrlCRL.contains(text)). \
                limit(config['Listing']['watch']).count()
            self.ui.tableWidget_6.setRowCount(count_all)
            count = 0
            for row in query:
                self.ui.tableWidget_6.setItem(count, 0, QTableWidgetItem(str(row.Name)))
                self.ui.tableWidget_6.setItem(count, 1, QTableWidgetItem(str(row.INN)))
                self.ui.tableWidget_6.setItem(count, 2, QTableWidgetItem(str(row.OGRN)))
                self.ui.tableWidget_6.setItem(count, 3, QTableWidgetItem(str(row.KeyId)))
                self.ui.tableWidget_6.setItem(count, 4, QTableWidgetItem(str(row.Stamp)))
                self.ui.tableWidget_6.setItem(count, 5, QTableWidgetItem(str(row.SerialNumber)))
                self.ui.tableWidget_6.setItem(count, 6, QTableWidgetItem(str(row.UrlCRL)))

                # buttonDeleteWatch = QPushButton()
                # buttonDeleteWatch.setFixedSize(100, 30)
                # buttonDeleteWatch.setText("Удалить")
                # self.tableWidgetDeletedWatchingCRL.setCellWidget(count, 7, buttonDeleteWatch)
                #
                count = count + 1

            self.ui.tableWidget_6.setColumnWidth(1, 150)
            self.ui.tableWidget_6.setColumnWidth(1, 100)
            self.ui.tableWidget_6.setColumnWidth(2, 100)
            self.ui.tableWidget_6.setColumnWidth(3, 150)
            self.ui.tableWidget_6.setColumnWidth(4, 150)
            self.ui.tableWidget_6.setColumnWidth(5, 150)
            self.ui.tableWidget_6.horizontalHeader().setSectionResizeMode(6, QHeaderView.Stretch)
        except Exception:
            print('Error: sub_tab_watching_off_crl()')
            logs('Error: sub_tab_watching_off_crl()', 'errors')

    def init_settings(self):
        try:
            # main config
            self.ui.lineEdit_13.setText(config['Tabs']['ucLimit'])
            self.ui.lineEdit_18.setText(config['Tabs']['certLimit'])
            self.ui.lineEdit_17.setText(config['Tabs']['crlLimit'])
            self.ui.lineEdit_16.setText(config['Tabs']['wcLimit'])
            self.ui.lineEdit_15.setText(config['Tabs']['wccLimit'])
            self.ui.lineEdit_14.setText(config['Tabs']['wcdLimit'])

            if config['Sec']['allowImportCRL'] == 'Yes':
                self.ui.checkBox_4.setChecked(True)
            else:
                self.ui.pushButton_6.setDisabled(True)
            if config['Sec']['allowExportCRL'] == 'Yes':
                self.ui.checkBox_5.setChecked(True)
            else:
                self.ui.pushButton_13.setDisabled(True)
            if config['Sec']['allowDeleteWatchingCRL'] == 'Yes':
                self.ui.checkBox_6.setChecked(True)
                # self.ui.pushButton_X.setDisabled(True)
            if config['Sec']['allowDownloadButtonCRL'] == 'Yes':
                self.ui.checkBox_7.setChecked(True)
            else:
                self.ui.pushButton_4.setDisabled(True)
            if config['Sec']['allowCheckButtonCRL'] == 'Yes':
                self.ui.checkBox_8.setChecked(True)
            else:
                self.ui.pushButton_5.setDisabled(True)

            # Interface  config
            self.ui.lineEdit_12.setText(config['MainWindow']['height'])
            self.ui.lineEdit_11.setText(config['MainWindow']['width'])
            if config['MainWindow']['saveWidth'] == 'Yes':
                self.ui.checkBox_3.setChecked(True)
            if config['MainWindow']['AllowResize'] == 'Yes':
                self.ui.checkBox_2.setChecked(True)

            # download config
            self.ui.label_13.setText(config['Folders']['crls'])
            self.ui.label_12.setText(config['Folders']['certs'])
            self.ui.label_11.setText(config['Folders']['to_uc'])
            self.ui.label_10.setText(config['Folders']['tmp'])
            self.ui.label_9.setText(config['Folders']['to_uc'])

            self.ui.pushButton_18.clicked.connect(lambda: self.choose_directory('crl'))
            self.ui.pushButton_17.clicked.connect(lambda: self.choose_directory('cert'))
            self.ui.pushButton_16.clicked.connect(lambda: self.choose_directory('to_uc'))
            self.ui.pushButton_15.clicked.connect(lambda: self.choose_directory('tmp'))
            self.ui.pushButton_14.clicked.connect(lambda: self.choose_directory('uc'))

            self.ui.lineEdit_7.setText(config['Proxy']['ip'])
            self.ui.lineEdit_8.setText(config['Proxy']['port'])
            self.ui.lineEdit_9.setText(config['Proxy']['login'])
            self.ui.lineEdit_10.setText(config['Proxy']['password'])

            if config['Proxy']['proxyon'] == 'No':
                self.ui.checkBox.setChecked(False)
                self.ui.lineEdit_7.setDisabled(True)
                self.ui.lineEdit_8.setDisabled(True)
                self.ui.lineEdit_9.setDisabled(True)
                self.ui.lineEdit_10.setDisabled(True)
            elif config['Proxy']['proxyon'] == 'Yes':
                self.ui.checkBox.setChecked(True)
                self.ui.lineEdit_7.setEnabled(True)
                self.ui.lineEdit_8.setEnabled(True)
                self.ui.lineEdit_9.setEnabled(True)
                self.ui.lineEdit_10.setEnabled(True)

            # Logs
            try:
                self.ui.textBrowser.setText(
                    open('logs/log_' + datetime.datetime.now().strftime('%Y%m%d') + '.log', 'r').read())
            except Exception:
                logs('Error: init_settings()::Filed_open_log::logs/log_' + datetime.datetime.now().strftime(
                    '%Y%m%d') + '.log', 'errors')
            try:
                self.ui.textBrowser_2.setText(
                    open('logs/error_' + datetime.datetime.now().strftime('%Y%m%d') + '.log', 'r').read())
            except Exception:
                logs('Error: init_settings()::Filed_open_log::logs/error_' + datetime.datetime.now().strftime(
                    '%Y%m%d') + '.log', 'errors')

            self.ui.pushButton_21.pressed.connect(lambda: self.save_settings_main())
            self.ui.pushButton_22.pressed.connect(lambda: self.save_settings_interface())
            self.ui.pushButton_23.pressed.connect(lambda: self.save_settings_downloads())
            self.ui.pushButton_24.pressed.connect(lambda: self.save_settings_logs())
        except Exception:
            print('Error: init_settings()')
            logs('Error: init_settings()', 'errors')

    def save_settings_main(self):
        try:
            set_value_in_property_file('settings.ini', 'Tabs', 'ucLimit', self.ui.lineEdit_13.text())
            set_value_in_property_file('settings.ini', 'Tabs', 'certLimit', self.ui.lineEdit_18.text())
            set_value_in_property_file('settings.ini', 'Tabs', 'crlLimit', self.ui.lineEdit_17.text())
            set_value_in_property_file('settings.ini', 'Tabs', 'wcLimit', self.ui.lineEdit_16.text())
            set_value_in_property_file('settings.ini', 'Tabs', 'wccLimit', self.ui.lineEdit_15.text())
            set_value_in_property_file('settings.ini', 'Tabs', 'wcdLimit', self.ui.lineEdit_14.text())

            if self.ui.checkBox_4.checkState() == 0:
                set_value_in_property_file('settings.ini', 'Sec', 'allowImportCRL', 'No')
                self.ui.pushButton_6.setDisabled(True)
            elif self.ui.checkBox_4.checkState() == 2:
                set_value_in_property_file('settings.ini', 'Sec', 'allowImportCRL', 'Yes')
                self.ui.pushButton_6.setEnabled(True)
            if self.ui.checkBox_5.checkState() == 0:
                set_value_in_property_file('settings.ini', 'Sec', 'allowExportCRL', 'No')
                self.ui.pushButton_13.setDisabled(True)
            elif self.ui.checkBox_5.checkState() == 2:
                set_value_in_property_file('settings.ini', 'Sec', 'allowExportCRL', 'Yes')
                self.ui.pushButton_13.setEnabled(True)
            if self.ui.checkBox_6.checkState() == 0:
                set_value_in_property_file('settings.ini', 'Sec', 'allowDeleteWatchingCRL', 'No')
            elif self.ui.checkBox_6.checkState() == 2:
                set_value_in_property_file('settings.ini', 'Sec', 'allowDeleteWatchingCRL', 'Yes')
            if self.ui.checkBox_7.checkState() == 0:
                set_value_in_property_file('settings.ini', 'Sec', 'allowDownloadButtonCRL', 'No')
                self.ui.pushButton_4.setDisabled(True)
            elif self.ui.checkBox_7.checkState() == 2:
                set_value_in_property_file('settings.ini', 'Sec', 'allowDownloadButtonCRL', 'Yes')
                self.ui.pushButton_4.setEnabled(True)
            if self.ui.checkBox_8.checkState() == 0:
                set_value_in_property_file('settings.ini', 'Sec', 'allowCheckButtonCRL', 'No')
                self.ui.pushButton_5.setDisabled(True)
            elif self.ui.checkBox_8.checkState() == 2:
                set_value_in_property_file('settings.ini', 'Sec', 'allowCheckButtonCRL', 'Yes')
                self.ui.pushButton_5.setEnabled(True)

            print('Info: save_settings_main()::Saved')
            logs('Info: save_settings_main()::Saved')
        except Exception:
            print('Error: save_settings_main()')
            logs('Error: save_settings_main()', 'errors')

    def save_settings_interface(self):
        set_value_in_property_file('settings.ini', 'MainWindow', 'width', self.ui.lineEdit_12.text())
        set_value_in_property_file('settings.ini', 'MainWindow', 'height', self.ui.lineEdit_11.text())

        if self.ui.checkBox_3.checkState() == 0:
            set_value_in_property_file('settings.ini', 'MainWindow', 'allowresize', 'No')

        elif self.ui.checkBox_3.checkState() == 2:
            set_value_in_property_file('settings.ini', 'MainWindow', 'allowresize', 'Yes')

        if self.ui.checkBox_2.checkState() == 0:
            set_value_in_property_file('settings.ini', 'MainWindow', 'savewidth', 'No')

        elif self.ui.checkBox_2.checkState() == 2:
            set_value_in_property_file('settings.ini', 'MainWindow', 'savewidth', 'Yes')

    def save_settings_downloads(self):
        set_value_in_property_file('settings.ini', 'Folders', 'certs', self.ui.label_13.text())
        set_value_in_property_file('settings.ini', 'Folders', 'crls', self.ui.label_12.text())
        set_value_in_property_file('settings.ini', 'Folders', 'tmp', self.ui.label_11.text())
        set_value_in_property_file('settings.ini', 'Folders', 'logs', self.ui.label_10.text())
        set_value_in_property_file('settings.ini', 'Folders', 'to_uc', self.ui.label_9.text())

        set_value_in_property_file('settings.ini', 'Proxy', 'ip', self.ui.lineEdit_7.text())
        set_value_in_property_file('settings.ini', 'Proxy', 'port', self.ui.lineEdit_8.text())
        set_value_in_property_file('settings.ini', 'Proxy', 'login', self.ui.lineEdit_9.text())
        set_value_in_property_file('settings.ini', 'Proxy', 'password', self.ui.lineEdit_10.text())

        if self.ui.checkBox_12.checkState() == 0:
            set_value_in_property_file('settings.ini', 'Update', 'advancedchecking', 'No')
        elif self.ui.checkBox_12.checkState() == 2:
            set_value_in_property_file('settings.ini', 'Update', 'advancedchecking', 'Yes')
        if self.ui.checkBox_13.checkState() == 0:
            set_value_in_property_file('settings.ini', 'Update', 'viewingcrllastnextupdate', 'No')
        elif self.ui.checkBox_13.checkState() == 2:
            set_value_in_property_file('settings.ini', 'Update', 'viewingcrllastnextupdate', 'Yes')

        if self.ui.checkBox.checkState() == 0:
            set_value_in_property_file('settings.ini', 'Proxy', 'proxyon', 'No')
            self.ui.lineEdit_7.setDisabled(True)
            self.ui.lineEdit_8.setDisabled(True)
            self.ui.lineEdit_9.setDisabled(True)
            self.ui.lineEdit_10.setDisabled(True)
        elif self.ui.checkBox.checkState() == 2:
            set_value_in_property_file('settings.ini', 'Proxy', 'proxyon', 'Yes')
            self.ui.lineEdit_7.setEnabled(True)
            self.ui.lineEdit_8.setEnabled(True)
            self.ui.lineEdit_9.setEnabled(True)
            self.ui.lineEdit_10.setEnabled(True)

    def save_settings_logs(self):
        print()

    def init_xml(self):
        try:
            self.ui.pushButton_2.setEnabled(False)
            self.ui.pushButton.setEnabled(False)
            UC.drop_table()
            CRL.drop_table()
            CERT.drop_table()
            UC.create_table()
            CERT.create_table()
            CRL.create_table()
            self.ui.label_7.setText('Обрабатываем данные.')
            logs('Info: Init TLS started')
            with open('tsl.xml', "rt", encoding="utf-8") as obj:
                xml = obj.read().encode()

            root = etree.fromstring(xml)
            uc_count = 0
            cert_count = 0
            crl_count = 0
            crl_count_all = 3267
            current_version = 'Unknown'
            last_update = 'Unknown'
            for appt in root.getchildren():
                QCoreApplication.processEvents()
                address_code = ''
                address_name = ''
                address_index = ''
                address_address = ''
                address_street = ''
                address_town = ''
                registration_number = ''
                inn = ''
                ogrn = ''
                full_name = ''
                email = ''
                name = ''
                url = ''
                key_id = ''
                stamp = ''
                serial_number = ''
                cert_base64 = ''
                cert_data = []
                if appt.text:
                    if appt.tag == 'Версия':
                        current_version = appt.text
                if appt.text:
                    if appt.tag == 'Дата':
                        last_update = appt.text
                for elem in appt.getchildren():
                    if not elem.text:
                        for sub_elem in elem.getchildren():
                            if not sub_elem.text:
                                for two_elem in sub_elem.getchildren():
                                    if not two_elem.text:
                                        for tree_elem in two_elem.getchildren():
                                            if not tree_elem.text:
                                                if tree_elem.tag == 'Ключ':
                                                    data_cert = {}
                                                    adr_crl = []
                                                    key_ident = {}
                                                    for four_elem in tree_elem.getchildren():
                                                        if not four_elem.text:
                                                            for five_elem in four_elem.getchildren():
                                                                if not five_elem.text:
                                                                    for six_elem in five_elem.getchildren():
                                                                        if six_elem.text:
                                                                            if six_elem.tag == 'Отпечаток':
                                                                                data_cert['stamp'] = six_elem.text
                                                                            if six_elem.tag == 'СерийныйНомер':
                                                                                cert_count = cert_count + 1
                                                                                data_cert['serrial'] = six_elem.text
                                                                            if six_elem.tag == 'Данные':
                                                                                data_cert['data'] = six_elem.text
                                                                else:
                                                                    if five_elem.tag == 'Адрес':
                                                                        five_text = five_elem.text
                                                                        adr_crl.append(five_text)
                                                                        crl_count = crl_count + 1
                                                        else:
                                                            four_text = four_elem.text
                                                            if four_elem.tag == 'ИдентификаторКлюча':
                                                                key_ident['keyid'] = four_text
                                                    cert_data.append([key_ident, data_cert, adr_crl])
                                    else:
                                        two_text = two_elem.text
                                        if two_elem.tag == 'Код':
                                            address_code = two_text
                                        if two_elem.tag == 'Название':
                                            address_name = two_text
                            else:
                                sub_text = sub_elem.text
                                if sub_elem.tag == 'Индекс':
                                    address_index = sub_text
                                if sub_elem.tag == 'УлицаДом':
                                    address_street = sub_text
                                if sub_elem.tag == 'Город':
                                    address_town = sub_text
                                if sub_elem.tag == 'Страна':
                                    address_address = sub_text
                    else:
                        text = elem.text
                        if elem.tag == 'Название':
                            full_name = text
                        if elem.tag == 'ЭлектроннаяПочта':
                            email = text
                        if elem.tag == 'КраткоеНазвание':
                            name = text
                        if elem.tag == 'АдресСИнформациейПоУЦ':
                            url = text
                        if elem.tag == 'ИНН':
                            inn = text
                        if elem.tag == 'ОГРН':
                            ogrn = text
                        if elem.tag == 'РеестровыйНомер':
                            registration_number = text
                            uc_count = uc_count + 1
                if registration_number != '':
                    self.ui.label_7.setText('Обрабатываем данные:\n УЦ: ' + name)
                    logs('Info: Processing - UC:' + name)
                    uc = UC(Registration_Number=registration_number,
                            INN=inn,
                            OGRN=ogrn,
                            Full_Name=full_name,
                            Email=email,
                            Name=name,
                            URL=url,
                            AddresCode=address_code,
                            AddresName=address_name,
                            AddresIndex=address_index,
                            AddresAddres=address_address,
                            AddresStreet=address_street,
                            AddresTown=address_town)
                    uc.save()
                    for cert in cert_data:
                        if type(cert_data) == list:
                            for data in cert:
                                if type(data) == dict:
                                    for var, dats in data.items():
                                        if var == 'keyid':
                                            key_id = dats
                                        if var == 'stamp':
                                            stamp = dats
                                        if var == 'serrial':
                                            serial_number = dats
                                        if var == 'data':
                                            cert_base64 = dats

                                if type(data) == list:
                                    for dats in data:
                                        url_crl = dats
                                        crl = CRL(Registration_Number=registration_number,
                                                  Name=name,
                                                  KeyId=key_id,
                                                  Stamp=stamp,
                                                  SerialNumber=serial_number,
                                                  UrlCRL=url_crl)
                                        crl.save()
                        cert = CERT(Registration_Number=registration_number,
                                    Name=name,
                                    KeyId=key_id,
                                    Stamp=stamp,
                                    SerialNumber=serial_number,
                                    Data=cert_base64)
                        cert.save()

                        # uc_percent_step = int(math.floor(100 / (uc_count_all / uc_count)))
                        # cert_percent_step = int(math.floor(100 / (cert_count_all / cert_count)))
                        crl_percent_step = int(math.floor(100 / (crl_count_all / crl_count)))
                        self.ui.progressBar_2.setValue(crl_percent_step)
            self.ui.label_3.setText(" Версия базы: " + current_version)
            self.ui.label_2.setText(" Дата выпуска базы: " + last_update.replace('T', ' ').split('.')[0])
            self.ui.label.setText(" Всего УЦ: " + str(uc_count))
            self.ui.label_4.setText(" Всего Сертификатов: " + str(cert_count))
            self.ui.label_5.setText(" Всего CRL: " + str(crl_count))

            query_ver = Settings.update(value=current_version).where(Settings.name == 'ver')
            query_ver.execute()
            query_data_update = Settings.update(value=last_update).where(Settings.name == 'data_update')
            query_data_update.execute()
            self.ui.pushButton.setEnabled(True)
            self.ui.pushButton_2.setEnabled(True)
            self.ui.label_7.setText('Готово.')
            logs('Info: Processing successful done')
        except Exception:
            print('Error: init_xml()')
            logs('Error: init_xml()', 'errors')

    def open_sub_window_info_uc(self, reg_number):
        try:
            if self.window_uc is None:
                self.window_uc = UcWindow(reg_number)
                self.window_uc.show()
            else:
                self.window_uc.close()  # Close window.
                self.window_uc = None  # Discard reference.
        except Exception:
            print('Error: open_sub_window_info_uc()')
            logs('Error: open_sub_window_info_uc()', 'errors')

    def open_sub_window_add(self):
        try:
            if self.window_add_crl is None:
                self.window_add_crl = AddCRLWindow()
                self.window_add_crl.show()
            else:
                self.window_add_crl.close()  # Close window.
                self.window_add_crl = None  # Discard reference.
        except Exception:
            print('Error: open_sub_window_info_uc()')
            logs('Error: open_sub_window_info_uc()', 'errors')

    def choose_directory(self, type):
        try:
            input_dir = QFileDialog.getExistingDirectory(None, 'Выбор директории:', os.path.expanduser("~"))
            if type == 'crl':
                self.ui.label_13.setText(input_dir)
            if type == 'cert':
                self.ui.label_12.setText(input_dir)
            if type == 'uc':
                self.ui.label_9.setText(input_dir)
            if type == 'tmp':
                self.ui.label_10.setText(input_dir)
            if type == 'to_uc':
                self.ui.label_11.setText(input_dir)
        except Exception:
            print('Error: choose_directory()')
            logs('Error: choose_directory()', 'errors')

    def check_all_crl(self):
        try:
            query_1 = WatchingCRL.select()
            query_2 = WatchingCustomCRL.select()
            self.ui.pushButton_5.setEnabled(False)
            self.ui.label_8.setText('Проверяем основной список CRL')
            for wc in query_1:
                check_crl(wc.ID, wc.Name, wc.KeyId)
            self.ui.label_8.setText('Проверяем свой список CRL')
            for wcc in query_2:
                check_custom_crl(wcc.ID, wcc.Name, wcc.KeyId)
            self.ui.label_8.setText('Готово')
            self.ui.pushButton_5.setEnabled(True)
            # self.textBrowser.setText(open('main.log', 'rb').read().decode())
        except Exception:
            print('Error: check_all_crl()')
            logs('Error: check_all_crl()', 'errors')

    def add_watch_cert_crl(self, registration_number, keyid, stamp, serial_number, url_crl):
        try:
            count = WatchingCRL.select().where(WatchingCRL.Stamp.contains(stamp)
                                               | WatchingCRL.SerialNumber.contains(serial_number)).count()
            print(count)
            if count < 1:
                select_uc = UC.select().where(UC.Registration_Number == registration_number)
                for row in select_uc:
                    add_to_watching_crl = WatchingCRL(Name=row.Name,
                                                      INN=row.INN,
                                                      OGRN=row.OGRN,
                                                      KeyId=keyid,
                                                      Stamp=stamp,
                                                      SerialNumber=serial_number,
                                                      UrlCRL=url_crl,
                                                      status='Unknown',
                                                      download_status='Unknown',
                                                      download_count='0',
                                                      last_download='1970-01-01 00:00:00',
                                                      last_update='1970-01-01 00:00:00',
                                                      next_update='1970-01-01 00:00:00'
                                                      )
                    add_to_watching_crl.save()
                    # self.counter_added = self.counter_added + 1
            else:
                print('crl exist')
                logs('Info: add_watch_cert_crl()::Crl_Exist:' + keyid)
                # self.counter_added_exist = self.counter_added_exist + 1
            # self.on_changed_find_watching_crl('')
        except Exception:
            print('Error: add_watch_cert_crl()')
            logs('Error: add_watch_cert_crl()', 'errors')

    def add_watch_custom_cert_crl(self, url_crl):
        try:
            count = WatchingCustomCRL.select().where(WatchingCustomCRL.UrlCRL.contains(url_crl)).count()
            if count < 1:
                add_to_watching_crl = WatchingCustomCRL(Name='Unknown',
                                                        INN='0',
                                                        OGRN='0',
                                                        KeyId='Unknown',
                                                        Stamp='Unknown',
                                                        SerialNumber='Unknown',
                                                        UrlCRL=url_crl)
                add_to_watching_crl.save()
                self.counter_added_custom = self.counter_added_custom + 1
            else:
                print('crl exist')
                logs('Info: add_watch_custom_cert_crl()::Crl_Exist:' + url_crl)
                self.counter_added_exist = self.counter_added_exist + 1
            self.on_changed_find_watching_crl('')
        except Exception:
            print('Error: add_watch_custom_cert_crl()')
            logs('Error: add_watch_custom_cert_crl()', 'errors')

    def move_watching_to_passed(self, id_var, from_var):
        try:
            if from_var == 'current':
                from_bd = WatchingCRL.select().where(WatchingCRL.ID == id_var)
                for row in from_bd:
                    to_bd = WatchingDeletedCRL(Name=row.Name,
                                               INN=row.INN,
                                               OGRN=row.OGRN,
                                               KeyId=row.KeyId,
                                               Stamp=row.Stamp,
                                               SerialNumber=row.SerialNumber,
                                               UrlCRL=row.UrlCRL)
                    to_bd.save()
                WatchingCRL.delete_by_id(id_var)
                self.on_changed_find_watching_crl()
                self.on_changed_find_deleted_watching_crl()
            elif from_var == 'custom':
                WatchingCustomCRL.delete_by_id(id_var)
                self.on_changed_find_deleted_watching_crl('')
            else:
                print('Error: Ошибка перемещения')
                logs('Error: add_watch_custom_cert_crl()::Error_Moving', 'errors')
        except Exception:
            print('Error: move_watching_to_delete()')
            logs('Error: move_watching_to_delete()', 'errors')

    # def delete_watching(self, id):
    #     WatchingCRL.delete_by_id(id)
    #     self.on_changed_find_watching_crl('')
    #     print(id + ' id is deleted')

    def download_xml(self):
        try:
            self.ui.label_7.setText('Скачиваем список.')
            self.ui.label_7.adjustSize()
            self.ui.pushButton.setEnabled(False)
            self.ui.pushButton_2.setEnabled(False)
            self._download = Downloader('https://e-trust.gosuslugi.ru/CA/DownloadTSL?schemaVersion=0', 'tsl.xml')
            # Устанавливаем максимальный размер данных
            self._download.pre_progress.connect(lambda x: self.ui.progressBar.setMaximum(x))
            # Промежуточный/скачанный размер
            self._download.progress.connect(lambda y: self.ui.progressBar.setValue(y))
            # говорим что всё скачано
            self._download.downloading.connect(lambda z: self.ui.label_7.setText(z))
            self._download.done.connect(lambda z: self.ui.label_7.setText(z))
            self._download.done.connect(lambda hint1: self.ui.pushButton.setEnabled(True))
            self._download.done.connect(lambda hint2: self.ui.pushButton_2.setEnabled(True))
            # self._download.done.connect(lambda hint3: self.on_changed_find_uc(''))
            # self._download.done.connect(lambda hint4: self.on_changed_find_cert(''))
            # self._download.done.connect(lambda hint5: self.on_changed_find_crl(''))
            self._download.start()
        except Exception:
            print('Error: download_xml()')
            logs('Error: download_xml()', 'errors')

    def download_all_crls(self):
        try:
            self.ui.pushButton_4.setEnabled(False)
            QCoreApplication.processEvents()
            query_1 = WatchingCRL.select()
            query_2 = WatchingCustomCRL.select()
            counter_watching_crl_all = WatchingCRL.select().count()
            watching_custom_crl_all = WatchingCustomCRL.select().count()
            counter_watching_crl = 0
            counter_watching_custom_crl = 0
            self.ui.label_8.setText('Загрузка началась')
            for wc in query_1:
                QCoreApplication.processEvents()
                counter_watching_crl = counter_watching_crl + 1
                file_url = wc.UrlCRL
                file_name = wc.KeyId + '.crl'
                # file_name = wc.UrlCRL.split('/')[-1]
                # file_name = wcc.KeyId
                folder = config['Folders']['crls']
                self.ui.label_8.setText(
                    str(counter_watching_crl) + ' из ' + str(counter_watching_crl_all) + ' Загружаем: ' + str(
                        wc.Name) + ' ' + str(wc.KeyId))
                download_file(file_url, file_name, folder, 'current', wc.ID)
                # Downloader(str(wc.UrlCRL), str(wc.SerialNumber)+'.crl')
            print('WatchingCRL downloaded ' + str(counter_watching_crl))
            logs('Info: WatchingCRL downloaded ' + str(counter_watching_crl))
            for wcc in query_2:
                QCoreApplication.processEvents()
                counter_watching_custom_crl = counter_watching_custom_crl + 1
                file_url = wcc.UrlCRL
                file_name = wcc.KeyId + '.crl'
                # file_name = wcc.UrlCRL.split('/')[-1]
                # file_name = wcc.KeyId
                folder = config['Folders']['crls']
                self.ui.label_8.setText(
                    str(counter_watching_custom_crl) + ' из ' + str(watching_custom_crl_all) + ' Загружаем: ' + str(
                        wcc.Name) + ' ' + str(wcc.KeyId))
                download_file(file_url, file_name, folder, 'custome', wcc.ID)
                # Downloader(str(wcc.UrlCRL), str(wcc.SerialNumber)+'.crl'
            self.ui.label_8.setText('Загрузка закончена')
            print('WatchingCustomCRL downloaded ' + str(counter_watching_custom_crl))
            logs('Info: WatchingCustomCRL downloaded ' + str(counter_watching_custom_crl))
            print('All download done, w=' + str(counter_watching_crl) + ', c=' + str(counter_watching_custom_crl))
            logs('Info: All download done, w=' + str(counter_watching_crl) + ', c=' + str(counter_watching_custom_crl))
            self.ui.pushButton_4.setEnabled(True)
        except Exception:
            print('Error: download_all_crls()')
            logs('Error: download_all_crls()', 'errors')

    def import_crl_list(self, file_name='crl_list.txt'):
        try:
            path = os.path.realpath(file_name)
            if os.path.exists(path):
                crl_list = open(file_name, 'r')
                crl_lists = crl_list.readlines()
                for crl_url in crl_lists:
                    QCoreApplication.processEvents()
                    crl_url = crl_url.replace("\n", "")
                    QCoreApplication.processEvents()
                    print(crl_url)
                    count = CRL.select().where(CRL.UrlCRL.contains(crl_url)).count()
                    data = CRL.select().where(CRL.UrlCRL.contains(crl_url))
                    if count > 0:
                        for row in data:
                            print(row.Registration_Number)
                            self.add_watch_cert_crl(row.Registration_Number, row.KeyId, row.Stamp, row.SerialNumber,
                                                    row.UrlCRL)
                    else:
                        print('add to custom')
                        self.add_watch_custom_cert_crl(crl_url)
                    # self.on_changed_find_watching_crl('')
                print(self.counter_added, self.counter_added_custom, self.counter_added_exist)
            else:
                print('Not found crl_list.txt')
                logs('Info: Not found crl_list.txt')
        except Exception:
            print('Error: import_crl_list()')
            logs('Error: import_crl_list()', 'errors')

    def export_crl(self):
        self.ui.label_7.setText('Генерируем файл')
        export_all_watching_crl()
        self.ui.label_7.setText('Файл сгенерирован')

    def export_crl_to_uc(self):
        self.ui.pushButton_3.setEnabled(False)
        self.ui.label_8.setText('Обрабатываем CRL для загрузки в УЦ')
        check_for_import_in_uc()
        self.ui.label_8.setText('Все CRL обработаны')
        self.ui.pushButton_3.setEnabled(True)

    def stop_thread(self):
        self.worker.stop()
        self.thread.quit()
        self.thread.wait()


class UcWindow(QWidget):
    def __init__(self, reg_number):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('assists/favicon.ico'))
        self.init(reg_number)

    def init(self, reg_number):
        try:
            registration_number = 'Unknown'
            inn = 'Unknown'
            ogrn = 'Unknown'
            full_name = 'Unknown'
            email = 'Unknown'
            name = 'Unknown'
            url = 'Unknown'
            address_code = 'Unknown'
            address_name = 'Unknown'
            address_index = 'Unknown'
            address_address = 'Unknown'
            address_street = 'Unknown'
            address_town = 'Unknown'
            query = UC.select().where(UC.Registration_Number == reg_number)
            for row in query:
                registration_number = 'Регистрационный номер: ' + str(row.Registration_Number)
                inn = 'ИНН: ' + str(row.INN)
                ogrn = 'ОГРН: ' + str(row.OGRN)
                full_name = 'Полное название организации: ' + str(row.Full_Name)
                email = 'Электронная почта: ' + str(row.Email)
                name = 'Название организации: ' + str(row.Name)
                url = 'Интернет адрес: ' + str(row.URL)
                address_code = 'Код региона: ' + str(row.AddresCode)
                address_name = 'Регион: ' + str(row.AddresName)
                address_index = 'Почтовый индекс: ' + str(row.AddresIndex)
                address_address = 'Код страны: ' + str(row.AddresAddres)
                address_street = 'Улица: ' + str(row.AddresStreet)
                address_town = 'Город : ' + str(row.AddresTown)

            self.setWindowTitle(name)
            self.setWindowIcon(QIcon('assists/favicon.ico'))

            self.ui.label_7.setText(registration_number)
            self.ui.label_6.setText(inn)
            self.ui.label_5.setText(ogrn)
            self.ui.label_4.setText(full_name)
            self.ui.label_3.setText(email)
            self.ui.label_2.setText(url)
            self.ui.label.setText(name)

            self.ui.label_13.setText(address_code)
            self.ui.label_12.setText(address_name)
            self.ui.label_11.setText(address_index)
            self.ui.label_10.setText(address_address)
            self.ui.label_8.setText(address_street)
            self.ui.label_9.setText(address_town)

            query = CRL.select().where(CRL.Registration_Number == reg_number)
            query_count = CRL.select().where(CRL.Registration_Number == reg_number).count()
            self.ui.tableWidget.setRowCount(query_count)
            count = 0
            try:
                for row in query:
                    self.ui.tableWidget.setItem(count, 0, QTableWidgetItem(str(row.Registration_Number)))
                    self.ui.tableWidget.setItem(count, 1, QTableWidgetItem(str(row.KeyId)))
                    self.ui.tableWidget.setItem(count, 2, QTableWidgetItem(str(row.Stamp)))
                    self.ui.tableWidget.setItem(count, 3, QTableWidgetItem(str(row.SerialNumber)))
                    self.ui.tableWidget.setItem(count, 4, QTableWidgetItem(str()))
                    self.ui.tableWidget.setItem(count, 5, QTableWidgetItem(str(row.UrlCRL)))
                    count = count + 1
                self.ui.tableWidget.setColumnWidth(0, 50)
                self.ui.tableWidget.setColumnWidth(1, 150)
                self.ui.tableWidget.setColumnWidth(2, 150)
                self.ui.tableWidget.setColumnWidth(3, 150)
                self.ui.tableWidget.setColumnWidth(4, 150)
                self.ui.tableWidget.horizontalHeader().setSectionResizeMode(5, QHeaderView.Stretch)
            except Exception:
                print('Error: UcWindow()::init()::query_to_row')
                logs('Error: UcWindow()::init()::query_to_row', 'errors')
        except Exception:
            print('Error: UcWindow()::init()')
            logs('Error: UcWindow()::init()', 'errors')


class AddCRLWindow(QWidget):
    def __init__(self):
        try:
            super().__init__()
            self.ui_add = Ui_Form_add()
            self.ui_add.setupUi(self)
            self.setWindowIcon(QIcon('assists/favicon.ico'))
            self.ui_add.lineEdit.textChanged[str].connect(self.init)
            self.ui_add.pushButton.pressed.connect(self.set_fields)
            self.ui_add.pushButton_2.pressed.connect(self.query_fields)
            self.init()
        except Exception:
            print('Error: AddCRLWindow()::__init__()', 'errors')
            logs('Error: AddCRLWindow()::__init__()', 'errors')

    def init(self, text=''):
        try:
            self.ui_add.comboBox.clear()
            query = CERT.select().where(CERT.Registration_Number.contains(text)
                                        | CERT.Name.contains(text)
                                        | CERT.KeyId.contains(text)
                                        | CERT.Stamp.contains(text)
                                        | CERT.SerialNumber.contains(text)).limit(config['Listing']['cert'])
            for row in query:
                self.ui_add.comboBox.addItem(row.Name, row.KeyId)
        except Exception:
            print('Error: AddCRLWindow()::init()', 'errors')
            logs('Error: AddCRLWindow()::init()', 'errors')

    def set_fields(self):
        try:
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
        except Exception:
            print('Error: AddCRLWindow()::set_fields()', 'errors')
            logs('Error: AddCRLWindow()::set_fields()', 'errors')

    def query_fields(self):
        try:
            if WatchingCRL.select().where(WatchingCRL.Name == self.ui_add.lineEdit_6.text()
                                          or WatchingCRL.INN == self.ui_add.lineEdit_7.text()
                                          or WatchingCRL.OGRN == self.ui_add.lineEdit_2.text()
                                          or WatchingCRL.KeyId == self.ui_add.lineEdit_3.text()
                                          or WatchingCRL.Stamp == self.ui_add.lineEdit_8.text()
                                          or WatchingCRL.SerialNumber == self.ui_add.lineEdit_4.text()
                                          or WatchingCRL.UrlCRL == self.ui_add.lineEdit_9.text()).count() > 0:
                print('Info: CRL is exists in WatchingCRL')
                logs('Info: CRL is exists in WatchingCRL')
                self.ui_add.label_10.setText('CRL уже есть в основном списке отслеживания')
            elif WatchingCustomCRL.select().where(WatchingCustomCRL.Name == self.ui_add.lineEdit_6.text()
                                                  or WatchingCustomCRL.INN == self.ui_add.lineEdit_7.text()
                                                  or WatchingCustomCRL.OGRN == self.ui_add.lineEdit_2.text()
                                                  or WatchingCustomCRL.KeyId == self.ui_add.lineEdit_3.text()
                                                  or WatchingCustomCRL.Stamp == self.ui_add.lineEdit_8.text()
                                                  or WatchingCustomCRL.SerialNumber == self.ui_add.lineEdit_4.text()
                                                  or WatchingCustomCRL.UrlCRL == self.ui_add.lineEdit_9.text())\
                    .count() > 0:
                print('Info: CRL is exist in WatchingCustomCRL')
                logs('Info: CRL is exist in WatchingCustomCRL')
                self.ui_add.label_10.setText('CRL уже есть в своем списке отслеживания')
            elif WatchingDeletedCRL.select().where(WatchingDeletedCRL.Name == self.ui_add.lineEdit_6.text()
                                                   or WatchingDeletedCRL.INN == self.ui_add.lineEdit_7.text()
                                                   or WatchingDeletedCRL.OGRN == self.ui_add.lineEdit_2.text()
                                                   or WatchingDeletedCRL.KeyId == self.ui_add.lineEdit_3.text()
                                                   or WatchingDeletedCRL.Stamp == self.ui_add.lineEdit_8.text()
                                                   or WatchingDeletedCRL.SerialNumber == self.ui_add.lineEdit_4.text()
                                                   or WatchingDeletedCRL.UrlCRL == self.ui_add.lineEdit_9.text())\
                    .count() > 0:
                print('Info: CRL is exist in WatchingDeletedCRL')
                logs('Info: CRL is exist in WatchingDeletedCRL')
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
                    logs('Info: The fields should not be empty')
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
                    download_file(url_crl,
                                  key_id + '.crl',
                                  config['Folders']['crls'],
                                  'custome',
                                  str(query.ID),
                                  set_dd='Yes')
                    check_custom_crl(query.ID, name, key_id)
                    print('Info: CRL added in WatchingCustomCRL')
                    logs('Info: CRL added in WatchingCustomCRL')
                    self.ui_add.label_10.setText('CRL "' + name + '" добавлен в список отслеживания')
        except Exception:
            print('Error: AddCRLWindow()::query_fields()', 'errors')
            logs('Error: AddCRLWindow()::query_fields()', 'errors')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle(config['Style']['Window'])
    main_app = MainWindow()
    main_app.show()
    sys.exit(app.exec_())
