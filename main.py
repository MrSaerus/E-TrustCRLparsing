# PyQt5, lxml, peewee, ebcdic, OpenSSL
import base64, sys, socket, sqlite3, os, configparser, math
from urllib import request, error
from os.path import expanduser
from PyQt5.QtWidgets import \
    QMainWindow, \
    QProgressBar, \
    QApplication, \
    QPushButton, \
    QWidget, \
    QTabWidget, \
    QVBoxLayout, \
    QHBoxLayout, \
    QLabel, \
    QTableWidgetItem, \
    QTableWidget, \
    QFrame, \
    QSplitter, \
    QLineEdit, \
    QHeaderView, \
    QSizePolicy, \
    QFileDialog

from PyQt5.QtGui import QIcon, QFont
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
connect = sqlite3.connect(config['Bd']['name'])
db = SqliteDatabase(config['Bd']['name'])

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
    if totalsize == 0:
        percent = 0
    else:
        percent = blocknum * blocksize / totalsize
    if percent > 1.0:
        percent = 1.0
    percent = percent * 100
    print("\ndownload : %.2f%%" %(percent))
    progressbar(percent)


def get_info_xlm(xml_file, type_data):
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


def save_cert(seriall_number):
    for certs in CERT.select().where(CERT.SerialNumber == seriall_number):
        with open(config['Folders']['certs']+"/" + certs.SerialNumber + ".cer", "wb") as file:
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
    # CryptExtOpenCAT «файл» Открывает каталог безопасности.
    # CryptExtOpenCER «файл» Открывает сертификат безопасности.
    # CryptExtOpenCRL «файл» Открывает список отзыва сертификатов.
    # CryptExtOpenCTL «файл» Открывает список доверия сертификатов.
    # CryptExtOpenP10 «файл» Открывает запрос на сертификат.
    # CryptExtOpenP7R «файл» Открывает файл ответа на запрос сертификата.
    # CryptExtOpenPKCS7 «файл» Открывает сертификат PCKS #7.
    # CryptExtOpenSTR «файл» Открывает хранилище сериализированных сертификатов.

    type = ""
    folder = ""
    if file_type == 'cer':
        type = 'CryptExtOpenCER'
        folder = 'certs'
    elif file_type == 'crl':
        type = 'CryptExtOpenCRL'
        folder = 'crls'
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


def download_file(file_url, file_name, folder):
    file_name_url = file_url.split('/')[-1]
    type_file = file_name_url.split('.')[-1]
    path = folder + '/' + file_name + '.' + type_file
    try:
       request.urlretrieve(file_url, path, schedule)
    except error.HTTPError as e:
       print(e)
       print('\r\n' + file_url + ' download failed!' + '\r\n')
    except Exception:
       print('\r\n' + file_url + ' download failed!' + '\r\n')
    else:
       print('\r\n' + file_url + ' download successfully!')
       os.startfile(os.path.realpath(config['Folders']['crls'] + "/"))


class Downloader(QThread):
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
            self.done.emit('Загрузка завершена')
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


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'E-Trust CRL Parsing v1.0.0-5'
        self.left = 0
        self.top = 0
        self.counter_added = 0
        self.counter_added_exist = 0
        self.counter_added_custom = 0
        self.width = int(config['MainWindow']['width'])
        self.height = int(config['MainWindow']['height'])
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon('assests/favicon.ico'))
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.tab_widget = TabWidget(self)
        self.setCentralWidget(self.tab_widget)

        self.show()


