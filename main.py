from ui_main import *
from ui_sub_main import *
import shutil
import base64, sys, socket, sqlite3, os, configparser, math, OpenSSL, requests, datetime
from urllib import request, error
from os.path import expanduser
from PyQt5.QtWidgets import \
    QMainWindow, \
    QApplication, \
    QPushButton, \
    QWidget, \
    QTableWidgetItem, \
    QHeaderView, \
    QFileDialog
from PyQt5.QtGui import QIcon, QFont, QBrush, QColor
from PyQt5.QtCore import QCoreApplication, Qt, pyqtSignal, QThread, QRect, QSize
from lxml import etree
from peewee import *

config = configparser.ConfigParser()
if os.path.isfile('settings.ini'):
    config.read('settings.ini')
else:
    open('settings.ini', 'w').close()
    config['Folders'] = {'certs': 'certs/',
                         'crls': 'crls/',
                         'tmp': 'temp/',
                         'assests': 'assests/'}
    config['MainWindow'] = {'width': '1200',
                            'height': '400'}
    config['Bd'] = {'type': 'sqlite3',
                    'name': 'cert_crl.db'}
    config['Socket'] = {'timeout': '15'}
    config['Style'] = {'Window': 'Fusion'}
    with open('settings.ini', 'w') as configfile:
        config.write(configfile)

# socket.setdefaulttimeout(int(config['Socket']['timeout']))

# bd_backup_name = str('cert_crl.db_')+datetime.datetime.now().strftime('%Y%m%d%H%M%S')+'.bkp'
bd_backup_name = str('cert_crl.db_')+datetime.datetime.now().strftime('%Y%m%d')+'.bkp'
if os.path.isfile(bd_backup_name):
    print('Info: '+bd_backup_name+' exist')
else:
    try:
        shutil.copy2('cert_crl.db', bd_backup_name)
        print('Info: ' + bd_backup_name + ' created')
    except Exception:
        print('Error: cert_crl.db NOT FOUND')
try:
    connect = sqlite3.connect(config['Bd']['name'])
    db = SqliteDatabase(config['Bd']['name'])
except Exception:
    print('Error: Connect to BD failed')

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


def schedule(blocknum, blocksize, totalsize):
    QCoreApplication.processEvents()
    if totalsize == 0:
        percent = 0
    else:
        percent = blocknum * blocksize / totalsize
    if percent > 1.0:
        percent = 1.0
    percent = percent * 100
    print("\ndownload : %.2f%%" %(percent))
    progressbar(percent)


def get_info_xlm(type_data, xml_file='tsl.xml'):
    current_version = 'unknown'
    last_update = 'unknown'
    with open(xml_file, "rt", encoding="utf-8") as obj:
        xml = obj.read().encode()

    root = etree.fromstring(xml)
    for appt in root.getchildren():
        if appt.text:
            if appt.tag == 'Версия':
                current_version = appt.text
        if appt.text:
            if appt.tag == 'Дата':
                last_update = appt.text
    if type_data == 'current_version':
        return current_version
    if type_data == 'last_update':
        return last_update


def xml_parsing(xml_file, type_data):

    with open(xml_file, "rt", encoding="utf-8") as obj:
        xml = obj.read().encode()

    root = etree.fromstring(xml)
    uc_count = 0
    cert_count = 0
    crl_count = 0
    for appt in root.getchildren():
        for elem in appt.getchildren():
            if not elem.text:
                for sub_elem in elem.getchildren():
                    if not sub_elem.text:
                        for two_elem in sub_elem.getchildren():
                            if not two_elem.text:
                                for tree_elem in two_elem.getchildren():
                                    if not tree_elem.text:
                                        if tree_elem.tag == 'Ключ':
                                            for four_elem in tree_elem.getchildren():
                                                if not four_elem.text:
                                                    for five_elem in four_elem.getchildren():
                                                        if not five_elem.text:
                                                            for six_elem in five_elem.getchildren():
                                                                if not six_elem.text:
                                                                    six_text = "None"
                                                                else:
                                                                    if six_elem.tag == 'СерийныйНомер':
                                                                        cert_count = cert_count + 1
                                                        else:
                                                            if five_elem.tag == 'Адрес':
                                                                crl_count = crl_count + 1
                                                else:
                                                    four_text = four_elem.text
                                    else:
                                        tree_text = tree_elem.text
                            else:
                                two_text = two_elem.text
                    else:
                        sub_text = sub_elem.text
            else:
                text = elem.text
                if elem.tag == 'Название':
                    name = text
                if elem.tag == 'ИНН':
                    inn = text
                if elem.tag == 'ОГРН':
                    ogrn = text
                if elem.tag == 'РеестровыйНомер':
                    reesterNumber = text
                    uc_count = uc_count + 1

    if type_data == 'uc_count':
        return str(uc_count)
    if type_data == 'cert_count':
        return str(cert_count)
    if type_data == 'crl_count':
        return str(crl_count)


