from PyQt5.QtCore import pyqtSignal, QThread
from lxml import etree
from main_models import UC, CRL, CERT, Settings, db
from main_log_system import logs
import math
import os
import peewee
import time


class InitXML(QThread):
    progressbar = pyqtSignal(int)
    current_uc = pyqtSignal(str)
    done_ver = pyqtSignal(str)
    done_date = pyqtSignal(str)
    done_all_uc = pyqtSignal(str)
    done_all_cert = pyqtSignal(str)
    done_all_crl = pyqtSignal(str)
    done_err = pyqtSignal(str)

    def __init__(self, xml_file):
        QThread.__init__(self)
        self._init = False
        self.fileName = xml_file

    def run(self):
        self.current_uc.emit('Инициализвация..')
        logs('Info: Init TLS started', 'info', '5')
        UC.drop_table()
        CRL.drop_table()
        CERT.drop_table()
        UC.create_table()
        CERT.create_table()
        CRL.create_table()

        if os.path.exists(self.fileName):
            with open(self.fileName, "rt", encoding="utf-8") as obj:
                xml = obj.read().encode()
            try:
                root = etree.fromstring(xml)
            except etree.XMLSyntaxError:
                self.current_uc.emit('XML Файл имеет неподдерживаемую структуру, необходимо скачать заново.')
                self.done_err.emit('XML Файл имеет неподдерживаемую структуру, необходимо скачать заново.')
                logs('Error: XMLSyntaxError ' + self.fileName, 'errors', '2')
            else:
                uc_count = 0
                cert_count = 0
                crl_count = 0
                crl_count_all = 3267
                current_version = 'Unknown'
                last_update = 'Unknown'
                for element in root.getchildren():
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
                    if element.text:
                        if element.tag == 'Версия':
                            current_version = element.text
                    if element.text:
                        if element.tag == 'Дата':
                            last_update = element.text
                    for elem in element.getchildren():
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
                                                                                    data_cert['serial'] = six_elem.text
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
                        self.current_uc.emit('Обрабатываем данные: ' + name)
                        logs('Info: Processing - UC:' + name, 'info', '6')
                        while True:
                            try:
                                with db.transaction('exclusive'):
                                    (UC(Registration_Number=registration_number,
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
                                     .save())
                            except peewee.OperationalError:
                                print('OperationalError')
                                time.sleep(5)
                            else:
                                break

                        for cert in cert_data:
                            if type(cert_data) == list:
                                for data in cert:
                                    if type(data) == dict:
                                        for var, dats in data.items():
                                            if var == 'keyid':
                                                key_id = dats
                                            if var == 'stamp':
                                                stamp = dats
                                            if var == 'serial':
                                                serial_number = dats
                                            if var == 'data':
                                                cert_base64 = dats

                                    if type(data) == list:
                                        for dats in data:
                                            url_crl = dats
                                            while True:
                                                try:
                                                    with db.transaction('exclusive'):
                                                        (CRL(Registration_Number=registration_number,
                                                             Name=name,
                                                             KeyId=key_id,
                                                             Stamp=stamp,
                                                             SerialNumber=serial_number,
                                                             UrlCRL=url_crl)
                                                         .save())
                                                except peewee.OperationalError:
                                                    print('OperationalError')
                                                    time.sleep(5)
                                                else:
                                                    break
                            while True:
                                try:
                                    with db.transaction('exclusive'):
                                        (CERT(Registration_Number=registration_number,
                                              Name=name,
                                              KeyId=key_id,
                                              Stamp=stamp,
                                              SerialNumber=serial_number,
                                              Data=cert_base64)
                                         .save())
                                except peewee.OperationalError:
                                    print('OperationalError')
                                    time.sleep(5)
                                else:
                                    break
                            crl_percent_step = int(math.floor(100 / (crl_count_all / crl_count)))
                            self.progressbar.emit(crl_percent_step)
                self.done_ver.emit(" Версия базы: " + current_version)
                self.done_date.emit(" Дата выпуска базы: " + last_update.replace('T', ' ').split('.')[0])
                self.done_all_uc.emit(" Всего УЦ: " + str(uc_count))
                self.done_all_cert.emit(" Всего Сертификатов: " + str(cert_count))
                self.done_all_crl.emit(" Всего CRL: " + str(crl_count))
                while True:
                    try:
                        with db.transaction('exclusive'):
                            Settings.update(value=current_version).where(Settings.name == 'ver').execute()
                    except peewee.OperationalError:
                        print('OperationalError')
                        time.sleep(5)
                    else:
                        break
                while True:
                    try:
                        with db.transaction('exclusive'):
                            Settings.update(value=last_update).where(Settings.name == 'data_update').execute()
                    except peewee.OperationalError:
                        print('OperationalError')
                        time.sleep(5)
                    else:
                        break
                self.current_uc.emit('Обработка завершена.')
                logs('Info: Processing successful done', 'info', '6')
        else:
            self.current_uc.emit('XML Файл не найден, необходимо скачать заново.')
            logs('Error: XML File not fount ' + self.fileName, 'errors', '2')
