from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QHeaderView
from PyQt5.QtGui import QIcon
from ui_sub_main import Ui_Form
from main_models import CRL, UC


class UcWindow(QWidget):
    def __init__(self, reg_number):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('assets/favicon.ico'))
        self.init(reg_number)

    def init(self, reg_number):

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
        self.setWindowIcon(QIcon('assets/favicon.ico'))

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

        for row in query:
            self.ui.tableWidget.setItem(count, 0, QTableWidgetItem(str(row.Registration_Number)))
            self.ui.tableWidget.setItem(count, 1, QTableWidgetItem(str(row.KeyId)))
            self.ui.tableWidget.setItem(count, 2, QTableWidgetItem(str(row.Stamp)))
            self.ui.tableWidget.setItem(count, 3, QTableWidgetItem(str(row.SerialNumber)))
            self.ui.tableWidget.setItem(count, 4, QTableWidgetItem(str(row.UrlCRL)))
            count = count + 1
        self.ui.tableWidget.setColumnWidth(0, 50)
        self.ui.tableWidget.setColumnWidth(1, 150)
        self.ui.tableWidget.setColumnWidth(2, 150)
        self.ui.tableWidget.setColumnWidth(3, 150)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(4, QHeaderView.Stretch)