def parseXML(xmlFile):
    with open(xmlFile, "rt", encoding="utf-8") as obj:
        xml = obj.read().encode()

    root = etree.fromstring(xml)
    uc_count = 0
    cert_count = 0
    crl_count = 0
    for appt in root.getchildren():
        QCoreApplication.processEvents()
        AddresCode = ''
        AddresName = ''
        AddresIndex = ''
        AddresAddres = ''
        AddresStreet = ''
        AddresTown = ''
        Registration_Number = ''
        INN = ''
        OGRN = ''
        Full_Name = ''
        Email = ''
        Name = ''
        URL = ''
        keyIdent = ''
        stamp = ''
        cert_data = []
        if appt.text:
            if appt.tag == 'Версия':
                current_version = appt.text
        if appt.text:
            if appt.tag == 'Дата':
                last_update = appt.text
        print('------------------begin------------------')
        for elem in appt.getchildren():
            if not elem.text:
                print("   1<" + elem.tag + ">")
                for sub_elem in elem.getchildren():
                    if not sub_elem.text:
                        print("      2<" + sub_elem.tag + ">")
                        for two_elem in sub_elem.getchildren():
                            if not two_elem.text:
                                print("         3<" + two_elem.tag + ">")
                                for tree_elem in two_elem.getchildren():
                                    if not tree_elem.text:
                                        if tree_elem.tag == 'Ключ':
                                            print("            4<" + tree_elem.tag + ">")
                                            data_cert = {}
                                            adr_crl = []
                                            keyIdent = {}
                                            for four_elem in tree_elem.getchildren():
                                                if not four_elem.text:
                                                    print("               5<" + four_elem.tag + ">")
                                                    for five_elem in four_elem.getchildren():
                                                        if not five_elem.text:
                                                            print("                  6<" + five_elem.tag + ">")
                                                            for six_elem in five_elem.getchildren():
                                                                if not six_elem.text:
                                                                    six_text = "None"
                                                                else:
                                                                    if six_elem.tag == 'Отпечаток':
                                                                        stamp = six_elem.text
                                                                        #data_cert.append(six_elem.text)
                                                                        data_cert['stamp'] = six_elem.text
                                                                    if six_elem.tag == 'СерийныйНомер':
                                                                        cert_count = cert_count + 1
                                                                        data_cert['serrial'] = six_elem.text
                                                                        #data_cert.append(six_elem.text)
                                                                    if six_elem.tag == 'Данные':
                                                                        #with open("certs/"+stamp+".cer", "wb") as fh:
                                                                        #    fh.write(base64.decodebytes(six_elem.text.encode()))
                                                                        #data_cert.append(six_elem.text)
                                                                        data_cert['data'] = six_elem.text
                                                                    six_text = six_elem.text
                                                                    print("                     " + six_elem.tag + " => " + six_text)
                                                            print("                  </" + five_elem.tag + ">")
                                                        else:
                                                            if five_elem.tag == 'Адрес':
                                                                five_text = five_elem.text
                                                                adr_crl.append(five_text)
                                                                print("                  "+five_text)
                                                                file_name = five_text.split('/')[-1]
                                                                url = five_text
                                                                path = 'crls/' + stamp + '.crl'
                                                                #try:
                                                                #    request.urlretrieve(url, path, schedule)
                                                                #except error.HTTPError as e:
                                                                #    print(e)
                                                                #    print('\r\n' + url + ' download failed!' + '\r\n')
                                                                #except Exception:
                                                                #    print('\r\n' + url + ' download failed!' + '\r\n')
                                                                #else:
                                                                #    print('\r\n' + url + ' download successfully!')
                                                                #try:
                                                                #    urllib.request.urlretrieve(five_text, 'crls/' + file_name + '.crl')
                                                                #except Exception:
                                                                #    print('download error')
                                                                crl_count = crl_count + 1
                                                            print("                  " + five_elem.tag + " => " + five_text)
                                                    print("               </" + four_elem.tag + ">")
                                                else:
                                                    four_text = four_elem.text
                                                    if four_elem.tag == 'ИдентификаторКлюча':
                                                        keyIdent['keyid'] = four_text
                                                    print("               " + four_elem.tag + " => " + four_text)

                                            print("            </" + tree_elem.tag + ">")
                                            cert_data.append([keyIdent, data_cert, adr_crl])
                                        elif tree_elem.tag == 'Адрес':
                                            print("            4<" + tree_elem.tag + ">")
                                            for four_elem in tree_elem.getchildren():
                                                if not four_elem.text:
                                                    print("               5<" + four_elem.tag + ">")
                                                    for five_elem in four_elem.getchildren():
                                                        if not five_elem.text:
                                                            print("                  6<" + five_elem.tag + ">")
                                                            for six_elem in five_elem.getchildren():
                                                                if not six_elem.text:
                                                                    six_text = "None"
                                                                else:
                                                                    six_text = six_elem.text
                                                                    print("                     " + six_elem.tag + " => " + six_text)
                                                            print("                  </" + five_elem.tag + ">")
                                                        else:
                                                            print("                  " + five_elem.tag + " => " + five_text)
                                                    print("               </" + four_elem.tag + ">")
                                                else:
                                                    four_text = four_elem.text
                                                    print("               " + four_elem.tag + " => " + four_text)
                                            print("            </" + tree_elem.tag + ">")

                                    else:
                                        tree_text = tree_elem.text
                                        print("            " + tree_elem.tag + " => " + tree_text)
                                print("         </" + two_elem.tag + ">")
                            else:
                                two_text = two_elem.text
                                if two_elem.tag == 'Код':
                                    AddresCode = two_text
                                if two_elem.tag == 'Название':
                                    AddresName = two_text
                                print("         " + two_elem.tag + " => " + two_text)

                        print("      </" + sub_elem.tag + ">")
                    else:
                        sub_text = sub_elem.text
                        if sub_elem.tag == 'Индекс':
                            AddresIndex = sub_text
                        if sub_elem.tag == 'УлицаДом':
                            AddresStreet = sub_text
                        if sub_elem.tag == 'Город':
                            AddresTown = sub_text
                        if sub_elem.tag == 'Страна':
                            AddresAddres = sub_text
                        print("      " + sub_elem.tag + " => " + sub_text)
                print("   </" + elem.tag + ">")
            else:
                text = elem.text
                if elem.tag == 'Название':
                    Full_Name = text
                if elem.tag == 'ЭлектроннаяПочта':
                    Email = text
                if elem.tag == 'КраткоеНазвание':
                    Name = text
                if elem.tag == 'АдресСИнформациейПоУЦ':
                    URL = text
                if elem.tag == 'ИНН':
                    INN = text
                if elem.tag == 'ОГРН':
                    OGRN = text
                if elem.tag == 'РеестровыйНомер':
                    Registration_Number = text
                    uc_count = uc_count + 1
                print(elem.tag + " => " + text)
        print('------------------end------------------')
        '''
        print(''
              + ' Name:' + Name
              + ', Email:' + Email
              + ', Full_Name:' + Full_Name
              + ', URL:' + URL
              + ', AddresAddres:' + AddresAddres
              + ', AddresCode:' + AddresCode
              + ', AddresName:' + AddresName
              + ', AddresIndex:' + AddresIndex
              + ', AddresStreet:' + AddresStreet
              + ', AddresTown:' + AddresTown
              + ', INN:' + INN
              + ', OGRN:' + OGRN
              + ', Registration_Number:' + Registration_Number
              + ', certs:', cert_data)
        '''
        if Registration_Number != '':
            uc = UC(Registration_Number=Registration_Number,
                    INN=INN,
                    OGRN=OGRN,
                    Full_Name=Full_Name,
                    Email=Email,
                    Name=Name,
                    URL=URL,
                    AddresCode=AddresCode,
                    AddresName=AddresName,
                    AddresIndex=AddresIndex,
                    AddresAddres=AddresAddres,
                    AddresStreet=AddresStreet,
                    AddresTown=AddresTown)
            uc.save()
            # print(type(cert_data))
            for cert in cert_data:
                if type(cert_data) == list:
                    for data in cert:
                        if type(data) == dict:
                            for id, dats in data.items():
                                if id == 'keyid':
                                    KeyId = dats
                                    # print(dats)
                                if id == 'stamp':
                                    Stamp = dats
                                    # print(dats)
                                if id == 'serrial':
                                    SerialNumber = dats
                                    # print(dats)
                                if id == 'data':
                                    Data = dats
                                    # print(dats)

                        if type(data) == list:
                            for dats in data:
                                UrlCRL = dats
                                crl = CRL(Registration_Number=Registration_Number,
                                          KeyId=KeyId,
                                          Stamp=Stamp,
                                          SerialNumber=SerialNumber,
                                          UrlCRL=UrlCRL)
                                crl.save()
                cert = CERT(Registration_Number=Registration_Number,
                            KeyId=KeyId,
                            Stamp=Stamp,
                            SerialNumber=SerialNumber,
                            Data=Data)
                cert.save()

    print('Центров:' + str(uc_count))
    print('Сертов:' + str(cert_count))
    print('CRL:' + str(crl_count))