class TabWidget(QWidget):
    def __init__(self, parent):
        super(TabWidget, self).__init__(parent)
        self.window_uc = None
        self.layout = QVBoxLayout(self)

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab0 = QWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()

        # Add tabs
        self.tabs.addTab(self.tab0, "Инициализация")
        self.tabs.addTab(self.tab1, "Список УЦ")
        self.tabs.addTab(self.tab2, "Список Сертификатов")
        self.tabs.addTab(self.tab3, "Список CRL")
        self.tabs.addTab(self.tab4, "Скачиваемые УЦ")
        self.tabs.addTab(self.tab5, "Настройки")

        self.tab_info()
        self.tab_uc()
        self.tab_cert()
        self.tab_crl()
        self.tab_watching_crl()
        self.tab_settings()

    def tab_info(self):
        ucs = UC.select()
        certs = CERT.select()
        crls = CRL.select()
        watching_crl = WatchingCRL.select()
        settings_ver = '0'
        settings_update_date = '0'
        query = Settings.select()
        for data in query:
            if data.name == 'ver':
                settings_ver = data.value
            if data.name == 'data_update':
                settings_update_date = data.value

        self.verticalLayout_3 = QVBoxLayout()
        self.horizontalLayout = QHBoxLayout()
        self.frame_2 = QFrame()
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setLineWidth(0)
        self.verticalLayoutWidget_5 = QWidget(self.frame_2)
        self.verticalLayoutWidget_5.setGeometry(QRect(0, 0, 381, 151))
        self.verticalLayout_16 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_16.setSpacing(5)
        self.verticalLayout_16.setContentsMargins(10, 10, 10, 10)
        self.lable_1 = QLabel("Начальная инициализация сертификатов и списка отзыва")
        self.verticalLayout_16.addWidget(self.lable_1)
        self.lable_2 = QLabel(" Версия базы: " + settings_ver)
        self.verticalLayout_16.addWidget(self.lable_2)
        self.lable_3 = QLabel(" Дата выпуска базы: " + settings_update_date)
        self.verticalLayout_16.addWidget(self.lable_3)
        self.lable_5 = QLabel(" Всего УЦ: " + str(ucs.count()))
        self.verticalLayout_16.addWidget(self.lable_5)
        self.lable_6 = QLabel(" Всего Сертификатов: " + str(certs.count()))
        self.verticalLayout_16.addWidget(self.lable_6)
        self.lable_7 = QLabel(" Всего CRL: " + str(crls.count()))
        self.verticalLayout_16.addWidget(self.lable_7)
        self.lable_8 = QLabel(" CRL будет загружено: " + str(watching_crl.count()))
        self.verticalLayout_16.addWidget(self.lable_8)

        self.horizontalLayout.addWidget(self.frame_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_29 = QVBoxLayout()
        self.frame_3 = QFrame()
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_3)
        self.verticalLayout_30 = QVBoxLayout()
        self.currentTread = QLabel()
        self.verticalLayout_30.addWidget(self.currentTread)
        self.horizontalLayout_7.addLayout(self.verticalLayout_30)
        self.verticalLayout_29.addWidget(self.frame_3)
        self.verticalLayout_5.addLayout(self.verticalLayout_29)
        self.frame = QFrame()
        self.frame.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setStyleSheet(u";\n""border-color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.verticalLayout_4 = QVBoxLayout()
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setMinimumSize(QSize(200, 30))
        self.pushButton.setBaseSize(QSize(0, 0))
        self.pushButton.setText("Загрузить TSL")
        self.pushButton.clicked.connect(self.download_xml)
        self.verticalLayout_4.addWidget(self.pushButton)
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setMinimumSize(QSize(200, 30))
        self.pushButton_2.setText("Обработать TSL")
        self.pushButton_2.clicked.connect(self.init_xml)
        self.verticalLayout_4.addWidget(self.pushButton_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_2 = QVBoxLayout()
        self.progressBar = QProgressBar(self.frame)
        self.progressBar.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet(u"background-color: rgb(218, 218, 218);")
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QProgressBar.TopToBottom)
        self.verticalLayout_2.addWidget(self.progressBar, 0, Qt.AlignBottom)
        self.progressBar_2 = QProgressBar(self.frame)
        self.progressBar_2.setMinimumSize(QSize(0, 30))
        font1 = QFont()
        font1.setKerning(False)
        self.progressBar_2.setFont(font1)
        self.progressBar_2.setMouseTracking(False)
        self.progressBar_2.setStyleSheet(u"background-color: rgb(218, 218, 218);")
        self.progressBar_2.setAlignment(Qt.AlignCenter)
        self.progressBar_2.setTextVisible(True)
        self.progressBar_2.setOrientation(Qt.Horizontal)
        self.progressBar_2.setInvertedAppearance(False)
        self.progressBar_2.setTextDirection(QProgressBar.TopToBottom)
        self.verticalLayout_2.addWidget(self.progressBar_2, 0, Qt.AlignBottom)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_5.addWidget(self.frame, 0, Qt.AlignBottom)
        self.verticalLayout_3.addLayout(self.verticalLayout_5)
        self.tab0.setLayout(self.verticalLayout_3)

    def tab_uc(self):
        ucs = UC.select()
        self.tab1.layout = QVBoxLayout(self)

        self.qline = QLineEdit(self)
        self.qline.setMaximumWidth(300)
        self.qline.textChanged[str].connect(self.on_changed_find_uc)
        self.tab1.layout.addWidget(self.qline)

        self.lableFindUC = QLabel(self)
        self.tab1.layout.addWidget(self.lableFindUC)

        self.tableWidget = QTableWidget(self)
        self.tableWidget.setRowCount(int(ucs.count()))
        self.tableWidget.setColumnCount(5)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setHorizontalHeaderLabels(["Р/Н",
                                                    "ИНН",
                                                    "ОГРН",
                                                    "Название",
                                                    ""])
        self.on_changed_find_uc('')
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.horizontalHeader().setSectionResizeMode(3, QHeaderView.Stretch)
        self.tab1.layout.addWidget(self.tableWidget)
        self.tab1.setLayout(self.tab1.layout)

    def tab_cert(self):
        certs = CERT.select()
        self.tab2.layout = QVBoxLayout(self)

        self.zline = QLineEdit(self)
        self.zline.setMaximumWidth(300)
        self.zline.textChanged[str].connect(self.on_changed_find_cert)
        self.tab2.layout.addWidget(self.zline)

        self.lableFindCert = QLabel(self)
        self.tab2.layout.addWidget(self.lableFindCert)

        self.tableWidgetCert = QTableWidget(self)
        self.tableWidgetCert.setRowCount(int(certs.count()))
        self.tableWidgetCert.setColumnCount(7)
        self.tableWidgetCert.verticalHeader().setVisible(False)
        self.tableWidgetCert.setHorizontalHeaderLabels(["Р/Н",
                                                    "Название",
                                                    "Идентификатор ключа",
                                                    "Отпечаток",
                                                    "Серийный номер",
                                                    "",
                                                    ""])
        self.on_changed_find_cert('')
        self.tableWidgetCert.resizeColumnToContents(0)
        self.tableWidgetCert.setColumnWidth(1, 150)
        self.tableWidgetCert.setColumnWidth(2, 150)
        self.tableWidgetCert.setColumnWidth(3, 150)
        self.tableWidgetCert.horizontalHeader().setSectionResizeMode(4, QHeaderView.Stretch)
        self.tableWidgetCert.resizeColumnToContents(5)
        self.tab2.layout.addWidget(self.tableWidgetCert)
        self.tab2.setLayout(self.tab2.layout)

    def tab_crl(self):
        crls = CRL.select()
        self.tab3.layout = QVBoxLayout(self)

        self.xline = QLineEdit(self)
        self.xline.setMaximumWidth(300)
        self.xline.textChanged[str].connect(self.on_changed_find_crl)
        self.tab3.layout.addWidget(self.xline)

        self.lableFindCRL = QLabel(self)
        self.tab3.layout.addWidget(self.lableFindCRL)

        self.tableWidgetCRL = QTableWidget(self)
        self.tableWidgetCRL.setRowCount(int(crls.count()))
        self.tableWidgetCRL.setColumnCount(8)
        self.tableWidgetCRL.verticalHeader().setVisible(False)
        self.tableWidgetCRL.setHorizontalHeaderLabels(["Р/Н",
                                                    "Название",
                                                    "Идентификатор ключа",
                                                    "Отпечаток",
                                                    "Серийный номер",
                                                    "Адрес в интернете",
                                                    "",
                                                    ""])
        self.on_changed_find_crl('')
        self.tableWidgetCRL.resizeColumnToContents(0)
        self.tableWidgetCRL.setColumnWidth(1, 150)
        self.tableWidgetCRL.setColumnWidth(2, 150)
        self.tableWidgetCRL.setColumnWidth(3, 150)
        self.tableWidgetCRL.setColumnWidth(4, 150)
        self.tableWidgetCRL.horizontalHeader().setSectionResizeMode(5, QHeaderView.Stretch)
        self.tab3.layout.addWidget(self.tableWidgetCRL)
        self.tab3.setLayout(self.tab3.layout)
        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def tab_watching_crl(self):
        self.layout_watching = QVBoxLayout()
        self.horizontalLayout_14 = QHBoxLayout()

        self.label_12 = QLabel()
        self.horizontalLayout_14.addWidget(self.label_12)

        self.pushButton_7 = QPushButton()
        self.pushButton_7.setText("Скачать CRL'ы")
        self.pushButton_7.setMaximumSize(QSize(200, 16777215))
        self.horizontalLayout_14.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton()
        self.pushButton_8.setText("Провермть спискси CRL")
        self.pushButton_8.setMaximumSize(QSize(200, 16777215))
        self.horizontalLayout_14.addWidget(self.pushButton_8)

        self.layout_watching.addLayout(self.horizontalLayout_14)

        self.verticalLayout_12 = QVBoxLayout()
        self.tabs2 = QTabWidget()
        self.tab7 = QWidget()
        self.tab8 = QWidget()
        self.tab9 = QWidget()
        self.tabs2.addTab(self.tab7, "Скачиваемые УЦ")
        self.tabs2.addTab(self.tab8, "Свои скачиваемыее УЦ")
        self.tabs2.addTab(self.tab9, "Удаленные")

        self.sub_tab_watching_crl()
        self.sub_tab_custom_watching_crl()
        self.sub_tab_deleted_watching_crl()

        self.verticalLayout_12.addWidget(self.tabs2)
        self.layout_watching.addLayout(self.verticalLayout_12)

        self.horizontalLayout_10 = QHBoxLayout()
        buttonAddCRLList = QPushButton()
        buttonAddCRLList.setText("Импортировать список CRL")
        buttonAddCRLList.pressed.connect(self.import_crl_list)
        self.horizontalLayout_10.addWidget(buttonAddCRLList)

        self.progressBar_3 = QProgressBar()
        # self.progressBar_3.setValue(1)
        self.progressBar_3.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_10.addWidget(self.progressBar_3)
        self.layout_watching.addLayout(self.horizontalLayout_10)
        self.tab4.setLayout(self.layout_watching)
        # Add tabs to widget
        # self.layout_watching.addWidget(self.tabs2)
        # self.setLayout(self.layout_watching)

    def sub_tab_watching_crl(self):
        wcrls = WatchingCRL.select()
        self.tab7.layout_watching = QVBoxLayout(self)
        self.wline = QLineEdit(self)
        self.wline.setMaximumWidth(300)
        self.wline.textChanged[str].connect(self.on_changed_find_watching_crl)
        self.tab7.layout_watching.addWidget(self.wline)

        self.lableFindWatchingCRL = QLabel(self)
        self.tab7.layout_watching.addWidget(self.lableFindWatchingCRL)

        self.tableWidgetWatchingCRL = QTableWidget(self)
        self.tableWidgetWatchingCRL.setRowCount(int(wcrls.count()))
        self.tableWidgetWatchingCRL.setColumnCount(8)
        self.tableWidgetWatchingCRL.setHorizontalHeaderLabels(["Name",
                                                       "ИНН",
                                                       "ОГРН",
                                                       "Идентификатор ключа",
                                                       "Отпечаток",
                                                       "Серийный номер",
                                                       "Адрес CRL",
                                                       ""])
        self.on_changed_find_watching_crl('')
        self.tableWidgetWatchingCRL.setColumnWidth(1, 150)
        self.tableWidgetWatchingCRL.setColumnWidth(1, 100)
        self.tableWidgetWatchingCRL.setColumnWidth(2, 100)
        self.tableWidgetWatchingCRL.setColumnWidth(3, 150)
        self.tableWidgetWatchingCRL.setColumnWidth(4, 150)
        self.tableWidgetWatchingCRL.setColumnWidth(5, 150)
        self.tableWidgetWatchingCRL.horizontalHeader().setSectionResizeMode(6, QHeaderView.Stretch)
        self.tab7.layout_watching.addWidget(self.tableWidgetWatchingCRL)
        self.tab7.setLayout(self.tab7.layout_watching)

    def sub_tab_custom_watching_crl(self):
        wccrls = WatchingCustomCRL.select()
        self.tab8.layout_watching = QVBoxLayout(self)
        self.cwline = QLineEdit(self)
        self.cwline.setMaximumWidth(300)
        self.cwline.textChanged[str].connect(self.on_changed_find_custom_watching_crl)
        self.tab8.layout_watching.addWidget(self.cwline)

        self.lableFindWatchingCustomCRL = QLabel(self)
        self.tab8.layout_watching.addWidget(self.lableFindWatchingCustomCRL)

        self.tableWidgetCustomWatchingCRL = QTableWidget(self)
        self.tableWidgetCustomWatchingCRL.setRowCount(int(wccrls.count()))
        self.tableWidgetCustomWatchingCRL.setColumnCount(8)
        self.tableWidgetCustomWatchingCRL.setHorizontalHeaderLabels(["Name",
                                                       "ИНН",
                                                       "ОГРН",
                                                       "Идентификатор ключа",
                                                       "Отпечаток",
                                                       "Серийный номер",
                                                       "Адрес CRL",
                                                       ""])
        self.on_changed_find_custom_watching_crl('')
        self.tableWidgetCustomWatchingCRL.setColumnWidth(1, 150)
        self.tableWidgetCustomWatchingCRL.setColumnWidth(1, 100)
        self.tableWidgetCustomWatchingCRL.setColumnWidth(2, 100)
        self.tableWidgetCustomWatchingCRL.setColumnWidth(3, 150)
        self.tableWidgetCustomWatchingCRL.setColumnWidth(4, 150)
        self.tableWidgetCustomWatchingCRL.setColumnWidth(5, 150)
        self.tableWidgetCustomWatchingCRL.horizontalHeader().setSectionResizeMode(6, QHeaderView.Stretch)
        self.tab8.layout_watching.addWidget(self.tableWidgetCustomWatchingCRL)
        self.tab8.setLayout(self.tab8.layout_watching)

    def sub_tab_deleted_watching_crl(self):
        wcdcrls = WatchingDeletedCRL.select()
        self.tab9.layout_deleted = QVBoxLayout(self)
        self.cwline = QLineEdit(self)
        self.cwline.setMaximumWidth(300)
        self.cwline.textChanged[str].connect(self.on_changed_find_deleted_watching_crl)
        self.tab9.layout_deleted.addWidget(self.cwline)

        self.lableFindWatchingDeleteCRL = QLabel(self)
        self.tab9.layout_deleted.addWidget(self.lableFindWatchingDeleteCRL)

        self.tableWidgetDeletedWatchingCRL = QTableWidget(self)
        self.tableWidgetDeletedWatchingCRL.setRowCount(int(wcdcrls.count()))
        self.tableWidgetDeletedWatchingCRL.setColumnCount(8)
        self.tableWidgetDeletedWatchingCRL.setHorizontalHeaderLabels(["Name",
                                                       "ИНН",
                                                       "ОГРН",
                                                       "Идентификатор ключа",
                                                       "Отпечаток",
                                                       "Серийный номер",
                                                       "Адрес CRL",
                                                       "",
                                                       ""])
        self.on_changed_find_deleted_watching_crl('')
        self.tableWidgetDeletedWatchingCRL.setColumnWidth(1, 150)
        self.tableWidgetDeletedWatchingCRL.setColumnWidth(1, 100)
        self.tableWidgetDeletedWatchingCRL.setColumnWidth(2, 100)
        self.tableWidgetDeletedWatchingCRL.setColumnWidth(3, 150)
        self.tableWidgetDeletedWatchingCRL.setColumnWidth(4, 150)
        self.tableWidgetDeletedWatchingCRL.setColumnWidth(5, 150)
        self.tableWidgetDeletedWatchingCRL.horizontalHeader().setSectionResizeMode(6, QHeaderView.Stretch)
        self.tab9.layout_deleted.addWidget(self.tableWidgetDeletedWatchingCRL)
        self.tab9.setLayout(self.tab9.layout_deleted)

    def tab_settings(self):
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_23 = QVBoxLayout()
        self.horizontalLayout_6 = QHBoxLayout()
        self.verticalLayout_25 = QVBoxLayout()
        self.frame_7 = QFrame()
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.verticalLayout_25.addWidget(self.frame_7)

        self.horizontalLayout_6.addLayout(self.verticalLayout_25)

        self.verticalLayout_24 = QVBoxLayout()
        self.frame_8 = QFrame()
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)

        self.verticalLayout_24.addWidget(self.frame_8)

        self.horizontalLayout_6.addLayout(self.verticalLayout_24)

        self.verticalLayout_23.addLayout(self.horizontalLayout_6)

        self.verticalLayout_14.addLayout(self.verticalLayout_23)

        self.verticalLayout_17 = QVBoxLayout()
        self.horizontalLayout_3 = QHBoxLayout()
        self.verticalLayout_20 = QVBoxLayout()
        self.frame_5 = QFrame()
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_31 = QVBoxLayout()
        self.label_12 = QLabel('  Настройка директорий')

        self.verticalLayout_31.addWidget(self.label_12, 0, Qt.AlignTop)

        self.horizontalLayout_9 = QHBoxLayout()
        self.pushButton_4 = QPushButton(self.frame_5)
        self.pushButton_4.setText("Папка с CRL")
        self.pushButton_4.clicked.connect(lambda: self.choose_directory('crl'))
        self.horizontalLayout_9.addWidget(self.pushButton_4, 0, Qt.AlignVCenter)

        self.pushButton_5 = QPushButton(self.frame_5)
        self.pushButton_5.setText("Папка с сертами")
        self.pushButton_5.clicked.connect(lambda: self.choose_directory('cert'))
        self.horizontalLayout_9.addWidget(self.pushButton_5, 0, Qt.AlignVCenter)

        self.pushButton_3 = QPushButton(self.frame_5)
        self.pushButton_3.setText("Папка для УЦ")
        self.pushButton_3.clicked.connect(lambda: self.choose_directory('uc'))
        self.horizontalLayout_9.addWidget(self.pushButton_3, 0, Qt.AlignVCenter)

        self.verticalLayout_31.addLayout(self.horizontalLayout_9)

        self.verticalLayout_33 = QVBoxLayout()
        self.label_9 = QLabel('  Папка с CRL: ')

        self.verticalLayout_33.addWidget(self.label_9)

        self.label_10 = QLabel('  Папка с сертификатами: ')

        self.verticalLayout_33.addWidget(self.label_10)

        self.label_11 = QLabel('  Папка для УЦ: ')

        self.verticalLayout_33.addWidget(self.label_11)

        self.verticalLayout_31.addLayout(self.verticalLayout_33)

        self.horizontalLayout_8.addLayout(self.verticalLayout_31)

        self.verticalLayout_20.addWidget(self.frame_5)

        self.horizontalLayout_3.addLayout(self.verticalLayout_20)

        self.verticalLayout_19 = QVBoxLayout()
        self.frame_6 = QFrame()
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.verticalLayout_19.addWidget(self.frame_6)

        self.horizontalLayout_3.addLayout(self.verticalLayout_19)

        self.verticalLayout_26 = QVBoxLayout()
        self.frame_9 = QFrame()
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)

        self.verticalLayout_26.addWidget(self.frame_9)

        self.horizontalLayout_3.addLayout(self.verticalLayout_26)

        self.verticalLayout_17.addLayout(self.horizontalLayout_3)

        self.verticalLayout_14.addLayout(self.verticalLayout_17)

        self.verticalLayout_18 = QVBoxLayout()
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_5 = QHBoxLayout()
        self.verticalLayout_22 = QVBoxLayout()
        self.frame_4 = QFrame()
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.verticalLayout_22.addWidget(self.frame_4)

        self.horizontalLayout_5.addLayout(self.verticalLayout_22)

        self.verticalLayout_28 = QVBoxLayout()

        self.horizontalLayout_5.addLayout(self.verticalLayout_28)

        self.verticalLayout_21 = QVBoxLayout()
        self.frame_10 = QFrame()
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)

        self.verticalLayout_21.addWidget(self.frame_10)

        self.horizontalLayout_5.addLayout(self.verticalLayout_21)

        self.horizontalLayout_4.addLayout(self.horizontalLayout_5)

        self.verticalLayout_18.addLayout(self.horizontalLayout_4)

        self.verticalLayout_14.addLayout(self.verticalLayout_18)

        self.verticalLayout_15.addLayout(self.verticalLayout_14)
        self.tab5.setLayout(self.verticalLayout_15)

    def open_sub_window_info_uc(self, reg_number):
        if self.window_uc is None:
            self.window_uc = SubWindowUC(reg_number)
            self.window_uc.show()
        else:
            self.window_uc.close()  # Close window.
            self.window_uc = None  # Discard reference.

    def choose_directory(self, type):
        input_dir = QFileDialog.getExistingDirectory(None, 'Выбор директории:', expanduser("~"))
        if type == 'crl':
            self.label_9.setText('  Папка с CRL: '+input_dir)
        if type == 'cert':
            self.label_10.setText('  Папка с сертификатами: '+input_dir)
        if type == 'uc':
            self.label_11.setText('  Папка для УЦ: '+input_dir)

    """
    def init_tsl(self):
        self.d_bar.show()
        self.currentTread.setText('Скачиваем список.')
        time.sleep(0.05)
        self.currentTread.adjustSize()

        download_file('https://e-trust.gosuslugi.ru/CA/DownloadTSL?schemaVersion=0', 'tsl.xml', '')
        self.currentTread.setText('Скачали.')
        self.currentTread.setText('Очищаем базу.')
        UC.drop_table()
        CRL.drop_table()
        CERT.drop_table()
        self.currentTread.setText('Создаем базу.')
        UC.create_table()
        CERT.create_table()
        CRL.create_table()
        self.currentTread.setText('Обрабатываем данные.')
        parseXML("tsl.xml")
        self.currentTread.setText('Готово.')
        self.d_bar.hide()

    """

    def on_changed_find_uc(self, text=''):
        self.lableFindUC.setText('Ищем: ' + text)
        self.lableFindUC.adjustSize()

        query = UC.select().where(UC.Registration_Number.contains(text)
                                  | UC.INN.contains(text)
                                  | UC.OGRN.contains(text)
                                  | UC.Full_Name.contains(text)).limit(config['Listing']['uc'])
        count_all = UC.select().where(UC.Registration_Number.contains(text)
                                      | UC.INN.contains(text)
                                      | UC.OGRN.contains(text)
                                      | UC.Full_Name.contains(text)).limit(config['Listing']['uc']).count()
        self.tableWidget.setRowCount(count_all)
        count = 0
        for row in query:
            self.tableWidget.setItem(count, 0, QTableWidgetItem(str(row.Registration_Number)))
            self.tableWidget.setItem(count, 1, QTableWidgetItem(str(row.INN)))
            self.tableWidget.setItem(count, 2, QTableWidgetItem(str(row.OGRN)))
            self.tableWidget.setItem(count, 3, QTableWidgetItem(str(row.Full_Name)))
            buttonInfo = QPushButton()
            buttonInfo.setFixedSize(100, 30)
            buttonInfo.setText("Подробнее")
            regnum = row.Registration_Number
            buttonInfo.pressed.connect(lambda rg=regnum: self.open_sub_window_info_uc(rg))
            self.tableWidget.setCellWidget(count, 4, buttonInfo)
            count = count + 1

    def on_changed_find_cert(self, text=''):
        self.lableFindCert.setText('Ищем: ' + text)
        self.lableFindCert.adjustSize()

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
        self.tableWidgetCert.setRowCount(count_all)
        count = 0
        for row in query:
            self.tableWidgetCert.setItem(count, 0, QTableWidgetItem(str(row.Registration_Number)))
            self.tableWidgetCert.setItem(count, 1, QTableWidgetItem(str(row.Name)))
            self.tableWidgetCert.setItem(count, 2, QTableWidgetItem(str(row.KeyId)))
            self.tableWidgetCert.setItem(count, 3, QTableWidgetItem(str(row.Stamp)))
            self.tableWidgetCert.setItem(count, 4, QTableWidgetItem(str(row.SerialNumber)))

            self.buttonSert = QPushButton()
            self.buttonSert.setFixedSize(150, 30)
            self.buttonSert.setText("Просмотр сертификата")
            serrial = row.SerialNumber
            self.buttonSert.pressed.connect(lambda sn = serrial: open_file(sn, "cer"))
            self.tableWidgetCert.setCellWidget(count, 5, self.buttonSert)

            buttonSertSave = QPushButton()
            buttonSertSave.setFixedSize(100, 30)
            buttonSertSave.setText("Сохранить")
            sn = row.SerialNumber
            buttonSertSave.pressed.connect(lambda serrial = sn: save_cert(serrial))
            self.tableWidgetCert.setCellWidget(count, 6, buttonSertSave)
            count = count + 1

    def on_changed_find_crl(self, text=''):
        self.lableFindCRL.setText('Ищем: ' + text)
        self.lableFindCRL.adjustSize()

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
        self.tableWidgetCRL.setRowCount(count_all)
        count = 0
        for row in query:
            self.tableWidgetCRL.setItem(count, 0, QTableWidgetItem(str(row.Registration_Number)))
            self.tableWidgetCRL.setItem(count, 1, QTableWidgetItem(str(row.Name)))
            self.tableWidgetCRL.setItem(count, 2, QTableWidgetItem(str(row.KeyId)))
            self.tableWidgetCRL.setItem(count, 3, QTableWidgetItem(str(row.Stamp)))
            self.tableWidgetCRL.setItem(count, 4, QTableWidgetItem(str(row.SerialNumber)))
            self.tableWidgetCRL.setItem(count, 5, QTableWidgetItem(str(row.UrlCRL)))
            buttonCRLSave = QPushButton()
            buttonCRLSave.setFixedSize(100, 30)
            buttonCRLSave.setText("Скачать")
            stamp = row.Stamp
            url = row.UrlCRL
            buttonCRLSave.pressed.connect(lambda u=url, s=stamp: download_file(u, s, config['Folders']['crls']))
            self.tableWidgetCRL.setCellWidget(count, 6, buttonCRLSave)

            button_add_to_watch = QPushButton()
            button_add_to_watch.setFixedSize(100, 30)
            button_add_to_watch.setText("Отслеживать")
            rb = row.Registration_Number
            ki = row.KeyId
            st = row.Stamp
            sn = row.SerialNumber
            uc = row.UrlCRL
            button_add_to_watch.pressed.connect(lambda registration_number = rb,
                                                       keyid = ki,
                                                       stamp = st,
                                                       serial_number = sn,
                                                       url_crl = uc: self.add_watch_cert_crl(registration_number,
                                                                                             keyid,
                                                                                             stamp,
                                                                                             serial_number,
                                                                                             url_crl))
            self.tableWidgetCRL.setCellWidget(count, 7, button_add_to_watch)

            count = count + 1

    def on_changed_find_watching_crl(self, text=''):
        self.lableFindWatchingCRL.setText('Ищем: ' + text)
        self.lableFindWatchingCRL.adjustSize()

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
                                               | WatchingCRL.UrlCRL.contains(text)).limit(config['Listing']['watch']).count()
        self.tableWidgetWatchingCRL.setRowCount(count_all)
        count = 0
        for row in query:
            self.tableWidgetWatchingCRL.setItem(count, 0, QTableWidgetItem(str(row.Name)))
            self.tableWidgetWatchingCRL.setItem(count, 1, QTableWidgetItem(str(row.INN)))
            self.tableWidgetWatchingCRL.setItem(count, 2, QTableWidgetItem(str(row.OGRN)))
            self.tableWidgetWatchingCRL.setItem(count, 3, QTableWidgetItem(str(row.KeyId)))
            self.tableWidgetWatchingCRL.setItem(count, 4, QTableWidgetItem(str(row.Stamp)))
            self.tableWidgetWatchingCRL.setItem(count, 5, QTableWidgetItem(str(row.SerialNumber)))
            self.tableWidgetWatchingCRL.setItem(count, 6, QTableWidgetItem(str(row.UrlCRL)))

            buttonDeleteWatch = QPushButton()
            buttonDeleteWatch.setFixedSize(100, 30)
            buttonDeleteWatch.setText("Удалить")
            id = row.ID
            buttonDeleteWatch.pressed.connect(lambda o=id: self.move_watching_to_delete(o, 'current'))
            self.tableWidgetWatchingCRL.setCellWidget(count, 7, buttonDeleteWatch)
            count = count + 1

    def on_changed_find_custom_watching_crl(self, text=''):
        self.lableFindWatchingCustomCRL.setText('Ищем: ' + text)
        self.lableFindWatchingCustomCRL.adjustSize()

        query = WatchingCustomCRL.select().where(WatchingCustomCRL.Name.contains(text)
                                           | WatchingCustomCRL.INN.contains(text)
                                           | WatchingCustomCRL.OGRN.contains(text)
                                           | WatchingCustomCRL.KeyId.contains(text)
                                           | WatchingCustomCRL.Stamp.contains(text)
                                           | WatchingCustomCRL.SerialNumber.contains(text)
                                           | WatchingCustomCRL.UrlCRL.contains(text)).limit(config['Listing']['watch'])
        count_all = WatchingCustomCRL.select().where(WatchingCustomCRL.Name.contains(text)
                                               | WatchingCustomCRL.INN.contains(text)
                                               | WatchingCustomCRL.OGRN.contains(text)
                                               | WatchingCustomCRL.KeyId.contains(text)
                                               | WatchingCustomCRL.Stamp.contains(text)
                                               | WatchingCustomCRL.SerialNumber.contains(text)
                                               | WatchingCustomCRL.UrlCRL.contains(text)).limit(config['Listing']['watch']).count()
        self.tableWidgetCustomWatchingCRL.setRowCount(count_all)
        count = 0
        for row in query:
            self.tableWidgetCustomWatchingCRL.setItem(count, 0, QTableWidgetItem(str(row.Name)))
            self.tableWidgetCustomWatchingCRL.setItem(count, 1, QTableWidgetItem(str(row.INN)))
            self.tableWidgetCustomWatchingCRL.setItem(count, 2, QTableWidgetItem(str(row.OGRN)))
            self.tableWidgetCustomWatchingCRL.setItem(count, 3, QTableWidgetItem(str(row.KeyId)))
            self.tableWidgetCustomWatchingCRL.setItem(count, 4, QTableWidgetItem(str(row.Stamp)))
            self.tableWidgetCustomWatchingCRL.setItem(count, 5, QTableWidgetItem(str(row.SerialNumber)))
            self.tableWidgetCustomWatchingCRL.setItem(count, 6, QTableWidgetItem(str(row.UrlCRL)))

            # buttonDeleteWatch = QPushButton()
            # buttonDeleteWatch.setFixedSize(100, 30)
            # buttonDeleteWatch.setText("Удалить")
            # id = row.ID
            # buttonDeleteWatch.pressed.connect(lambda i=id: self.delete_watching(i))
            # self.tableWidgetCustomWatchingCRL.setCellWidget(count, 7, buttonDeleteWatch)

            count = count + 1

    def on_changed_find_deleted_watching_crl(self, text=''):
        self.lableFindWatchingDeleteCRL.setText('Ищем: ' + text)
        self.lableFindWatchingDeleteCRL.adjustSize()

        query = WatchingDeletedCRL.select().where(WatchingDeletedCRL.Name.contains(text)
                                           | WatchingDeletedCRL.INN.contains(text)
                                           | WatchingDeletedCRL.OGRN.contains(text)
                                           | WatchingDeletedCRL.KeyId.contains(text)
                                           | WatchingDeletedCRL.Stamp.contains(text)
                                           | WatchingDeletedCRL.SerialNumber.contains(text)
                                           | WatchingDeletedCRL.UrlCRL.contains(text)).limit(config['Listing']['watch'])
        count_all = WatchingDeletedCRL.select().where(WatchingDeletedCRL.Name.contains(text)
                                               | WatchingDeletedCRL.INN.contains(text)
                                               | WatchingDeletedCRL.OGRN.contains(text)
                                               | WatchingDeletedCRL.KeyId.contains(text)
                                               | WatchingDeletedCRL.Stamp.contains(text)
                                               | WatchingDeletedCRL.SerialNumber.contains(text)
                                               | WatchingDeletedCRL.UrlCRL.contains(text)).limit(config['Listing']['watch']).count()
        self.tableWidgetDeletedWatchingCRL.setRowCount(count_all)
        count = 0
        for row in query:
            self.tableWidgetDeletedWatchingCRL.setItem(count, 0, QTableWidgetItem(str(row.Name)))
            self.tableWidgetDeletedWatchingCRL.setItem(count, 1, QTableWidgetItem(str(row.INN)))
            self.tableWidgetDeletedWatchingCRL.setItem(count, 2, QTableWidgetItem(str(row.OGRN)))
            self.tableWidgetDeletedWatchingCRL.setItem(count, 3, QTableWidgetItem(str(row.KeyId)))
            self.tableWidgetDeletedWatchingCRL.setItem(count, 4, QTableWidgetItem(str(row.Stamp)))
            self.tableWidgetDeletedWatchingCRL.setItem(count, 5, QTableWidgetItem(str(row.SerialNumber)))
            self.tableWidgetDeletedWatchingCRL.setItem(count, 6, QTableWidgetItem(str(row.UrlCRL)))

            # buttonDeleteWatch = QPushButton()
            # buttonDeleteWatch.setFixedSize(100, 30)
            # buttonDeleteWatch.setText("Удалить")
            # self.tableWidgetDeletedWatchingCRL.setCellWidget(count, 7, buttonDeleteWatch)
