# PyQt5, lxml, peewee
import base64, sys, socket, sqlite3, os, configparser
from urllib import request, error
from functools import partial
from PyQt5.QtWidgets import QMainWindow, \
    QApplication, QPushButton, QWidget, QAction, \
    QTabWidget, QVBoxLayout, QHBoxLayout, QLabel, QBoxLayout, \
    QTableWidgetItem, QTableWidget, QFrame, QSplitter, QGridLayout, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication, Qt
from lxml import etree
from peewee import *


config = configparser.ConfigParser()
config.read('settings.ini')

socket.setdefaulttimeout(15)
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
    OGRN  = IntegerField()
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
    KeyId = CharField()
    Stamp = CharField()
    SerialNumber = CharField()
    Data = CharField()

    class Meta:
        database = db


class CRL(Model):
    ID = IntegerField(primary_key=True)
    Registration_Number = IntegerField()
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


def progressbar(cur, total=100):
    percent = '{:.2%}'.format(cur / total)
    sys.stdout.write('\r')
    # sys.stdout.write("[%-50s] %s" % ('=' * int(math.floor(cur * 50 / total)),percent))
    sys.stdout.write("[%-100s] %s" % ('=' * int(cur), percent))
    sys.stdout.flush()


def schedule(blocknum, blocksize, totalsize):
    """
    blocknum: currently downloaded block
         blocksize: block size for each transfer
         totalsize: total size of web page files
    """
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
                                # print(dats)
                cert = CERT(Registration_Number = Registration_Number,
                            KeyId = KeyId,
                            Stamp = Stamp,
                            SerialNumber = SerialNumber,
                            Data = Data)
                cert.save()
                crl = CRL(Registration_Number = Registration_Number,
                          KeyId=KeyId,
                          Stamp=Stamp,
                          SerialNumber=SerialNumber,
                          UrlCRL = UrlCRL)
                crl.save()

    print('Центров:' + str(uc_count))
    print('Сертов:' + str(cert_count))
    print('CRL:' + str(crl_count))


def save_cert(seriall_number):
    for certs in CERT.select().where(CERT.SerialNumber == seriall_number):
        with open("certs/" + certs.SerialNumber + ".cer", "wb") as file:
            file.write(base64.decodebytes(certs.Data.encode()))


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


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'E-Trust CRL Parsing'
        self.left = 0
        self.top = 0
        self.width = 1200
        self.height = 400
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon('assests/favicon.ico'))
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.tab_widget = TabWidget(self)
        self.setCentralWidget(self.tab_widget)

        self.show()


class TabWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.window_uc = None
        self.layout = QVBoxLayout(self)

        # Init BD

        seting = Settings.select()

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab0 = QWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()

        # Add tabs
        self.tabs.addTab(self.tab0, "Инициальзация")
        self.tabs.addTab(self.tab1, "Список УЦ")
        self.tabs.addTab(self.tab2, "Список Сертификатов")
        self.tabs.addTab(self.tab3, "Список CRL")
        self.tabs.addTab(self.tab4, "Скачиваемые УЦ")
        self.tabs.addTab(self.tab5, "Настройки")

        self.tab_info()
        self.tab_uc()
        self.tab_cert()
        self.tab_crl()

    def tab_info(self):
        ucs = UC.select()
        certs = CERT.select()
        crls = CRL.select()

        self.tab0.layout = QVBoxLayout(self)

        self.topFrame = QFrame(self)
        # self.topFrame.setStyleSheet("background-color: green")
        self.topFrame.setFixedSize(400, 150)
        self.inf = QVBoxLayout(self)
        settings_ver = '0'
        settings_update_date = '0'
        query = Settings.select()
        for data in query:
            if data.name == 'ver':
                settings_ver = data.value
            if data.name == 'data_update':
                settings_update_date = data.value
        self.inf.addWidget(QLabel("Начальная инициализация сертификатов и списка отзыва: "))
        self.inf.addWidget(QLabel("Версия базы: " + settings_ver))
        self.inf.addWidget(QLabel("Дата выпуска базы: " + settings_update_date))
        self.inf.addWidget(QLabel("Всего УЦ: " + str(ucs.count())))
        self.inf.addWidget(QLabel("Всего CRL: " + str(crls.count())))
        self.inf.addWidget(QLabel("УЦ для загрузки отмечено: " + str(ucs.count())))
        self.inf.addWidget(QLabel("CRL будет загружено: " + str(crls.count())))
        self.topFrame.setLayout(self.inf)
        self.tab0.layout.addWidget(self.topFrame)

        buttonInit = QPushButton()
        buttonInit.setText("Загрузить и обновить информацию")
        buttonInit.setFixedSize(250, 30)
        buttonInit.clicked.connect(self.init_tsl)
        self.tab0.layout.addWidget(buttonInit)

        self.tab0.setLayout(self.tab0.layout)

    def tab_uc(self):
        ucs = UC.select()
        self.tab1.layout = QVBoxLayout(self)

        self.qline = QLineEdit(self)
        self.qline.setMaximumWidth(300)
        self.qline.textChanged[str].connect(self.onChangedFindUC)
        self.tab1.layout.addWidget(self.qline)

        self.lableFindUC = QLabel(self)
        self.tab1.layout.addWidget(self.lableFindUC)

        self.tableWidget = QTableWidget(self)
        self.tableWidget.setRowCount(int(ucs.count()))
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(["Р/Н",
                                                    "ИНН",
                                                    "ОГРН",
                                                    "Название",
                                                    ""])

        self.onChangedFindUC('')
        self.tableWidget.resizeColumnsToContents()
        self.tab1.layout.addWidget(self.tableWidget)
        self.tab1.setLayout(self.tab1.layout)

    def tab_cert(self):
        certs = CERT.select()
        self.tab2.layout = QVBoxLayout(self)

        self.zline = QLineEdit(self)
        self.zline.setMaximumWidth(300)
        self.zline.textChanged[str].connect(self.onChangedFindCert)
        self.tab2.layout.addWidget(self.zline)

        self.lableFindCert = QLabel(self)
        self.tab2.layout.addWidget(self.lableFindCert)

        self.tableWidgetCert = QTableWidget(self)
        self.tableWidgetCert.setRowCount(int(certs.count()))
        self.tableWidgetCert.setColumnCount(6)
        self.tableWidgetCert.setHorizontalHeaderLabels(["Р/Н",
                                                    "Идентификатор ключа",
                                                    "Отпечаток",
                                                    "Серийный номер",
                                                    "",
                                                    ""])
        self.onChangedFindCert('')
        self.tableWidgetCert.resizeColumnsToContents()
        self.tab2.layout.addWidget(self.tableWidgetCert)
        self.tab2.setLayout(self.tab2.layout)

    def tab_crl(self):
        crls = CRL.select()
        self.tab3.layout = QVBoxLayout(self)

        self.xline = QLineEdit(self)
        self.xline.setMaximumWidth(300)
        self.xline.textChanged[str].connect(self.onChangedFindCRL)
        self.tab3.layout.addWidget(self.xline)

        self.lableFindCRL = QLabel(self)
        self.tab3.layout.addWidget(self.lableFindCRL)

        self.tableWidgetCRL = QTableWidget(self)
        self.tableWidgetCRL.setRowCount(int(crls.count()))
        self.tableWidgetCRL.setColumnCount(6)
        self.tableWidgetCRL.setHorizontalHeaderLabels(["Р/Н",
                                                    "Идентификатор ключа",
                                                    "Отпечаток",
                                                    "Серийный номер",
                                                    "Адрес в интернете",
                                                    ""])
        self.onChangedFindCRL('')

        self.tab3.layout.addWidget(self.tableWidgetCRL)
        self.tab3.setLayout(self.tab3.layout)
        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def openSubWindowInfoUc(self, RegNumber):
        if self.window_uc is None:
            self.window_uc = SubWindowUC(RegNumber)
            self.window_uc.show()
        else:
            self.window_uc.close()  # Close window.
            self.window_uc = None  # Discard reference.

    def init_tsl(self):
        download_file('https://e-trust.gosuslugi.ru/CA/DownloadTSL?schemaVersion=0', 'tsl.xml', '')

        UC.drop_table()
        CRL.drop_table()
        CERT.drop_table()

        UC.create_table()
        CERT.create_table()
        CRL.create_table()

        parseXML("tsl.xml")

    def onChangedFindUC(self, text):
        self.lableFindUC.setText('Ищем по ОГРН: ' + text)
        self.lableFindUC.adjustSize()

        query = UC.select().where(UC.OGRN.contains(text))
        count_all = UC.select().where(UC.OGRN.contains(text)).count()
        self.tableWidget.setRowCount(count_all)
        count = 0
        for row in query:
            self.tableWidget.setItem(count, 0, QTableWidgetItem(str(row.Registration_Number)))
            self.tableWidget.setItem(count, 1, QTableWidgetItem(str(row.INN)))
            self.tableWidget.setItem(count, 2, QTableWidgetItem(str(row.OGRN)))
            self.tableWidget.setItem(count, 3, QTableWidgetItem(str(row.Name)))
            buttonInfo = QPushButton()
            buttonInfo.setFixedSize(100, 30)
            buttonInfo.setText("Подробнее")
            regnum = row.Registration_Number
            buttonInfo.pressed.connect(lambda rg=regnum: self.openSubWindowInfoUc(rg))
            self.tableWidget.setCellWidget(count, 4, buttonInfo)
            count = count + 1
        self.tableWidget.resizeColumnsToContents()

    def onChangedFindCert(self, text):
        self.lableFindCert.setText('Ищем по Отпечатку: ' + text)
        self.lableFindCert.adjustSize()

        query = CERT.select().where(CERT.Stamp.contains(text))
        count_all = CERT.select().where(CERT.Stamp.contains(text)).count()
        self.tableWidgetCert.setRowCount(count_all)
        count = 0
        for row in query:
            self.tableWidgetCert.setItem(count, 0, QTableWidgetItem(str(row.Registration_Number)))
            self.tableWidgetCert.setItem(count, 1, QTableWidgetItem(str(row.KeyId)))
            self.tableWidgetCert.setItem(count, 2, QTableWidgetItem(str(row.Stamp)))
            self.tableWidgetCert.setItem(count, 3, QTableWidgetItem(str(row.SerialNumber)))

            self.buttonSert = QPushButton()
            self.buttonSert.setFixedSize(150, 30)
            self.buttonSert.setText("Просмотр сертификата")
            self.tableWidgetCert.setCellWidget(count, 4, self.buttonSert)

            buttonSertSave = QPushButton()
            buttonSertSave.setFixedSize(100, 30)
            buttonSertSave.setText("Сохранить")
            sn = row.SerialNumber
            buttonSertSave.pressed.connect(lambda serrial = sn: save_cert(serrial))
            self.tableWidgetCert.setCellWidget(count, 5, buttonSertSave)
            count = count + 1
        self.tableWidgetCert.resizeColumnsToContents()

    def onChangedFindCRL(self, text):
        self.lableFindCRL.setText('Ищем по Отпечатку: ' + text)
        self.lableFindCRL.adjustSize()

        query = CRL.select().where(CRL.Stamp.contains(text))
        count_all = CRL.select().where(CRL.Stamp.contains(text)).count()
        self.tableWidgetCRL.setRowCount(count_all)
        count = 0
        for row in query:
            self.tableWidgetCRL.setItem(count, 0, QTableWidgetItem(str(row.Registration_Number)))
            self.tableWidgetCRL.setItem(count, 1, QTableWidgetItem(str(row.KeyId)))
            self.tableWidgetCRL.setItem(count, 2, QTableWidgetItem(str(row.Stamp)))
            self.tableWidgetCRL.setItem(count, 3, QTableWidgetItem(str(row.SerialNumber)))
            self.tableWidgetCRL.setItem(count, 4, QTableWidgetItem(str(row.UrlCRL)))
            buttonCRLSave = QPushButton()
            buttonCRLSave.setFixedSize(100, 30)
            buttonCRLSave.setText("Сохранить")
            stamp = row.Stamp
            url = row.UrlCRL
            buttonCRLSave.pressed.connect(lambda u=url, s=stamp: download_file(u, s, config['Folders']['crls']))
            self.tableWidgetCRL.setCellWidget(count, 5, buttonCRLSave)
            count = count + 1
        self.tableWidgetCRL.resizeColumnToContents(0)
        self.tableWidgetCRL.resizeColumnToContents(1)
        self.tableWidgetCRL.resizeColumnToContents(2)
        self.tableWidgetCRL.setColumnWidth(3, 150)
        self.tableWidgetCRL.setColumnWidth(4, 200)


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
    ex = MainWindow()
    sys.exit(app.exec_())