def save_cert(KeyId):
    for certs in CERT.select().where(CERT.KeyId == KeyId):
        with open(config['Folders']['certs']+"/" + certs.KeyId + ".cer", "wb") as file:
            file.write(base64.decodebytes(certs.Data.encode()))
    os.startfile(os.path.realpath(config['Folders']['certs']+"/"))


def open_file(file_name, file_type, url='None'):
    # open_file(sn + ".cer", "cer")
    # CryptExtAddCER «файл» Добавляет сертификат безопасности.
    # CryptExtAddCRL «файл» Добавляет список отзыва сертификатов.
    # CryptExtAddCTL «файл» Добавляет список доверия сертификатов.
    # CryptExtAddP7R «файл» Добавляет файл ответа на запрос сертификата.
    # CryptExtAddPFX «файл» Добавляет файл обмена личной информацией.
    # CryptExtAddSPC «файл» Добавляет сертификат PCKS #7.
    type = ""
    folder = ""
    if file_type == 'cer':          # CryptExtOpenCER «файл» Открывает сертификат безопасности.
        type = 'CryptExtOpenCER'
        folder = 'certs'
    elif file_type == 'crl':        # CryptExtOpenCRL «файл» Открывает список отзыва сертификатов.
        type = 'CryptExtOpenCRL'
        folder = 'crls'
    elif file_type == 'cat':        # CryptExtOpenCAT «файл» Открывает каталог безопасности.
        type = 'CryptExtOpenCAT'
        folder = 'cats'
    elif file_type == 'ctl':        # CryptExtOpenCTL «файл» Открывает список доверия сертификатов.
        type = 'CryptExtOpenCTL'
        folder = 'ctls'
    elif file_type == 'p10':        # CryptExtOpenP10 «файл» Открывает запрос на сертификат.
        type = 'CryptExtOpenP10'
        folder = 'p10s'
    elif file_type == 'p7r':        # CryptExtOpenP7R «файл» Открывает файл ответа на запрос сертификата.
        type = 'CryptExtOpenP7R'
        folder = 'p7rs'
    elif file_type == 'pkcs7':      # CryptExtOpenPKCS7 «файл» Открывает сертификат PCKS #7.
        type = 'CryptExtOpenPKCS7'
        folder = 'pkcs7s'
    elif file_type == 'str':        # CryptExtOpenSTR «файл» Открывает хранилище сериализированных сертификатов.
        type = 'CryptExtOpenSTR'
        folder = 'strs'

    run_dll = "%SystemRoot%\\System32\\rundll32.exe cryptext.dll,"+type
    path = os.path.realpath(config['Folders'][folder] + "/" + file_name + "." + file_type)
    print(path)
    if not os.path.exists(path):
        if file_type == 'cer':
            save_cert(file_name)
        elif file_type == 'crl':
            download_file(url, file_name, config['Folders']['crls'])
    else:
        open_crl = run_dll + "  " + path
        os.system(open_crl)