#
            count = count + 1

    def download_xml(self):
        self.currentTread.setText('Скачиваем список.')
        self.currentTread.adjustSize()
        self.pushButton.setEnabled(False)
        self.pushButton_2.setEnabled(False)
        self._download = Downloader('https://e-trust.gosuslugi.ru/CA/DownloadTSL?schemaVersion=0', 'tsl.xml')
        # Устанавливаем максимальный размер данных
        self._download.preprogress.connect(lambda x: self.progressBar.setMaximum(x))
        # Промежуточный/скачанный размер
        self._download.progress.connect(lambda y: self.progressBar.setValue(y))
        # говорим что всё скачано
        self._download.downloading.connect(lambda z: self.currentTread.setText(z))
        self._download.done.connect(lambda z: self.currentTread.setText(z))
        self._download.done.connect(lambda hint1: self.pushButton.setEnabled(True))
        self._download.done.connect(lambda hint2: self.pushButton_2.setEnabled(True))
        self._download.done.connect(lambda hint3: self.on_changed_find_uc(''))
        self._download.done.connect(lambda hint4: self.on_changed_find_cert(''))
        self._download.done.connect(lambda hint5: self.on_changed_find_crl(''))
        self._download.start()

    def init_xml(self):
        self.pushButton_2.setEnabled(False)
        self.pushButton.setEnabled(False)
        UC.drop_table()
        CRL.drop_table()
        CERT.drop_table()
        UC.create_table()
        CERT.create_table()
        CRL.create_table()
        self.currentTread.setText('Обрабатываем данные.')
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
                self.currentTread.setText('Обрабатываем данные:\n УЦ: ' + Name)
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
                    self.progressBar_2.setValue(crl_percent_step)
        # print('Центров:' + str(uc_count))
        # print('Сертов:' + str(cert_count))
        # print('CRL:' + str(crl_count))
        # current_version
        # last_update
        self.lable_2.setText(" Версия базы: " + current_version)
        self.lable_3.setText(" Дата выпуска базы: " + last_update)
        self.lable_5.setText(" Всего УЦ: " + str(uc_count))
        self.lable_6.setText(" Всего Сертификатов: " + str(cert_count))
        self.lable_7.setText(" Всего CRL: " + str(crl_count))
        query_ver = Settings.update(value=current_version).where(Settings.name == 'ver')
        query_ver.execute()
        query_data_update = Settings.update(value=last_update).where(Settings.name == 'data_update')
        query_data_update.execute()
        self.pushButton.setEnabled(True)
        self.pushButton_2.setEnabled(True)
        self.currentTread.setText('Готово.')

    def add_watch_cert_crl(self, registration_number, keyid, stamp, serial_number, url_crl):
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
                                                  UrlCRL=url_crl)
                add_to_watching_crl.save()
                # self.counter_added = self.counter_added + 1
        else:
            print('crl exist')
            # self.counter_added_exist = self.counter_added_exist + 1
        self.on_changed_find_watching_crl('')

    def add_watch_custom_cert_crl(self, url_crl):
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

    def move_watching_to_delete(self, id, froms):
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

    # def delete_watching(self, id):
    #     WatchingCRL.delete_by_id(id)
    #     self.on_changed_find_watching_crl('')
    #     print(id + ' id is deleted')

    def import_crl_list(self, file_name='crl_list.txt'):
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