def check_custom_crl():
    try:
        query = WatchingCustomCRL.select() #.where(WatchingCustomCRL.status.contains('Info:')
                                           #      | WatchingCustomCRL.status.contains('Warning:'))
        for wcc in query:
            QCoreApplication.processEvents()
            issuer = {}
            print('----------------------------------------------------')
            try:
                # crl = OpenSSL.crypto.load_crl(OpenSSL.crypto.FILETYPE_ASN1,
                #                               open('crls/'+str(wcc.UrlCRL).split('/')[-1], 'rb').read())
                crl = OpenSSL.crypto.load_crl(OpenSSL.crypto.FILETYPE_ASN1,
                                              open('crls/'+str(wcc.KeyId)+'.crl', 'rb').read())
                # crl = OpenSSL.crypto.load_crl(OpenSSL.crypto.FILETYPE_ASN1, requests.get(str(wcc.UrlCRL)).content)
                crl_crypto = crl.get_issuer()
                cryptography = crl.to_cryptography()
                try:
                    for type, data in crl_crypto.get_components():
                        issuer[type.decode("utf-8")] = data.decode("utf-8")
                except Exception:
                    print('Error: get_components()')
                query_uc = UC.select().where(UC.OGRN == issuer['OGRN'], UC.INN == issuer['INN'])
                for uc_data in query_uc:
                    Name = uc_data.Name
                query_update = WatchingCustomCRL.update(INN=issuer['INN'],
                                                        OGRN=issuer['OGRN'],
                                                        status='Info: Filetype good',
                                                        last_update=cryptography.last_update,
                                                        next_update=cryptography.next_update).\
                    where(WatchingCustomCRL.ID == wcc.ID)
                query_update.execute()
                print(wcc.ID, Name, issuer['OGRN'], issuer['INN'], cryptography.last_update, cryptography.next_update)
                Name = 'Unknown'
                issuer['INN'] = 'Unknown'
                issuer['OGRN'] = 'Unknown'
            except Exception:
                query_update = WatchingCustomCRL.update(status='Warning: FILETYPE ERROR',
                                                        last_update='1970-01-01',
                                                        next_update='1970-01-01').where(WatchingCustomCRL.ID == wcc.ID)
                query_update.execute()
                print('Warning: FILETYPE ERROR')
    except Exception:
        print('Error: check_custom_data_crl()')


def check_crl():
    try:
        query = WatchingCRL.select() #.where(WatchingCustomCRL.download_status.contains('Info:')
                                     #      | WatchingCustomCRL.download_status.contains('Warning:'))
        for wc in query:
            QCoreApplication.processEvents()
            issuer = {}
            print('----------------------------------------------------')
            try:
                # crl = OpenSSL.crypto.load_crl(OpenSSL.crypto.FILETYPE_ASN1,
                #                               open('crls/'+str(wcc.UrlCRL).split('/')[-1], 'rb').read())
                crl = OpenSSL.crypto.load_crl(OpenSSL.crypto.FILETYPE_ASN1,
                                              open('crls/'+str(wc.KeyId)+'.crl', 'rb').read())
                # crl = OpenSSL.crypto.load_crl(OpenSSL.crypto.FILETYPE_ASN1, requests.get(str(wcc.UrlCRL)).content)
                cryptography = crl.to_cryptography()
                query_update = WatchingCRL.update(status='Info: Filetype good',
                                                  last_update=cryptography.last_update,
                                                  next_update=cryptography.next_update).where(WatchingCRL.ID == wc.ID)
                query_update.execute()
                print(wc.ID, wc.Name, wc.INN, wc.OGRN, cryptography.next_update)
            except Exception:
                query_update = WatchingCRL.update(status='Warning: FILETYPE ERROR',
                                                  last_update='1970-01-01',
                                                  next_update='1970-01-01').where(WatchingCRL.ID == wc.ID)
                query_update.execute()
                print('Warning: FILETYPE ERROR')
    except Exception:
        print('Error: check_data_crl()')


def check_for_import_in_uc():
    try:
        folder = config['Folders']['crls']
        current_datetime = datetime.datetime.now()
        before_current_datetime = datetime.datetime.now()-datetime.timedelta(days=5)
        last_date_copy = '2021-02-28 00:00:00'
        last_update = '2021-02-27 06:20:00'
        next_update = '2021-02-27 19:52:00'
        query_1 = WatchingCRL.select().where(
            WatchingCRL.last_update.between(before_current_datetime, current_datetime)
        )
        query_2 = WatchingCustomCRL.select().where(
            WatchingCustomCRL.last_update.between(before_current_datetime, current_datetime)
        )
        # datetime.datetime.strptime(last_date_copy, '%Y-%m-%d %H:%M:%S')
        for wc in query_1:
            if wc.last_download < wc.last_update:
                print('1 Copying', wc.Name, wc.last_update, wc.next_update)
            if wc.last_download > wc.next_update:
                print('1 Need to download', wc.Name, wc.last_update, wc.next_update)
                download_file(wc.UrlCRL, wc.KeyId+'.crl', folder, 'current', wc.ID)
        for wcc in query_2:
            if wcc.last_download< wcc.last_update:
                print('2 Copying', wcc.Name, wcc.last_update, wcc.next_update)
            if wcc.last_download > wcc.next_update:
                print('2 Need to download', wcc.Name, wcc.last_update, wcc.next_update)
                download_file(wcc.UrlCRL, wcc.KeyId+'.crl', folder, 'custome', wcc.ID)
        # TODO: Сделать проверку файлов и копирование
    except Exception:
        print('Error: check_for_import_in_uc()')


# TODO: Сделать функцию копирования файлов для УЦ


def download_file(file_url, file_name, folder, type='', w_id=''):
    try:
        file_name_url = file_url.split('/')[-1]
        type_file = file_name_url.split('.')[-1]
        path = folder + '/' + file_name # + '.' + type_file
        counter_failed_watching_crl = 0
        counter_failed_watching_custom_crl = 0
        try:
            request.urlretrieve(file_url, path, schedule)
        # except error.HTTPError as e:
        #     print(e)
        #     print('\r\n' + file_url + ' download failed!' + '\r\n')
        #     if type == 'current':
        #         counter_failed_watching_crl = counter_failed_watching_crl + 1
        #         query_update = WatchingCRL.update(status='Error: Download failed'
        #                                                 ).where(WatchingCRL.ID == w_id)
        #         query_update.execute()
        #     elif type == 'custome':
        #         counter_failed_watching_custom_crl = counter_failed_watching_custom_crl + 1
        #         query_update = WatchingCustomCRL.update(status='Error: Download failed'
        #                                                 ).where(WatchingCustomCRL.ID == w_id)
        #         query_update.execute()
        except Exception:
            print('\r\n' + file_url + ' download failed!' + '\r\n')

            if type == 'current':
                counter_failed_watching_crl = counter_failed_watching_crl + 1
                query_update = WatchingCRL.update(download_status='Error: Download failed',
                                                  last_download=datetime.datetime.now()
                                                  ).where(WatchingCRL.ID == w_id)
                query_update.execute()
            elif type == 'custome':
                counter_failed_watching_custom_crl = counter_failed_watching_custom_crl + 1
                query_update = WatchingCustomCRL.update(download_status='Error: Download failed',
                                                        last_download=datetime.datetime.now()
                                                        ).where(WatchingCustomCRL.ID == w_id)
                query_update.execute()
        else:
            print('\r\n' + file_url + ' download successfully!')
            if type == 'current':
                counter_failed_watching_crl = counter_failed_watching_crl + 1
                query_update = WatchingCRL.update(download_status='Info: Download successfully',
                                                  last_download=datetime.datetime.now()
                                                  ).where(WatchingCRL.ID == w_id)
                query_update.execute()
            elif type == 'custome':
                counter_failed_watching_custom_crl = counter_failed_watching_custom_crl + 1
                query_update = WatchingCustomCRL.update(download_status='Info: Download successfully',
                                                        last_download=datetime.datetime.now()
                                                        ).where(WatchingCustomCRL.ID == w_id)
                query_update.execute()
            # os.startfile(os.path.realpath(config['Folders']['crls'] + "/"))
        print('cc' + str(counter_failed_watching_crl) + ' ccw' + str(counter_failed_watching_custom_crl))
    except Exception:
        print('Error: download_file()')


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