class SubWindowUC(QWidget):
    def __init__(self, RegNumber):
        super().__init__()
        self.init(RegNumber)

    def init(self, RegNumber):
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

        title = Name
        left = 0
        top = 0
        width = 900
        height = 400
        self.setWindowTitle(title)
        self.setWindowIcon(QIcon('assests/favicon.ico'))
        self.setGeometry(left, top, width, height)
        self.main_layout = QHBoxLayout()

        topleft = QFrame(self)
        topleft.setFixedHeight(150)
        topleft.setFrameShape(QFrame.StyledPanel)

        topright = QFrame(self)
        topright.setFrameShape(QFrame.StyledPanel)

        self.bottom = QFrame(self)
        self.bottom.setFrameShape(QFrame.StyledPanel)

        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(topleft)
        splitter1.addWidget(topright)

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(self.bottom)

        self.main_layout.setAlignment(Qt.AlignTop)

        topleft.setStyleSheet("background-color: white")
        company_vertical = QVBoxLayout()
        company_vertical.addWidget(QLabel(Registration_Number))
        company_vertical.addWidget(QLabel(INN))
        company_vertical.addWidget(QLabel(OGRN))
        company_vertical.addWidget(QLabel(Full_Name))
        company_vertical.addWidget(QLabel(Email))
        company_vertical.addWidget(QLabel(Name))
        company_vertical.addWidget(QLabel(URL))
        topleft.setLayout(company_vertical)

        topright.setStyleSheet("background-color: white")
        address_vertical = QVBoxLayout()
        address_vertical.addWidget(QLabel(AddresCode))
        address_vertical.addWidget(QLabel(AddresName))
        address_vertical.addWidget(QLabel(AddresIndex))
        address_vertical.addWidget(QLabel(AddresAddres))
        address_vertical.addWidget(QLabel(AddresStreet))
        address_vertical.addWidget(QLabel(AddresTown))
        topright.setLayout(address_vertical)

        self.get_crls_uc(RegNumber)

        self.main_layout.addWidget(splitter2)
        self.setLayout(self.main_layout)

    def get_crls_uc(self, RegNumber):
        Registration_Number = 'Unknown'
        KeyId = 'Unknown'
        Stamp = 'Unknown'
        SerialNumber = 'Unknown'
        UrlCRL = 'Unknown'
        query = CRL.select().where(CRL.Registration_Number == RegNumber)
        main_crls_frame = QVBoxLayout()
        main_crls_frame.setAlignment(Qt.AlignTop)

        for row in query:
            crls_frame = QFrame()
            crls_frame.setFixedHeight(30)
            crls_frame.setStyleSheet("background-color: white")
            crls_vertical = QHBoxLayout()
            crls_vertical.addWidget(QLabel(str(row.Registration_Number)))
            crls_vertical.addWidget(QLabel(str(row.KeyId)))
            crls_vertical.addWidget(QLabel(str(row.Stamp)))
            crls_vertical.addWidget(QLabel(str(row.SerialNumber)))
            crls_vertical.addWidget(QLabel(str(row.UrlCRL)))
            crls_frame.setLayout(crls_vertical)
            main_crls_frame.addWidget(crls_frame)
        self.bottom.setLayout(main_crls_frame)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle(config['Style']['Window'])
    ex = MainWindow()
    sys.exit(app.exec_())