class Downloader(QThread):
    try:
        preprogress = pyqtSignal(int)
        progress = pyqtSignal(int)
        done = pyqtSignal(str)
        downloading = pyqtSignal(str)

        def __init__(self, fileUrl, fileName):
            QThread.__init__(self)
            # Флаг инициализации
            self._init = False
            self.fileUrl = fileUrl
            self.fileName = fileName
            print(fileUrl)
            print(fileName)
            # site = request.urlopen(fileUrl)
            # meta = site.info()
            # print(meta)

        def run(self):
            # тест на локальных данных, но работать должно и с сетью
            # request.urlretrieve(self.fileUrl, self.fileName, self._progress)
            try:
                request.urlretrieve(self.fileUrl, self.fileName, self._progress)
            except error.HTTPError as e:
                print(e)
                self.done.emit('Ошибка загрузки')
            except Exception:
                self.done.emit('Ошибка загрузки')
            else:
                print('Загрузка завершена')

                #self.done.emit('Загрузка завершена')
                query_get_settings = Settings.select()
                ver_from_tsl = get_info_xlm('current_version')
                st = {}

                for setings in query_get_settings:
                    ver = setings.value
                    break
                if int(ver) == int(ver_from_tsl):
                    print('Info: update not need')
                    self.done.emit('Загрузка завершена, обновление не требуется')
                else:
                    print('Info: Need update')
                    self.done.emit('Загрузка завершена, требуются обновления Базы УЦ и сертификатов. Новая версия '
                                   +ver_from_tsl+' текущая версия '+ver)

                # get_info_xlm('last_update')
                size_tls = os.path.getsize("tsl.xml")
                self.preprogress.emit(size_tls)
                self.progress.emit(size_tls)

        def _progress(self, block_num, block_size, total_size, ccc=0):
            total_size = int('15000000')
            print(block_num, block_size, total_size)
            self.downloading.emit('Загрузка.')
            if not self._init:
                self.preprogress.emit(total_size)
                self._init = True
                # self.button_init.setEnabled(False)
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


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('assests/favicon.ico'))
        self.window_uc = None
        self.tab_info()
        self.tab_uc()
        self.tab_cert()
        self.tab_crl()
        self.tab_watching_crl()
        self.sub_tab_watching_crl()
        self.sub_tab_watching_custom_crl()
        self.sub_tab_watching_off_crl()

    # TODO: Need fix loop bug

    def tab_info(self):
        try:
            ucs = UC.select()
            certs = CERT.select()
            crls = CRL.select()
            watching_crl = WatchingCRL.select()
            watching_cusom_crl = WatchingCustomCRL.select()
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
                                          +int(watching_cusom_crl.count())))
            self.ui.pushButton.clicked.connect(self.download_xml)
            self.ui.pushButton_2.clicked.connect(self.init_xml)
            self.ui.pushButton_13.clicked.connect(self.export_crl)
            watching_crl = WatchingCRL.select().order_by(WatchingCRL.next_update).where(WatchingCRL.OGRN == '1047702026701')
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

            watching_crl = WatchingCRL.select().order_by(WatchingCRL.next_update).where(WatchingCRL.OGRN == '1020203227263')
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


        except Exception:
            print('Error: tab_info()')

    def tab_uc(self, text=''):
        try:
            # self.ui.label_8.setText('Ищем: ' + text)
            # self.ui.label_8.adjustSize()
            self.ui.lineEdit.textChanged[str].connect(self.tab_uc)

            query = UC.select().where(UC.Registration_Number.contains(text)
                                      | UC.INN.contains(text)
                                      | UC.OGRN.contains(text)
                                      | UC.Full_Name.contains(text)).limit(config['Listing']['uc'])
            count_all = UC.select().where(UC.Registration_Number.contains(text)
                                          | UC.INN.contains(text)
                                          | UC.OGRN.contains(text)
                                          | UC.Full_Name.contains(text)).limit(config['Listing']['uc']).count()
            self.ui.tableWidget.setRowCount(count_all)
            count = 0

            for row in query:
                self.ui.tableWidget.setItem(count, 0, QTableWidgetItem(str(row.Registration_Number)))
                self.ui.tableWidget.setItem(count, 1, QTableWidgetItem(str(row.INN)))
                self.ui.tableWidget.setItem(count, 2, QTableWidgetItem(str(row.OGRN)))
                self.ui.tableWidget.setItem(count, 3, QTableWidgetItem(str(row.Full_Name)))
                buttonInfo = QPushButton()
                buttonInfo.setFixedSize(100, 30)
                buttonInfo.setText("Подробнее")
                regnum = row.Registration_Number
                buttonInfo.pressed.connect(lambda rg=regnum: self.open_sub_window_info_uc(rg))
                self.ui.tableWidget.setCellWidget(count, 4, buttonInfo)
                count = count + 1
            self.ui.tableWidget.resizeColumnsToContents()
            self.ui.tableWidget.horizontalHeader().setSectionResizeMode(3, QHeaderView.Stretch)
        except Exception:
            print('Error: tab_uc()')

    def tab_cert(self, text=''):
        try:
            # self.lableFindCert.setText('Ищем: ' + text)
            # self.lableFindCert.adjustSize()
            self.ui.lineEdit_2.textChanged[str].connect(self.tab_cert)

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

                self.buttonSert = QPushButton()
                self.buttonSert.setFixedSize(150, 30)
                self.buttonSert.setText("Просмотр сертификата")
                ki = row.KeyId
                self.buttonSert.pressed.connect(lambda key_id=ki: open_file(key_id, "cer"))
                self.ui.tableWidget_2.setCellWidget(count, 5, self.buttonSert)

                buttonSertSave = QPushButton()
                buttonSertSave.setFixedSize(100, 30)
                buttonSertSave.setText("Сохранить")
                ki = row.KeyId
                buttonSertSave.pressed.connect(lambda key_id=ki: save_cert(key_id))
                self.ui.tableWidget_2.setCellWidget(count, 6, buttonSertSave)
                count = count + 1
            self.ui.tableWidget_2.resizeColumnToContents(0)
            self.ui.tableWidget_2.setColumnWidth(1, 150)
            self.ui.tableWidget_2.setColumnWidth(2, 150)
            self.ui.tableWidget_2.setColumnWidth(3, 150)
            self.ui.tableWidget_2.horizontalHeader().setSectionResizeMode(4, QHeaderView.Stretch)
            self.ui.tableWidget_2.resizeColumnToContents(5)
        except Exception:
            print('Error: tab_cert()')

    def tab_crl(self, text=''):
        try:
            # self.lableFindCRL.setText('Ищем: ' + text)
            # self.lableFindCRL.adjustSize()
            self.ui.lineEdit_3.textChanged[str].connect(self.tab_crl)

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
                buttonCRLSave = QPushButton()
                buttonCRLSave.setFixedSize(100, 30)
                buttonCRLSave.setText("Скачать")
                stamp = row.Stamp
                url = row.UrlCRL
                buttonCRLSave.pressed.connect(lambda u=url, s=stamp: download_file(u, s, config['Folders']['crls']))
                self.ui.tableWidget_3.setCellWidget(count, 6, buttonCRLSave)

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

    def tab_watching_crl(self):
        self.ui.pushButton_4.pressed.connect(self.download_all_crls)
        self.ui.pushButton_5.clicked.connect(self.check_all_crl)
        self.ui.pushButton_3.clicked.connect(check_for_import_in_uc)
        self.ui.pushButton_6.pressed.connect(self.import_crl_list)

    def sub_tab_watching_crl(self, text=''):
        try:
            self.ui.label_8.setText('Ищем: ' + text)
            self.ui.label_8.adjustSize()
            self.ui.lineEdit_4.textChanged[str].connect(self.sub_tab_watching_crl)

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

                buttonDeleteWatch = QPushButton()
                buttonDeleteWatch.setFixedSize(100, 30)
                buttonDeleteWatch.setText("Убрать")
                id = row.ID
                buttonDeleteWatch.pressed.connect(lambda o=id: self.move_watching_to_delete(o, 'current'))
                self.ui.tableWidget_4.setCellWidget(count, 8, buttonDeleteWatch)
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

    def sub_tab_watching_custom_crl(self, text=''):
        try:
            self.ui.label_8.setText('Ищем: ' + text)
            self.ui.label_8.adjustSize()
            self.ui.lineEdit_5.textChanged[str].connect(self.sub_tab_watching_custom_crl)
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

                buttonDeleteWatch = QPushButton()
                buttonDeleteWatch.setFixedSize(100, 30)
                buttonDeleteWatch.setText("Убрать")
                # id = row.ID
                # buttonDeleteWatch.pressed.connect(lambda i=id: self.delete_watching(i))
                self.ui.tableWidget_5.setCellWidget(count, 8, buttonDeleteWatch)

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

    def sub_tab_watching_off_crl(self, text=''):
        try:
            self.ui.label_8.setText('Ищем: ' + text)
            self.ui.label_8.adjustSize()
            self.ui.lineEdit_6.textChanged[str].connect(self.sub_tab_watching_off_crl)
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

    def tab_settings(self):
        try:
            self.pushButton_4.clicked.connect(lambda: self.choose_directory('crl'))
            self.pushButton_5.clicked.connect(lambda: self.choose_directory('cert'))
            self.pushButton_3.clicked.connect(lambda: self.choose_directory('uc'))
        except Exception:
            print('Error: tab_settings()')

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

    def choose_directory(self, type):
        try:
            input_dir = QFileDialog.getExistingDirectory(None, 'Выбор директории:', expanduser("~"))
            if type == 'crl':
                self.label_9.setText('  Папка с CRL: '+input_dir)
            if type == 'cert':
                self.label_10.setText('  Папка с сертификатами: '+input_dir)
            if type == 'uc':
                self.label_11.setText('  Папка для УЦ: '+input_dir)
        except Exception:
            print('Error: choose_directory()')

    def download_xml(self):
        try:
            self.ui.label_7.setText('Скачиваем список.')
            self.ui.label_7.adjustSize()
            self.ui.pushButton.setEnabled(False)
            self.ui.pushButton_2.setEnabled(False)
            self._download = Downloader('https://e-trust.gosuslugi.ru/CA/DownloadTSL?schemaVersion=0', 'tsl.xml')
            # Устанавливаем максимальный размер данных
            self._download.preprogress.connect(lambda x: self.ui.progressBar.setMaximum(x))
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

    def check_all_crl(self):
        try:
            self.ui.label_8.setText('Проверяем основной список CRL')
            check_crl()
            self.ui.label_8.setText('Проверяем свой список CRL')
            check_custom_crl()
            self.ui.label_8.setText('Готово')
            # self.textBrowser.setText(open('main.log', 'rb').read().decode())
        except Exception:
            print('Error: check_all_crl()')

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
            with open('tsl.xml', "rt", encoding="utf-8") as obj:
                xml = obj.read().encode()

            root = etree.fromstring(xml)
            uc_count = 0
            cert_count = 0
            crl_count = 0

            uc_count_all = 505
            cert_count_all = 2338
            crl_count_all = 3267
            current_version = 'Unknown'
            last_update = 'Unknown'
            for appt in root.getchildren():
                QCoreApplication.processEvents()
                AddresCode = ''
                AddresName = ''
                AddresIndex = ''
                AddresAddres = ''
                AddresStreet = ''
                AddresTown = ''
                Registration_Number = ''
                INN = ''
                OGRN = ''
                Full_Name = ''
                Email = ''
                Name = ''
                URL = ''
                keyIdent = ''
                stamp = ''
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
                                                    keyIdent = {}
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
                                                                keyIdent['keyid'] = four_text
                                                    cert_data.append([keyIdent, data_cert, adr_crl])
                                    else:
                                        two_text = two_elem.text
                                        if two_elem.tag == 'Код':
                                            AddresCode = two_text
                                        if two_elem.tag == 'Название':
                                            AddresName = two_text
                            else:
                                sub_text = sub_elem.text
                                if sub_elem.tag == 'Индекс':
                                    AddresIndex = sub_text
                                if sub_elem.tag == 'УлицаДом':
                                    AddresStreet = sub_text
                                if sub_elem.tag == 'Город':
                                    AddresTown = sub_text
                                if sub_elem.tag == 'Страна':
                                    AddresAddres = sub_text
                    else:
                        text = elem.text
                        if elem.tag == 'Название':
                            Full_Name = text
                        if elem.tag == 'ЭлектроннаяПочта':
                            Email = text
                        if elem.tag == 'КраткоеНазвание':
                            Name = text
                        if elem.tag == 'АдресСИнформациейПоУЦ':
                            URL = text
                        if elem.tag == 'ИНН':
                            INN = text
                        if elem.tag == 'ОГРН':
                            OGRN = text
                        if elem.tag == 'РеестровыйНомер':
                            Registration_Number = text
                            uc_count = uc_count + 1
                if Registration_Number != '':
                    self.ui.label_7.setText('Обрабатываем данные:\n УЦ: ' + Name)
                    uc = UC(Registration_Number=Registration_Number,
                            INN=INN,
                            OGRN=OGRN,
                            Full_Name=Full_Name,
                            Email=Email,
                            Name=Name,
                            URL=URL,
                            AddresCode=AddresCode,
                            AddresName=AddresName,
                            AddresIndex=AddresIndex,
                            AddresAddres=AddresAddres,
                            AddresStreet=AddresStreet,
                            AddresTown=AddresTown)
                    uc.save()
                    for cert in cert_data:
                        if type(cert_data) == list:
                            for data in cert:
                                if type(data) == dict:
                                    for id, dats in data.items():
                                        if id == 'keyid':
                                            KeyId = dats
                                        if id == 'stamp':
                                            Stamp = dats
                                        if id == 'serrial':
                                            SerialNumber = dats
                                        if id == 'data':
                                            Data = dats

                                if type(data) == list:
                                    for dats in data:
                                        UrlCRL = dats
                                        crl = CRL(Registration_Number=Registration_Number,
                                                  Name=Name,
                                                  KeyId=KeyId,
                                                  Stamp=Stamp,
                                                  SerialNumber=SerialNumber,
                                                  UrlCRL=UrlCRL)
                                        crl.save()
                        cert = CERT(Registration_Number=Registration_Number,
                                    Name=Name,
                                    KeyId=KeyId,
                                    Stamp=Stamp,
                                    SerialNumber=SerialNumber,
                                    Data=Data)
                        cert.save()

                        uc_percent_step = int(math.floor(100 / (uc_count_all / uc_count)))
                        cert_percent_step = int(math.floor(100 / (cert_count_all / cert_count)))
                        crl_percent_step = int(math.floor(100 / (crl_count_all / crl_count)))
                        self.ui.progressBar_2.setValue(crl_percent_step)
            # print('Центров:' + str(uc_count))
            # print('Сертов:' + str(cert_count))
            # print('CRL:' + str(crl_count))
            # current_version
            # last_update
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
        except Exception:
            print('Error: init_xml()')

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
                # self.counter_added_exist = self.counter_added_exist + 1
            # self.on_changed_find_watching_crl('')
        except Exception:
            print('Error: add_watch_cert_crl()')

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
                self.counter_added_exist = self.counter_added_exist + 1
            self.on_changed_find_watching_crl('')
        except Exception:
            print('Error: add_watch_custom_cert_crl()')

    def move_watching_to_delete(self, id, froms):
        try:
            if froms == 'current':
                from_bd = WatchingCRL.select().where(WatchingCRL.ID == id)
                for row in from_bd:
                    to_bd = WatchingDeletedCRL(Name=row.Name,
                                               INN=row.INN,
                                               OGRN=row.OGRN,
                                               KeyId=row.KeyId,
                                               Stamp=row.Stamp,
                                               SerialNumber=row.SerialNumber,
                                               UrlCRL=row.UrlCRL)
                    to_bd.save()
                WatchingCRL.delete_by_id(id)
                self.on_changed_find_watching_crl()
                self.on_changed_find_deleted_watching_crl()
            elif froms == 'custom':
                WatchingCustomCRL.delete_by_id(id)
                self.on_changed_find_deleted_watching_crl('')
            else:
                print('Error: Ошибка перемещения')
        except Exception:
            print('Error: move_watching_to_delete()')

    # def delete_watching(self, id):
    #     WatchingCRL.delete_by_id(id)
    #     self.on_changed_find_watching_crl('')
    #     print(id + ' id is deleted')

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
                            self.add_watch_cert_crl(row.Registration_Number, row.KeyId, row.Stamp, row.SerialNumber, row.UrlCRL)
                    else:
                        print('add to custom')
                        self.add_watch_custom_cert_crl(crl_url)
                    # self.on_changed_find_watching_crl('')
                print(self.counter_added, self.counter_added_custom, self.counter_added_exist)
            else:
                print('Not found crl_list.txt')
        except Exception:
            print('Error: import_crl_list()')

    def download_all_crls(self):
        try:
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
                file_name = wc.KeyId+'.crl'
                # file_name = wc.UrlCRL.split('/')[-1]
                # file_name = wcc.KeyId
                folder = config['Folders']['crls']
                self.ui.label_8.setText(str(counter_watching_crl) + ' из '+ str(counter_watching_crl_all) + ' Загружаем: ' + str(wc.Name) + ' ' + str(wc.KeyId))
                download_file(file_url, file_name, folder, 'current', wc.ID)
                # Downloader(str(wc.UrlCRL), str(wc.SerialNumber)+'.crl')
            print('WatchingCRL downloaded ' + str(counter_watching_crl))
            for wcc in query_2:
                QCoreApplication.processEvents()
                counter_watching_custom_crl = counter_watching_custom_crl + 1
                file_url = wcc.UrlCRL
                file_name = wcc.KeyId+'.crl'
                # file_name = wcc.UrlCRL.split('/')[-1]
                # file_name = wcc.KeyId
                folder = config['Folders']['crls']
                self.ui.label_8.setText(str(counter_watching_custom_crl) + ' из '+ str(watching_custom_crl_all) + ' Загружаем: ' + str(wcc.Name) + ' ' + str(wcc.KeyId))
                download_file(file_url, file_name, folder, 'custome', wcc.ID)
                # Downloader(str(wcc.UrlCRL), str(wcc.SerialNumber)+'.crl'
            self.ui.label_8.setText('Загрузка закончена')
            print('WatchingCustomCRL downloaded '+ str(counter_watching_custom_crl))
            print('All download done, w='+str(counter_watching_crl)+', c='+str(counter_watching_custom_crl))
        except Exception:
            print('Error: download_all_crls()')

    def export_crl(self):
        self.ui.label_7.setText('Генерируем файл')
        export_all_watching_crl()
        self.ui.label_7.setText('Файл сгенерирован')


class UcWindow(QWidget):
    def __init__(self, RegNumber):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.init(RegNumber)

    def init(self, RegNumber):
        try:
            Registration_Number = 'Unknown'
            INN = 'Unknown'
            OGRN = 'Unknown'
            Full_Name = 'Unknown'
            Email = 'Unknown'
            Name = 'Unknown'
            URL = 'Unknown'
            AddresCode = 'Unknown'
            AddresName = 'Unknown'
            AddresIndex = 'Unknown'
            AddresAddres = 'Unknown'
            AddresStreet = 'Unknown'
            AddresTown = 'Unknown'
            query = UC.select().where(UC.Registration_Number == RegNumber)
            for row in query:
                Registration_Number = 'Регистрационный номер: '+str(row.Registration_Number)
                INN = 'ИНН: '+str(row.INN)
                OGRN = 'ОГРН: '+str(row.OGRN)
                Full_Name = 'Полное название организации: '+str(row.Full_Name)
                Email = 'Электронная почта: '+str(row.Email)
                Name = 'Название организации: '+str(row.Name)
                URL = 'Интернет адрес: '+str(row.URL)
                AddresCode = 'Код региона: '+str(row.AddresCode)
                AddresName = 'Регион: '+str(row.AddresName)
                AddresIndex = 'Почтовый индекс: '+str(row.AddresIndex)
                AddresAddres = 'Код страны: '+str(row.AddresAddres)
                AddresStreet = 'Улица: '+str(row.AddresStreet)
                AddresTown = 'Город : '+str(row.AddresTown)

            self.setWindowTitle(Name)
            self.setWindowIcon(QIcon('assests/favicon.ico'))

            self.ui.label_7.setText(Registration_Number)
            self.ui.label_6.setText(INN)
            self.ui.label_5.setText(OGRN)
            self.ui.label_4.setText(Full_Name)
            self.ui.label_3.setText(Email)
            self.ui.label_2.setText(URL)
            self.ui.label.setText(Name)

            self.ui.label_13.setText(AddresCode)
            self.ui.label_12.setText(AddresName)
            self.ui.label_11.setText(AddresIndex)
            self.ui.label_10.setText(AddresAddres)
            self.ui.label_8.setText(AddresStreet)
            self.ui.label_9.setText(AddresTown)
            Registration_Number = 'Unknown'
            KeyId = 'Unknown'
            Stamp = 'Unknown'
            SerialNumber = 'Unknown'
            UrlCRL = 'Unknown'

            query = CRL.select().where(CRL.Registration_Number == RegNumber)
            query_count = CRL.select().where(CRL.Registration_Number == RegNumber).count()
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
        except Exception:
            print('Error: UcWindow()::init()')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle(config['Style']['Window'])
    main_app = MainWindow()
    main_app.show()
    sys.exit(app.exec_())
