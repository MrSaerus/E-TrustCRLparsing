from PyQt5.QtGui import QIcon, QPixmap, QColor, QBrush, QTextCursor
from PyQt5.QtWidgets import QPushButton, QWidget, QTableWidgetItem, QHeaderView, QFileDialog, QMainWindow, QApplication
from PyQt5.Qt import Qt
from ui_main import Ui_MainWindow
from main_images import base64_import, base64_icon, base64_info, base64_inbox, base64_file, base64_export, \
     base64_diskette, base64_black_list, base64_white_list
from main_settings_system import set_value_in_property_file
from main_moduls import save_cert, get_info_xlm, export_all_watching_crl, \
     uc_sorting, cert_sorting, crl_sorting, watching_crl_sorting, watching_custom_crl_sorting, \
     watching_disabled_crl_sorting
from main_models import UC, CRL, CERT, WatchingCRL, WatchingCustomCRL, WatchingDeletedCRL, Settings
from class_main_worker import MainWorker
from class_main_downloader import MainDownloader
from class_main_cheker import MainChecker
from class_window_uc import UcWindow
from class_window_crl import CRLWindow
from class_window_crl_add import AddCRLWindow
from class_init_xml import InitXML
from class_main_watchdog import Watchdog
from main_log_system import logs
from main_settings import config
from asyncio import Queue
import shutil
import base64
import datetime
import os
import sys
import peewee
import time

if config['Logs']['dividelogsbyday'] == 'Yes':
    date_time_day = '_' + datetime.datetime.now().strftime('%Y%m%d')
else:
    date_time_day = ''


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        download_queue = Queue()
        sql_queue = Queue()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # base64_import
        # base64_icon
        # base64_info
        # base64_inbox
        # base64_file
        # base64_export
        # base64_diskette
        # base64_black_list
        # base64_white_list

        self.icon_import = QIcon()
        self.icon_icon = QIcon()
        self.icon_info = QIcon()
        self.icon_inbox = QIcon()
        self.icon_file = QIcon()
        self.icon_export = QIcon()
        self.icon_diskette = QIcon()
        self.icon_black_list = QIcon()
        self.icon_white_lis = QIcon()

        self.pixmap_import = QPixmap()
        self.pixmap_icon = QPixmap()
        self.pixmap_info = QPixmap()
        self.pixmap_inbox = QPixmap()
        self.pixmap_file = QPixmap()
        self.pixmap_export = QPixmap()
        self.pixmap_diskette = QPixmap()
        self.pixmap_black_list = QPixmap()
        self.pixmap_white_lis = QPixmap()

        self.pixmap_import.loadFromData(base64.b64decode(base64_import))
        self.pixmap_icon.loadFromData(base64.b64decode(base64_icon))
        self.pixmap_info.loadFromData(base64.b64decode(base64_info))
        self.pixmap_inbox.loadFromData(base64.b64decode(base64_inbox))
        self.pixmap_file.loadFromData(base64.b64decode(base64_file))
        self.pixmap_export.loadFromData(base64.b64decode(base64_export))
        self.pixmap_diskette.loadFromData(base64.b64decode(base64_diskette))
        self.pixmap_black_list.loadFromData(base64.b64decode(base64_black_list))
        self.pixmap_white_lis.loadFromData(base64.b64decode(base64_white_list))

        self.icon_import.addPixmap(self.pixmap_import)
        self.icon_icon.addPixmap(self.pixmap_icon)
        self.icon_info.addPixmap(self.pixmap_info)
        self.icon_inbox.addPixmap(self.pixmap_inbox)
        self.icon_file.addPixmap(self.pixmap_file)
        self.icon_export.addPixmap(self.pixmap_export)
        self.icon_diskette.addPixmap(self.pixmap_diskette)
        self.icon_black_list.addPixmap(self.pixmap_black_list)
        self.icon_white_lis.addPixmap(self.pixmap_white_lis)

        self.setWindowIcon(QIcon(self.icon_icon))
        self.window_uc = None
        self.window_crl = None
        self.window_add_crl = None

        self.ui.pushButton_7.pressed.connect(lambda: self.ui.lineEdit.setText(''))
        self.ui.pushButton_8.pressed.connect(lambda: self.ui.lineEdit_2.setText(''))
        self.ui.pushButton_9.pressed.connect(lambda: self.ui.lineEdit_3.setText(''))
        self.ui.pushButton_10.pressed.connect(lambda: self.ui.lineEdit_4.setText(''))
        self.ui.pushButton_11.pressed.connect(lambda: self.ui.lineEdit_5.setText(''))
        self.ui.pushButton_12.pressed.connect(lambda: self.ui.lineEdit_6.setText(''))

        self.tab_uc_sorting = 'asc'
        self.tab_cert_sorting = 'asc'
        self.tab_crl_sorting = 'asc'
        self.sub_tab_watching_crl_sorting = 'asc'
        self.sub_tab_watching_custom_crl_sorting = 'asc'
        self.sub_tab_watching_disabled_crl_sorting = 'asc'

        self.ui.pushButton_61.pressed.connect(lambda: self.tab_uc(self.ui.lineEdit.text(), 'Full_Name'))
        self.ui.pushButton_60.pressed.connect(lambda: self.tab_uc(self.ui.lineEdit.text(), 'INN'))
        self.ui.pushButton_59.pressed.connect(lambda: self.tab_uc(self.ui.lineEdit.text(), 'OGRN'))

        self.ui.pushButton_58.pressed.connect(lambda: self.tab_cert(self.ui.lineEdit_2.text(), 'Name'))
        self.ui.pushButton_57.pressed.connect(lambda: self.tab_cert(self.ui.lineEdit_2.text(), 'KeyId'))
        self.ui.pushButton_56.pressed.connect(lambda: self.tab_cert(self.ui.lineEdit_2.text(), 'Stamp'))
        self.ui.pushButton_55.pressed.connect(lambda: self.tab_cert(self.ui.lineEdit_2.text(), 'SerialNumber'))

        self.ui.pushButton_51.pressed.connect(lambda: self.tab_crl(self.ui.lineEdit_3.text(), 'Name'))
        self.ui.pushButton_50.pressed.connect(lambda: self.tab_crl(self.ui.lineEdit_3.text(), 'KeyId'))
        self.ui.pushButton_49.pressed.connect(lambda: self.tab_crl(self.ui.lineEdit_3.text(), 'Stamp'))
        self.ui.pushButton_48.pressed.connect(lambda: self.tab_crl(self.ui.lineEdit_3.text(), 'SerialNumber'))
        self.ui.pushButton_53.pressed.connect(lambda: self.tab_crl(self.ui.lineEdit_3.text(), 'UrlCRL'))

        self.ui.pushButton_29.pressed.connect(
            lambda: self.sub_tab_watching_crl(self.ui.lineEdit_4.text(), 'Name'))
        self.ui.pushButton_28.pressed.connect(
            lambda: self.sub_tab_watching_crl(self.ui.lineEdit_4.text(), 'OGRN'))
        self.ui.pushButton_24.pressed.connect(
            lambda: self.sub_tab_watching_crl(self.ui.lineEdit_4.text(), 'KeyId'))
        self.ui.pushButton_32.pressed.connect(
            lambda: self.sub_tab_watching_crl(self.ui.lineEdit_4.text(), 'UrlCRL'))
        self.ui.pushButton_31.pressed.connect(
            lambda: self.sub_tab_watching_crl(self.ui.lineEdit_4.text(), 'last_download'))
        self.ui.pushButton_30.pressed.connect(
            lambda: self.sub_tab_watching_crl(self.ui.lineEdit_4.text(), 'next_update'))

        self.ui.pushButton_37.pressed.connect(
            lambda: self.sub_tab_watching_custom_crl(self.ui.lineEdit_5.text(), 'Name'))
        self.ui.pushButton_36.pressed.connect(
            lambda: self.sub_tab_watching_custom_crl(self.ui.lineEdit_5.text(), 'OGRN'))
        self.ui.pushButton_35.pressed.connect(
            lambda: self.sub_tab_watching_custom_crl(self.ui.lineEdit_5.text(), 'KeyId'))
        self.ui.pushButton_34.pressed.connect(
            lambda: self.sub_tab_watching_custom_crl(self.ui.lineEdit_5.text(), 'UrlCRL'))
        self.ui.pushButton_40.pressed.connect(
            lambda: self.sub_tab_watching_custom_crl(self.ui.lineEdit_5.text(), 'last_download'))
        self.ui.pushButton_39.pressed.connect(
            lambda: self.sub_tab_watching_custom_crl(self.ui.lineEdit_5.text(), 'next_update'))

        self.ui.pushButton_44.pressed.connect(
            lambda: self.sub_tab_watching_disabled_crl(self.ui.lineEdit_6.text(), 'Name'))
        self.ui.pushButton_43.pressed.connect(
            lambda: self.sub_tab_watching_disabled_crl(self.ui.lineEdit_6.text(), 'OGRN'))
        self.ui.pushButton_42.pressed.connect(
            lambda: self.sub_tab_watching_disabled_crl(self.ui.lineEdit_6.text(), 'KeyId'))
        self.ui.pushButton_41.pressed.connect(
            lambda: self.sub_tab_watching_disabled_crl(self.ui.lineEdit_6.text(), 'Stamp'))
        self.ui.pushButton_47.pressed.connect(
            lambda: self.sub_tab_watching_disabled_crl(self.ui.lineEdit_6.text(), 'SerialNumber'))
        self.ui.pushButton_46.pressed.connect(
            lambda: self.sub_tab_watching_disabled_crl(self.ui.lineEdit_6.text(), 'UrlCRL'))

        self.ui.lineEdit.textChanged[str].connect(self.tab_uc)
        self.ui.lineEdit_2.textChanged[str].connect(self.tab_cert)
        self.ui.lineEdit_3.textChanged[str].connect(self.tab_crl)
        self.ui.lineEdit_4.textChanged[str].connect(self.sub_tab_watching_crl)
        self.ui.lineEdit_5.textChanged[str].connect(self.sub_tab_watching_custom_crl)
        self.ui.lineEdit_6.textChanged[str].connect(self.sub_tab_watching_disabled_crl)

        self.init_settings()
        self.tab_info()
        self.tab_uc()
        self.tab_cert()
        self.tab_crl()
        self.tab_watching_crl()
        self.sub_tab_watching_crl()
        self.sub_tab_watching_custom_crl()
        self.sub_tab_watching_disabled_crl()

        self.tab_uc_sorting = ''
        self.tab_cert_sorting = ''
        self.tab_crl_sorting = ''

        self.sub_tab_watching_crl_sorting = ''
        self.sub_tab_watching_custom_crl_sorting = ''
        self.sub_tab_watching_disabled_crl_sorting = ''

        self._squirrel = MainWorker('MainWorker')
        self._squirrel.threadTimerSender.connect(lambda y: self.ui.label_36.setText('Время в работе: ' + str(y)))
        self._squirrel.threadBefore.connect(
            lambda msg: self.ui.label_37.setText('Предыдущее обновление: ' + str(msg)))
        self._squirrel.threadAfter.connect(lambda msg: self.ui.label_38.setText('Следующее обновление: ' + str(msg)))
        self._squirrel.threadButtonStartD.connect(lambda: self.ui.pushButton_19.setDisabled(True))
        self._squirrel.threadButtonStopD.connect(lambda: self.ui.pushButton_20.setDisabled(True))
        self._squirrel.threadButtonStartE.connect(lambda: self.ui.pushButton_19.setEnabled(True))
        self._squirrel.threadButtonStopE.connect(lambda: self.ui.pushButton_20.setEnabled(True))
        self._squirrel.threadButtonStartD.connect(lambda: self.ui.pushButton.setDisabled(True))
        self._squirrel.threadButtonStartD.connect(lambda: self.ui.pushButton_2.setDisabled(True))
        self._squirrel.threadButtonStartD.connect(lambda: self.ui.pushButton_3.setDisabled(True))
        self._squirrel.threadButtonStartD.connect(lambda: self.ui.pushButton_4.setDisabled(True))
        self._squirrel.threadButtonStartD.connect(lambda: self.ui.pushButton_5.setDisabled(True))
        self._squirrel.threadButtonStopD.connect(lambda: self.ui.pushButton.setEnabled(True))
        self._squirrel.threadButtonStopD.connect(lambda: self.ui.pushButton_2.setEnabled(True))
        self._squirrel.threadButtonStopD.connect(lambda: self.ui.pushButton_3.setEnabled(True))
        self._squirrel.threadButtonStopD.connect(lambda: self.ui.pushButton_4.setEnabled(True))
        self._squirrel.threadButtonStopD.connect(lambda: self.ui.pushButton_5.setEnabled(True))

        self._squirrel.threadInfoMessage.connect(lambda msg: self.ui.label_7.setText(msg))
        self._squirrel.threadMessageSender.connect(lambda msg: print(msg))

        self._woof = Watchdog()
        self._woof.push.connect(lambda: self.ui.textBrowser.setText(
            open(config['Folders']['logs'] + '/log' + date_time_day + '.log', 'r').read()))
        self._woof.push.connect(lambda: self.ui.textBrowser_2.setText(
            open(config['Folders']['logs'] + '/error' + date_time_day + '.log', 'r').read()))
        self._woof.push.connect(lambda: self.ui.textBrowser_3.setText(
            open(config['Folders']['logs'] + '/download' + date_time_day + '.log', 'r').read()))
        self._woof.push.connect(lambda: self.ui.textBrowser.moveCursor(QTextCursor.End))
        self._woof.push.connect(lambda: self.ui.textBrowser_2.moveCursor(QTextCursor.End))
        self._woof.push.connect(lambda: self.ui.textBrowser_3.moveCursor(QTextCursor.End))

        self._checker = MainChecker('check_all')
        self._checker.current_message.connect(lambda msg: self.ui.label_8.setText(msg))
        self._checker.done.connect(lambda: self.ui.pushButton_3.setEnabled(True))
        self._checker.done.connect(lambda: self.ui.pushButton_4.setEnabled(True))
        self._checker.done.connect(lambda: self.ui.pushButton_5.setEnabled(True))

        self._down = MainDownloader('MainDownloader_main', 'all_mon')
        self._down.current_message.connect(lambda msg: self.ui.label_8.setText(msg))
        self._down.done.connect(lambda: self.ui.pushButton_3.setEnabled(True))
        self._down.done.connect(lambda: self.ui.pushButton_4.setEnabled(True))
        self._down.done.connect(lambda: self.ui.pushButton_5.setEnabled(True))
        self._down.download_message.connect(lambda msg: self.add_log_to_main_tab(msg))

        self._down_mon = MainDownloader('MainDownloader_main', 'mon')
        self._down_mon.current_message.connect(lambda msg: self.ui.label_8.setText(msg))
        self._down_mon.done.connect(lambda: self.ui.pushButton_3.setEnabled(True))
        self._down_mon.done.connect(lambda: self.ui.pushButton_4.setEnabled(True))
        self._down_mon.done.connect(lambda: self.ui.pushButton_5.setEnabled(True))
        self._down_mon.download_message.connect(lambda msg: self.add_log_to_main_tab(msg))

        self._init_xml = InitXML('tsl.xml')
        self._init_xml.progressbar.connect(lambda y: self.ui.progressBar_2.setValue(y))
        self._init_xml.current_uc.connect(lambda uc: self.ui.label_7.setText(uc))
        self._init_xml.done_ver.connect(lambda current_version: self.ui.label_3.setText(current_version))
        self._init_xml.done_date.connect(lambda last_update: self.ui.label_2.
                                         setText(last_update.replace('T', ' ').split('.')[0]))
        self._init_xml.done_all_uc.connect(lambda uc_count: self.ui.label.setText(str(uc_count)))
        self._init_xml.done_all_cert.connect(lambda cert_count: self.ui.label_4.setText(str(cert_count)))
        self._init_xml.done_all_crl.connect(lambda crl_count: self.ui.label_5.setText(str(crl_count)))
        self._init_xml.done_ver.connect(lambda: self.ui.pushButton.setEnabled(True))
        self._init_xml.done_ver.connect(lambda: self.ui.pushButton_2.setEnabled(True))
        self._init_xml.done_ver.connect(lambda: self.ui.progressBar_2.setMaximum(-1))
        self._init_xml.done_err.connect(lambda: self.ui.pushButton.setEnabled(True))
        self._init_xml.done_err.connect(lambda: self.ui.pushButton_2.setEnabled(True))
        self._init_xml.done_err.connect(lambda: self.ui.progressBar_2.setMaximum(-1))

        self._download = MainDownloader('MainDownloader_single_1',
                                        'single',
                                        'https://e-trust.gosuslugi.ru/CA/DownloadTSL?schemaVersion=0',
                                        'tsl.xml')
        self._download.stage_progress_total.connect(lambda x: self.ui.progressBar.setMaximum(x))
        self._download.stage_progress_current.connect(lambda y: self.ui.progressBar.setValue(y))
        self._download.current_message.connect(lambda z: self.ui.label_7.setText(z))
        self._download.done.connect(lambda: self.xml_check(get_info_xlm('current_version')))
        self._download.done.connect(lambda: self.ui.pushButton.setEnabled(True))
        self._download.done.connect(lambda: self.ui.pushButton_2.setEnabled(True))
        self._download.done_err.connect(lambda msg: self.ui.label_7.setText(msg))
        self._download.done_err.connect(lambda: self.ui.pushButton.setEnabled(True))
        self._download.done_err.connect(lambda: self.ui.pushButton_2.setEnabled(True))

    def tab_info(self):
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
        self.ui.label_6.setText(" Мониторится CRL: "
                                + str(int(watching_crl.count())
                                      + int(watching_custom_crl.count())))
        self.ui.pushButton.clicked.connect(self.xml_download)
        self.ui.pushButton.setToolTip('Скачать TSL')
        self.ui.pushButton_2.clicked.connect(self.xml_init)
        self.ui.pushButton_2.setToolTip('Обработать TSL')
        self.ui.pushButton_13.clicked.connect(self.export_crl)
        self.ui.pushButton_13.setToolTip('Экспортировать список CRL')
        self.ui.pushButton_6.pressed.connect(self.import_crl_list)
        self.ui.pushButton_6.setToolTip('Импортировать список CRL')

        watching_crl = WatchingCRL.select().order_by(WatchingCRL.next_update).where(
            WatchingCRL.OGRN == config['Update']['main_uc_ogrn'])
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
            WatchingCRL.OGRN == config['Update']['self_uc_ogrn'])
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

        self.ui.tableWidget_9.setRowCount(1)
        self.ui.tableWidget_9.setItem(0, 1, QTableWidgetItem('Info: init log system'))
        self.ui.tableWidget_9.setColumnWidth(0, 23)
        self.ui.tableWidget_9.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.ui.pushButton_20.clicked.connect(self.main_worker_stop)
        self.ui.pushButton_20.setToolTip('Остановить мониторинг CRL')
        self.ui.pushButton_19.clicked.connect(self.main_worker)
        self.ui.pushButton_19.setToolTip('Запустить мониторинг CRL')

    def tab_uc(self, text='', order_by='Full_Name'):
        self.tab_uc_sorting = order_by

        order = uc_sorting(order_by)
        self.ui.tableWidget.clearContents()
        query = UC.select().order_by(order).where(UC.Registration_Number.contains(text)
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
            self.ui.tableWidget.setItem(count, 0, QTableWidgetItem(str(row.Full_Name)))
            self.ui.tableWidget.setItem(count, 1, QTableWidgetItem(str(row.INN)))
            self.ui.tableWidget.setItem(count, 2, QTableWidgetItem(str(row.OGRN)))

            button_info = QPushButton()
            button_info.setFixedSize(30, 30)
            button_info.setIcon(self.icon_info)
            button_info.setFlat(True)
            reg_num = row.Registration_Number
            button_info.pressed.connect(lambda rg=reg_num: self.open_sub_window_info_uc(rg))
            button_info.setToolTip('Подробная информация по УЦ')
            self.ui.tableWidget.setCellWidget(count, 3, button_info)
            count = count + 1
        self.ui.tableWidget.resizeColumnsToContents()
        self.ui.tableWidget.setColumnWidth(1, 100)
        self.ui.tableWidget.setColumnWidth(2, 100)
        self.ui.tableWidget.setColumnWidth(3, 31)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)

    def tab_cert(self, text='', order_by='Name'):
        self.tab_cert_sorting = order_by

        order = cert_sorting(order_by)
        self.ui.tableWidget_2.clearContents()
        self.ui.pushButton_22.setIcon(self.icon_file)
        self.ui.pushButton_22.setFlat(True)
        self.ui.pushButton_22.pressed.connect(lambda: os.startfile(os.path.realpath(config['Folders']['certs'])))
        self.ui.pushButton_22.setToolTip('Открыть папку с сертами')

        query = CERT.select().order_by(order).where(CERT.Registration_Number.contains(text)
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
            self.ui.tableWidget_2.setItem(count, 0, QTableWidgetItem(str(row.Name)))
            self.ui.tableWidget_2.setItem(count, 1, QTableWidgetItem(str(row.KeyId)))
            self.ui.tableWidget_2.setItem(count, 2, QTableWidgetItem(str(row.Stamp)))
            self.ui.tableWidget_2.setItem(count, 3, QTableWidgetItem(str(row.SerialNumber)))

            button_cert = QPushButton()
            button_cert.setFixedSize(30, 30)

            button_cert.setIcon(self.icon_diskette)
            button_cert.setFlat(True)
            ki = row.KeyId
            # button_cert.pressed.connect(lambda key_id=ki: open_file(key_id, "cer"))
            button_cert.pressed.connect(lambda key_id=ki: save_cert(key_id, config['Folders']['certs']))
            button_cert.setToolTip('Сохранить сертификат')
            self.ui.tableWidget_2.setCellWidget(count, 4, button_cert)

            button_cert_save = QPushButton()
            button_cert_save.setFixedSize(30, 30)
            button_cert_save.setIcon(self.icon_inbox)
            button_cert_save.setFlat(True)
            ki = row.KeyId
            button_cert_save.pressed.connect(lambda key_id=ki: save_cert(key_id, config['Folders']['to_uc']))
            button_cert_save.setToolTip('Сохранить сертификат в папку УЦ')
            self.ui.tableWidget_2.setCellWidget(count, 5, button_cert_save)
            count = count + 1
        self.ui.tableWidget_2.setColumnWidth(1, 150)
        self.ui.tableWidget_2.setColumnWidth(2, 150)
        self.ui.tableWidget_2.setColumnWidth(3, 150)
        self.ui.tableWidget_2.setColumnWidth(4, 31)
        self.ui.tableWidget_2.setColumnWidth(5, 31)
        self.ui.tableWidget_2.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)

    def tab_crl(self, text='', order_by='Full_Name'):
        self.tab_crl_sorting = order_by

        order = crl_sorting(order_by)
        self.ui.tableWidget_3.clearContents()
        self.ui.pushButton_26.setIcon(self.icon_file)
        self.ui.pushButton_26.setFlat(True)
        self.ui.pushButton_26.pressed.connect(lambda: os.startfile(os.path.realpath(config['Folders']['crls'])))
        self.ui.pushButton_26.setToolTip('Открыть папку с CRL')

        query = CRL.select().order_by(order).where(CRL.Registration_Number.contains(text)
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
            self.ui.tableWidget_3.setItem(count, 0, QTableWidgetItem(str(row.Name)))
            self.ui.tableWidget_3.setItem(count, 1, QTableWidgetItem(str(row.KeyId)))
            self.ui.tableWidget_3.setItem(count, 2, QTableWidgetItem(str(row.Stamp)))
            self.ui.tableWidget_3.setItem(count, 3, QTableWidgetItem(str(row.SerialNumber)))
            self.ui.tableWidget_3.setItem(count, 4, QTableWidgetItem(str(row.UrlCRL)))
            button_crl_save = QPushButton()
            button_crl_save.setFixedSize(30, 30)
            button_crl_save.setIcon(self.icon_diskette)
            button_crl_save.setFlat(True)
            button_crl_save.pressed.connect(
                lambda u=row.UrlCRL, s=row.KeyId: self.download_file(u, s + '.crl', config['Folders']['crls']))
            button_crl_save.setToolTip('Сохранить CRL')
            self.ui.tableWidget_3.setCellWidget(count, 5, button_crl_save)

            button_crl_save_to_uc = QPushButton()
            button_crl_save_to_uc.setFixedSize(30, 30)
            button_crl_save_to_uc.setIcon(self.icon_inbox)
            button_crl_save_to_uc.setFlat(True)
            button_crl_save_to_uc.pressed.connect(
                lambda u=row.UrlCRL, s=row.KeyId: self.download_file(u, s + '.crl', config['Folders']['to_uc']))
            button_crl_save_to_uc.setToolTip('Сохранить CRL в УЦ')
            self.ui.tableWidget_3.setCellWidget(count, 6, button_crl_save_to_uc)

            button_add_to_watch = QPushButton()
            button_add_to_watch.setFixedSize(30, 30)
            button_add_to_watch.setIcon(self.icon_import)
            button_add_to_watch.setFlat(True)
            rb = row.Registration_Number
            ki = row.KeyId
            st = row.Stamp
            sn = row.SerialNumber
            uc = row.UrlCRL
            button_add_to_watch.pressed.connect(lambda registration_number=rb,
                                                keyid=ki,
                                                stamp=st,
                                                serial_number=sn,
                                                url_crl=uc: self.add_watch_current_crl(registration_number,
                                                                                       keyid,
                                                                                       stamp,
                                                                                       serial_number,
                                                                                       url_crl))
            button_add_to_watch.setToolTip('Добавить CRL в мониторинг')
            self.ui.tableWidget_3.setCellWidget(count, 7, button_add_to_watch)
            count = count + 1
        self.ui.tableWidget_3.setColumnWidth(1, 150)
        self.ui.tableWidget_3.setColumnWidth(2, 150)
        self.ui.tableWidget_3.setColumnWidth(3, 150)
        self.ui.tableWidget_3.setColumnWidth(4, 150)
        self.ui.tableWidget_3.setColumnWidth(5, 31)
        self.ui.tableWidget_3.setColumnWidth(6, 31)
        self.ui.tableWidget_3.setColumnWidth(7, 31)
        self.ui.tableWidget_3.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)

    def tab_watching_crl(self):
        self.ui.pushButton_4.pressed.connect(lambda: self.downloader())
        self.ui.pushButton_4.setToolTip('Скачать все CRL (Занимает значительное время при использовании прокси)')
        self.ui.pushButton_5.clicked.connect(lambda: self.checker())
        self.ui.pushButton_5.setToolTip('Запустить проверку всех CRL ')
        self.ui.pushButton_3.clicked.connect(lambda: self.down_mon())
        self.ui.pushButton_3.setToolTip('Проверить наличие ноых CRL для скачивания и копирования в УЦ')
        self.ui.pushButton_27.setIcon(self.icon_file)
        self.ui.pushButton_27.setFlat(True)
        self.ui.pushButton_27.pressed.connect(lambda: os.startfile(os.path.realpath(config['Folders']['crls'])))
        self.ui.pushButton_27.setToolTip('Открыть папку с CRL')

    def sub_tab_watching_crl(self, text='', order_by='Full_Name', orders='Yes'):
        self.sub_tab_watching_crl_sorting = order_by

        order = watching_crl_sorting(order_by, orders)
        self.ui.tableWidget_4.clearContents()

        query = WatchingCRL.select().order_by(order).where(WatchingCRL.Name.contains(text)
                                                           | WatchingCRL.INN.contains(text)
                                                           | WatchingCRL.OGRN.contains(text)
                                                           | WatchingCRL.KeyId.contains(text)
                                                           | WatchingCRL.Stamp.contains(text)
                                                           | WatchingCRL.SerialNumber.contains(text)
                                                           | WatchingCRL.UrlCRL.contains(text)). \
            limit(config['Listing']['watch'])
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
            self.ui.tableWidget_4.setItem(count, 1, QTableWidgetItem(str(row.KeyId)))
            self.ui.tableWidget_4.setItem(count, 2, QTableWidgetItem(str(row.UrlCRL)))
            self.ui.tableWidget_4.setItem(count, 3, QTableWidgetItem(str(row.last_update)))
            self.ui.tableWidget_4.setItem(count, 4, QTableWidgetItem(str(row.last_download)))
            self.ui.tableWidget_4.setItem(count, 5, QTableWidgetItem(str(row.next_update)))

            if row.status == 'Info: Filetype good':
                status_item = QTableWidgetItem()
                status_item.setIcon(self.icon_white_lis)
                status_item.setToolTip('Файл прошел проверку')
                self.ui.tableWidget_4.setItem(count, 6, status_item)
            else:
                status_item_2 = QTableWidgetItem()
                status_item_2.setIcon(self.icon_black_list)
                status_item_2.setToolTip('Ошибка в файле или не скачан')
                self.ui.tableWidget_4.setItem(count, 6, status_item_2)

            button_crl_to_uc = QPushButton()
            button_crl_to_uc.setFixedSize(30, 30)
            button_crl_to_uc.setIcon(self.icon_inbox)
            button_crl_to_uc.setFlat(True)
            row_key_id = row.KeyId
            row_url_crl = row.UrlCRL
            button_crl_to_uc.pressed.connect(lambda rki=row_key_id, url=row_url_crl: self.copy_crl_to_uc(rki, url))
            button_crl_to_uc.setToolTip('Копировать CRL в УЦ')
            self.ui.tableWidget_4.setCellWidget(count, 7, button_crl_to_uc)

            button_down_crl_to_uc = QPushButton()
            button_down_crl_to_uc.setFixedSize(30, 30)
            button_down_crl_to_uc.setIcon(self.icon_inbox)
            button_down_crl_to_uc.setFlat(True)
            row_key_id = row.KeyId
            row_url_crl = row.UrlCRL
            row_id_w = row.ID
            button_down_crl_to_uc.pressed.connect(lambda rki=row_key_id, url=row_url_crl, id_w=row_id_w:
                                                  self.download_file(url,
                                                                     rki + '.crl',
                                                                     config['Folders']['crls'],
                                                                     'current',
                                                                     id_w))
            button_down_crl_to_uc.setToolTip('Скачать CRL в УЦ')
            self.ui.tableWidget_4.setCellWidget(count, 8, button_down_crl_to_uc)

            button_delete_watch = QPushButton()
            button_delete_watch.setFixedSize(30, 30)
            button_delete_watch.setIcon(self.icon_export)
            button_delete_watch.setFlat(True)
            id_row = row.ID
            id_table_row = count
            button_delete_watch.pressed.connect(lambda o=id_row, idt=id_table_row: self.move_watching_to_passed(o, 'current', idt))
            button_delete_watch.setToolTip('Убрать CRL из мониторинга')
            self.ui.tableWidget_4.setCellWidget(count, 9, button_delete_watch)
            count = count + 1
        self.ui.tableWidget_4.setColumnWidth(1, 150)
        self.ui.tableWidget_4.setColumnWidth(2, 150)
        self.ui.tableWidget_4.setColumnWidth(3, 150)
        self.ui.tableWidget_4.setColumnWidth(4, 150)
        self.ui.tableWidget_4.setColumnWidth(5, 150)
        self.ui.tableWidget_4.setColumnWidth(6, 25)
        self.ui.tableWidget_4.setColumnWidth(7, 31)
        self.ui.tableWidget_4.setColumnWidth(8, 31)
        self.ui.tableWidget_4.setColumnWidth(9, 31)
        self.ui.tableWidget_4.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)

    def sub_tab_watching_custom_crl(self, text='', order_by='Full_Name', orders='Yes'):
        self.sub_tab_watching_custom_crl_sorting = order_by

        order = watching_custom_crl_sorting(order_by, orders)
        self.ui.tableWidget_5.clearContents()
        self.ui.pushButton_25.pressed.connect(lambda: self.open_sub_window_add())
        query = WatchingCustomCRL.select().order_by(order) \
            .where(WatchingCustomCRL.Name.contains(text)
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
        # self.ui.tableWidget_5.clear()
        self.ui.tableWidget_5.setRowCount(count_all)
        count = 0
        for row in query:
            self.ui.tableWidget_5.setItem(count, 0, QTableWidgetItem(str(row.Name)))
            self.ui.tableWidget_5.setItem(count, 1, QTableWidgetItem(str(row.KeyId)))
            self.ui.tableWidget_5.setItem(count, 2, QTableWidgetItem(str(row.UrlCRL)))
            self.ui.tableWidget_5.setItem(count, 3, QTableWidgetItem(str(row.last_update)))
            self.ui.tableWidget_5.setItem(count, 4, QTableWidgetItem(str(row.last_download)))
            self.ui.tableWidget_5.setItem(count, 5, QTableWidgetItem(str(row.next_update)))

            if row.status == 'Info: Filetype good':
                status_item = QTableWidgetItem()
                status_item.setIcon(self.icon_white_lis)
                status_item.setToolTip('Файл прошел проверку')
                self.ui.tableWidget_5.setItem(count, 6, status_item)
            else:
                status_item_2 = QTableWidgetItem()
                status_item_2.setIcon(self.icon_black_list)
                status_item_2.setToolTip('Ошибка в файле или не скачан')
                self.ui.tableWidget_5.setItem(count, 6, status_item_2)

            button_crl_to_uc = QPushButton()
            button_crl_to_uc.setFixedSize(30, 30)
            button_crl_to_uc.setIcon(self.icon_inbox)
            button_crl_to_uc.setFlat(True)
            row_key_id = row.KeyId
            row_url_crl = row.UrlCRL
            button_crl_to_uc.pressed.connect(lambda rki=row_key_id, url=row_url_crl: self.copy_crl_to_uc(rki, url))
            button_crl_to_uc.setToolTip('Копировать CRL в УЦ')
            self.ui.tableWidget_5.setCellWidget(count, 7, button_crl_to_uc)

            button_down_crl_to_uc = QPushButton()
            button_down_crl_to_uc.setFixedSize(30, 30)
            button_down_crl_to_uc.setIcon(self.icon_inbox)
            button_down_crl_to_uc.setFlat(True)
            row_key_id = row.KeyId
            row_url_crl = row.UrlCRL
            row_id_wc = row.ID
            button_down_crl_to_uc.pressed.connect(lambda rki=row_key_id, url=row_url_crl, id_wc=row_id_wc:
                                                  self.download_file(url,
                                                                     rki + '.crl',
                                                                     config['Folders']['crls'],
                                                                     'custom',
                                                                     id_wc))
            button_down_crl_to_uc.setToolTip('Скачать CRL в УЦ')
            self.ui.tableWidget_5.setCellWidget(count, 8, button_down_crl_to_uc)

            button_delete_watch = QPushButton()
            button_delete_watch.setFixedSize(30, 30)
            button_delete_watch.setIcon(self.icon_export)
            button_delete_watch.setFlat(True)
            id_row = row.ID
            id_table_row = count
            button_delete_watch.pressed.connect(lambda o=id_row, idt=id_table_row: self.move_watching_to_passed(o, 'custom', idt))
            button_delete_watch.setToolTip('Убрать CRL из мониторинга')
            self.ui.tableWidget_5.setCellWidget(count, 9, button_delete_watch)

            count = count + 1
        self.ui.tableWidget_5.setColumnWidth(1, 150)
        self.ui.tableWidget_5.setColumnWidth(2, 150)
        self.ui.tableWidget_5.setColumnWidth(3, 150)
        self.ui.tableWidget_5.setColumnWidth(4, 150)
        self.ui.tableWidget_5.setColumnWidth(4, 150)
        self.ui.tableWidget_5.setColumnWidth(5, 150)
        self.ui.tableWidget_5.setColumnWidth(6, 25)
        self.ui.tableWidget_5.setColumnWidth(7, 31)
        self.ui.tableWidget_5.setColumnWidth(8, 31)
        self.ui.tableWidget_5.setColumnWidth(9, 31)
        self.ui.tableWidget_5.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)

    def sub_tab_watching_disabled_crl(self, text='', order_by='Full_Name', orders='Yes'):
        self.sub_tab_watching_disabled_crl_sorting = order_by

        order = watching_disabled_crl_sorting(order_by, orders)
        self.ui.tableWidget_6.clearContents()
        query = WatchingDeletedCRL.select().order_by(order). \
            where(WatchingDeletedCRL.Name.contains(text)
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
            self.ui.tableWidget_6.setItem(count, 1, QTableWidgetItem(str(row.OGRN)))
            self.ui.tableWidget_6.setItem(count, 2, QTableWidgetItem(str(row.KeyId)))
            self.ui.tableWidget_6.setItem(count, 3, QTableWidgetItem(str(row.Stamp)))
            self.ui.tableWidget_6.setItem(count, 4, QTableWidgetItem(str(row.SerialNumber)))
            self.ui.tableWidget_6.setItem(count, 5, QTableWidgetItem(str(row.UrlCRL)))

            button_return_watch = QPushButton()
            button_return_watch.setFixedSize(30, 30)
            button_return_watch.setIcon(self.icon_import)
            button_return_watch.setFlat(True)
            id_row = row.ID
            button_return_watch.pressed.connect(lambda o=id_row: self.move_passed_to_watching(o))
            button_return_watch.setToolTip('Вернуть CRL в мониторинг')
            self.ui.tableWidget_6.setCellWidget(count, 6, button_return_watch)
            count = count + 1

        self.ui.tableWidget_6.setColumnWidth(1, 100)
        self.ui.tableWidget_6.setColumnWidth(2, 150)
        self.ui.tableWidget_6.setColumnWidth(3, 150)
        self.ui.tableWidget_6.setColumnWidth(4, 150)
        self.ui.tableWidget_6.setColumnWidth(5, 150)
        self.ui.tableWidget_6.setColumnWidth(6, 31)
        self.ui.tableWidget_6.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)

    def init_settings(self):
        # main config
        self.ui.lineEdit_13.setText(config['Tabs']['ucLimit'])
        self.ui.lineEdit_18.setText(config['Tabs']['certLimit'])
        self.ui.lineEdit_17.setText(config['Tabs']['crlLimit'])
        self.ui.lineEdit_16.setText(config['Tabs']['wcLimit'])
        self.ui.lineEdit_15.setText(config['Tabs']['wccLimit'])
        self.ui.lineEdit_14.setText(config['Tabs']['wcdLimit'])
        self.ui.lineEdit_19.setText(config['XMPP']['server'])
        self.ui.lineEdit_20.setText(config['XMPP']['login'])
        self.ui.lineEdit_21.setText(config['XMPP']['password'])
        self.ui.lineEdit_22.setText(config['XMPP']['tosend'])
        self.ui.lineEdit_23.setText(config['Update']['deltaupdateinday'])
        self.ui.lineEdit_24.setText(config['Update']['timebeforeupdate'])
        self.ui.lineEdit_25.setText(config['Update']['self_uc_ogrn'])
        self.ui.lineEdit_26.setText(config['Update']['main_uc_ogrn'])

        if config['XMPP']['sendinfoerr'] == 'Yes':
            self.ui.checkBox_10.setChecked(True)
        if config['XMPP']['sendinfonewcrl'] == 'Yes':
            self.ui.checkBox_9.setChecked(True)
        if config['XMPP']['sendinfonewtsl'] == 'Yes':
            self.ui.checkBox_11.setChecked(True)

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

        # Sub  config
        self.ui.lineEdit_12.setText(config['MainWindow']['height'])
        self.ui.lineEdit_11.setText(config['MainWindow']['width'])
        self.resize(int(config['MainWindow']['width']), int(config['MainWindow']['height']))
        if config['MainWindow']['savewidth'] == 'No':
            self.ui.checkBox_2.setChecked(True)
        if config['MainWindow']['allowresize'] == 'Yes':
            self.ui.checkBox_3.setChecked(True)
            self.resize(int(config['MainWindow']['width']), int(config['MainWindow']['height']))
            self.setMinimumSize(int(config['MainWindow']['width']), int(config['MainWindow']['height']))
            self.setMaximumSize(int(config['MainWindow']['width']), int(config['MainWindow']['height']))

        self.ui.comboBox.setCurrentText(config['Logs']['loglevel'])
        self.ui.spinBox.setValue(int(config['Logs']['dividelogsbysize']))
        if config['Logs']['dividelogsbyday'] == 'Yes':
            self.ui.checkBox_14.setChecked(True)
        if config['Schedule']['allowupdatecrlbystart'] == 'Yes':
            self.ui.checkBox_12.setChecked(True)
        if config['Schedule']['allowupdatetslbystart'] == 'Yes':
            self.ui.checkBox_13.setChecked(True)
        if config['Schedule']['allowmonitoringcrlbystart'] == 'Yes':
            self.ui.checkBox_15.setChecked(True)
        else:
            self.ui.pushButton_20.setDisabled(True)
        # download config
        self.ui.label_13.setText(config['Folders']['crls'])
        self.ui.label_12.setText(config['Folders']['certs'])
        self.ui.label_11.setText(config['Folders']['uc'])
        self.ui.label_10.setText(config['Folders']['tmp'])
        self.ui.label_9.setText(config['Folders']['to_uc'])

        self.ui.pushButton_18.clicked.connect(lambda: self.choose_directory('crl'))
        self.ui.pushButton_18.setToolTip('Папка загрузки CRL')
        self.ui.pushButton_17.clicked.connect(lambda: self.choose_directory('cert'))
        self.ui.pushButton_17.setToolTip('Папка загрузки сертификатов')
        self.ui.pushButton_16.clicked.connect(lambda: self.choose_directory('uc'))
        self.ui.pushButton_16.setToolTip('Папка загрузки данных УЦ')
        self.ui.pushButton_15.clicked.connect(lambda: self.choose_directory('tmp'))
        self.ui.pushButton_15.setToolTip('Папка загрузки временныйх файлов программы')
        self.ui.pushButton_14.clicked.connect(lambda: self.choose_directory('to_uc'))
        self.ui.pushButton_14.setToolTip('Папка загрузки в УЦ')

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
        if config['Logs']['dividelogsbyday'] == 'Yes':
            date_time_day = '_' + datetime.datetime.now().strftime('%Y%m%d')
        else:
            date_time_day = ''
        if os.path.exists(config['Folders']['logs'] + '/log' + date_time_day + '.log'):
            self.ui.textBrowser.setText(
                open(config['Folders']['logs'] + '/log' + date_time_day + '.log', 'r').read())

        if os.path.exists(config['Folders']['logs'] + '/error' + date_time_day + '.log'):
            self.ui.textBrowser_2.setText(
                open(config['Folders']['logs'] + '/error' + date_time_day + '.log', 'r').read())

        if os.path.exists(config['Folders']['logs'] + '/download' + date_time_day + '.log'):
            self.ui.textBrowser_3.setText(
                open(config['Folders']['logs'] + '/download' + date_time_day + '.log', 'r').read())

        self.ui.pushButton_21.pressed.connect(lambda: self.save_settings_main())
        self.ui.pushButton_23.pressed.connect(lambda: self.save_settings_sub())

    def save_settings_main(self):
        set_value_in_property_file('settings.ini', 'Tabs', 'ucLimit', self.ui.lineEdit_13.text(), config)
        config.set('Tabs', 'ucLimit', self.ui.lineEdit_13.text())
        set_value_in_property_file('settings.ini', 'Tabs', 'certLimit', self.ui.lineEdit_18.text(), config)
        config.set('Tabs', 'certLimit', self.ui.lineEdit_18.text())
        set_value_in_property_file('settings.ini', 'Tabs', 'crlLimit', self.ui.lineEdit_17.text(), config)
        config.set('Tabs', 'crlLimit', self.ui.lineEdit_17.text())
        set_value_in_property_file('settings.ini', 'Tabs', 'wcLimit', self.ui.lineEdit_16.text(), config)
        config.set('Tabs', 'wcLimit', self.ui.lineEdit_16.text())
        set_value_in_property_file('settings.ini', 'Tabs', 'wccLimit', self.ui.lineEdit_15.text(), config)
        config.set('Tabs', 'wccLimit', self.ui.lineEdit_15.text())
        set_value_in_property_file('settings.ini', 'Tabs', 'wcdLimit', self.ui.lineEdit_14.text(), config)
        config.set('Tabs', 'wcdLimit', self.ui.lineEdit_14.text())
        set_value_in_property_file('settings.ini', 'MainWindow', 'height', self.ui.lineEdit_12.text(), config)
        config.set('MainWindow', 'height', self.ui.lineEdit_12.text())
        set_value_in_property_file('settings.ini', 'MainWindow', 'width', self.ui.lineEdit_11.text(), config)
        config.set('MainWindow', 'width', self.ui.lineEdit_11.text())
        set_value_in_property_file('settings.ini', 'XMPP', 'server', self.ui.lineEdit_19.text(), config)
        config.set('XMPP', 'server', self.ui.lineEdit_19.text())
        set_value_in_property_file('settings.ini', 'XMPP', 'login', self.ui.lineEdit_20.text(), config)
        config.set('XMPP', 'login', self.ui.lineEdit_20.text())
        set_value_in_property_file('settings.ini', 'XMPP', 'password', self.ui.lineEdit_21.text(), config)
        config.set('XMPP', 'password', self.ui.lineEdit_21.text())
        set_value_in_property_file('settings.ini', 'XMPP', 'tosend', self.ui.lineEdit_22.text(), config)
        config.set('XMPP', 'tosend', self.ui.lineEdit_22.text())
        set_value_in_property_file('settings.ini', 'Update', 'deltaupdateinday', self.ui.lineEdit_23.text(), config)
        config.set('Update', 'deltaupdateinday', self.ui.lineEdit_23.text())
        set_value_in_property_file('settings.ini', 'Update', 'timebeforeupdate', self.ui.lineEdit_24.text(), config)
        config.set('Update', 'timebeforeupdate', self.ui.lineEdit_24.text())

        if self.ui.checkBox_10.checkState() == 0:
            set_value_in_property_file('settings.ini', 'XMPP', 'sendinfoerr', 'No', config)
            config.set('XMPP', 'sendinfoerr', 'No')
        elif self.ui.checkBox_10.checkState() == 2:
            set_value_in_property_file('settings.ini', 'XMPP', 'sendinfoerr', 'Yes', config)
            config.set('XMPP', 'sendinfoerr', 'Yes')
        if self.ui.checkBox_9.checkState() == 0:
            set_value_in_property_file('settings.ini', 'XMPP', 'sendinfonewcrl', 'No', config)
            config.set('XMPP', 'sendinfonewcrl', 'No')
        elif self.ui.checkBox_9.checkState() == 2:
            set_value_in_property_file('settings.ini', 'XMPP', 'sendinfonewcrl', 'Yes', config)
            config.set('XMPP', 'sendinfonewcrl', 'Yes')
        if self.ui.checkBox_11.checkState() == 0:
            set_value_in_property_file('settings.ini', 'XMPP', 'sendinfonewtsl', 'No', config)
            config.set('XMPP', 'sendinfonewtsl', 'No')
        elif self.ui.checkBox_11.checkState() == 2:
            set_value_in_property_file('settings.ini', 'XMPP', 'sendinfonewtsl', 'Yes', config)
            config.set('XMPP', 'sendinfonewtsl', 'Yes')

        set_value_in_property_file('settings.ini', 'Proxy', 'ip', self.ui.lineEdit_7.text(), config)
        config['Proxy']['ip'] = self.ui.lineEdit_7.text()
        config.set('Proxy', 'ip', self.ui.lineEdit_7.text())
        set_value_in_property_file('settings.ini', 'Proxy', 'port', self.ui.lineEdit_8.text(), config)
        config['Proxy']['port'] = self.ui.lineEdit_8.text()
        config.set('Proxy', 'port', self.ui.lineEdit_8.text())
        set_value_in_property_file('settings.ini', 'Proxy', 'login', self.ui.lineEdit_9.text(), config)
        config['Proxy']['login'] = self.ui.lineEdit_9.text()
        config.set('Proxy', 'login', self.ui.lineEdit_9.text())
        set_value_in_property_file('settings.ini', 'Proxy', 'password', self.ui.lineEdit_10.text(), config)
        config['Proxy']['password'] = self.ui.lineEdit_10.text()
        config.set('Proxy', 'password', self.ui.lineEdit_10.text())

        if self.ui.checkBox.checkState() == 0:
            set_value_in_property_file('settings.ini', 'Proxy', 'proxyon', 'No', config)
            config.set('Proxy', 'proxyon', 'No')
            self.ui.lineEdit_7.setDisabled(True)
            self.ui.lineEdit_8.setDisabled(True)
            self.ui.lineEdit_9.setDisabled(True)
            self.ui.lineEdit_10.setDisabled(True)
        elif self.ui.checkBox.checkState() == 2:
            set_value_in_property_file('settings.ini', 'Proxy', 'proxyon', 'Yes', config)
            config.set('Proxy', 'proxyon', 'Yes')
            self.ui.lineEdit_7.setEnabled(True)
            self.ui.lineEdit_8.setEnabled(True)
            self.ui.lineEdit_9.setEnabled(True)
            self.ui.lineEdit_10.setEnabled(True)

        if self.ui.checkBox_3.checkState() == 0:
            set_value_in_property_file('settings.ini', 'MainWindow', 'allowresize', 'No', config)
            config.set('MainWindow', 'allowresize', 'Yes')
            self.resize(int(config['MainWindow']['width']), int(config['MainWindow']['height']))
            self.setMinimumSize(0, 0)
            self.setMaximumSize(16777215, 16777215)
        elif self.ui.checkBox_3.checkState() == 2:
            set_value_in_property_file('settings.ini', 'MainWindow', 'allowresize', 'Yes', config)
            config.set('MainWindow', 'allowresize', 'No')
            self.resize(int(config['MainWindow']['width']), int(config['MainWindow']['height']))
            self.setMinimumSize(int(config['MainWindow']['width']), int(config['MainWindow']['height']))
            self.setMaximumSize(int(config['MainWindow']['width']), int(config['MainWindow']['height']))

        if self.ui.checkBox_2.checkState() == 0:
            set_value_in_property_file('settings.ini', 'MainWindow', 'savewidth', 'Yes', config)
            config.set('MainWindow', 'savewidth', 'No')
        elif self.ui.checkBox_2.checkState() == 2:
            set_value_in_property_file('settings.ini', 'MainWindow', 'savewidth', 'No', config)
            config.set('MainWindow', 'savewidth', 'Yes')

        if self.ui.checkBox_4.checkState() == 0:
            set_value_in_property_file('settings.ini', 'Sec', 'allowImportCRL', 'No', config)
            config.set('Sec', 'allowImportCRL', 'No')
            self.ui.pushButton_6.setDisabled(True)
        elif self.ui.checkBox_4.checkState() == 2:
            set_value_in_property_file('settings.ini', 'Sec', 'allowImportCRL', 'Yes', config)
            config.set('Sec', 'allowImportCRL', 'Yes')
            self.ui.pushButton_6.setEnabled(True)
        if self.ui.checkBox_5.checkState() == 0:
            set_value_in_property_file('settings.ini', 'Sec', 'allowExportCRL', 'No', config)
            config.set('Sec', 'allowExportCRL', 'No')
            self.ui.pushButton_13.setDisabled(True)
        elif self.ui.checkBox_5.checkState() == 2:
            set_value_in_property_file('settings.ini', 'Sec', 'allowExportCRL', 'Yes', config)
            config.set('Sec', 'allowExportCRL', 'Yes')
            self.ui.pushButton_13.setEnabled(True)
        if self.ui.checkBox_6.checkState() == 0:
            set_value_in_property_file('settings.ini', 'Sec', 'allowDeleteWatchingCRL', 'No', config)
            config.set('Sec', 'allowDeleteWatchingCRL', 'No')
        elif self.ui.checkBox_6.checkState() == 2:
            set_value_in_property_file('settings.ini', 'Sec', 'allowDeleteWatchingCRL', 'Yes', config)
            config.set('Sec', 'allowDeleteWatchingCRL', 'Yes')
        if self.ui.checkBox_7.checkState() == 0:
            set_value_in_property_file('settings.ini', 'Sec', 'allowDownloadButtonCRL', 'No', config)
            config.set('Sec', 'allowDownloadButtonCRL', 'No')
            self.ui.pushButton_4.setDisabled(True)
        elif self.ui.checkBox_7.checkState() == 2:
            set_value_in_property_file('settings.ini', 'Sec', 'allowDownloadButtonCRL', 'Yes', config)
            config.set('Sec', 'allowDownloadButtonCRL', 'Yes')
            self.ui.pushButton_4.setEnabled(True)
        if self.ui.checkBox_8.checkState() == 0:
            set_value_in_property_file('settings.ini', 'Sec', 'allowCheckButtonCRL', 'No', config)
            config.set('Sec', 'allowCheckButtonCRL', 'No')
            self.ui.pushButton_5.setDisabled(True)
        elif self.ui.checkBox_8.checkState() == 2:
            set_value_in_property_file('settings.ini', 'Sec', 'allowCheckButtonCRL', 'Yes', config)
            config.set('Sec', 'allowCheckButtonCRL', 'Yes')
            self.ui.pushButton_5.setEnabled(True)
        self.ui.label_27.setText('Настройки сохранены')
        logs('Info: save_settings_main::Saved', 'info', '6')

    def save_settings_sub(self):
        set_value_in_property_file('settings.ini', 'Folders', 'certs', self.ui.label_12.text(), config)
        config.set('Folders', 'certs', self.ui.label_12.text())
        set_value_in_property_file('settings.ini', 'Folders', 'crls', self.ui.label_13.text(), config)
        config.set('Folders', 'crls', self.ui.label_13.text())
        set_value_in_property_file('settings.ini', 'Folders', 'tmp', self.ui.label_10.text(), config)
        config.set('Folders', 'tmp', self.ui.label_10.text())
        set_value_in_property_file('settings.ini', 'Folders', 'uc', self.ui.label_11.text(), config)
        config.set('Folders', 'uc', self.ui.label_11.text())
        set_value_in_property_file('settings.ini', 'Folders', 'to_uc', self.ui.label_9.text(), config)
        config.set('Folders', 'to_uc', self.ui.label_9.text())

        if self.ui.checkBox_12.checkState() == 0:
            set_value_in_property_file('settings.ini', 'Schedule', 'allowupdatecrlbystart', 'No', config)
            config.set('Schedule', 'allowupdatecrlbystart', 'No')
        elif self.ui.checkBox_12.checkState() == 2:
            set_value_in_property_file('settings.ini', 'Schedule', 'allowupdatecrlbystart', 'Yes', config)
            config.set('Schedule', 'allowupdatecrlbystart', 'Yes')
        if self.ui.checkBox_13.checkState() == 0:
            set_value_in_property_file('settings.ini', 'Schedule', 'allowupdatetslbystart', 'No', config)
            config.set('Schedule', 'allowupdatetslbystart', 'No')
        elif self.ui.checkBox_13.checkState() == 2:
            set_value_in_property_file('settings.ini', 'Schedule', 'allowupdatetslbystart', 'Yes', config)
            config.set('Schedule', 'allowupdatetslbystart', 'Yes')
        if self.ui.checkBox_15.checkState() == 0:
            set_value_in_property_file('settings.ini', 'Schedule', 'allowmonitoringcrlbystart', 'No', config)
            config.set('Schedule', 'allowmonitoringcrlbystart', 'No')
        elif self.ui.checkBox_15.checkState() == 2:
            set_value_in_property_file('settings.ini', 'Schedule', 'allowmonitoringcrlbystart', 'Yes', config)
            config.set('Schedule', 'allowmonitoringcrlbystart', 'Yes')

        set_value_in_property_file('settings.ini', 'Logs', 'loglevel', self.ui.comboBox.currentText(), config)
        config.set('Logs', 'loglevel', self.ui.comboBox.currentText())
        set_value_in_property_file('settings.ini', 'Logs', 'dividelogsbysize', str(self.ui.spinBox.value()), config)
        config.set('Logs', 'dividelogsbysize', str(self.ui.spinBox.value()))
        if self.ui.checkBox_14.checkState() == 0:
            set_value_in_property_file('settings.ini', 'Logs', 'dividelogsbyday', 'No', config)
            config.set('Logs', 'dividelogsbyday', 'No')
        elif self.ui.checkBox_14.checkState() == 2:
            set_value_in_property_file('settings.ini', 'Logs', 'dividelogsbyday', 'Yes', config)
            config.set('Logs', 'dividelogsbyday', 'Yes')
        self.ui.label_28.setText('Настройки сохранены')
        logs('Info: save_settings_sub::Saved', 'info', '6')

    def open_sub_window_info_uc(self, reg_number):
        if self.window_uc is None:
            self.window_uc = UcWindow(reg_number)
            self.window_uc.show()
        else:
            self.window_uc.close()  # Close window.
            self.window_uc = None  # Discard reference.

    def open_sub_window_info_crl(self, crl_key_id):
        if self.window_crl is None:
            self.window_crl = CRLWindow(crl_key_id)
            self.window_crl.show()
        else:
            self.window_crl.close()  # Close window.
            self.window_crl = None  # Discard reference.

    def open_sub_window_add(self):
        if self.window_add_crl is None:
            self.window_add_crl = AddCRLWindow()
            self.window_add_crl.show()
        else:
            self.window_add_crl.close()  # Close window.
            self.window_add_crl = None  # Discard reference.

    def choose_directory(self, type_file):
        input_dir = QFileDialog.getExistingDirectory(None, 'Выбор директории:', os.path.expanduser("~"))
        if type_file == 'crl':
            self.ui.label_13.setText(input_dir)
        if type_file == 'cert':
            self.ui.label_12.setText(input_dir)
        if type_file == 'uc':
            self.ui.label_11.setText(input_dir)
        if type_file == 'tmp':
            self.ui.label_10.setText(input_dir)
        if type_file == 'to_uc':
            self.ui.label_9.setText(input_dir)

    def add_watch_current_crl(self, registration_number, keyid, stamp, serial_number, url_crl):
        while True:
            try:
                count = WatchingCRL.select().where(WatchingCRL.Stamp.contains(stamp)
                                                   | WatchingCRL.SerialNumber.contains(serial_number)).count()
            except peewee.OperationalError:
                print('OperationalError')
                time.sleep(3)
            else:
                break

        if count < 1:
            while True:
                try:
                    select_uc = UC.select().where(UC.Registration_Number == registration_number)
                except peewee.OperationalError:
                    print('OperationalError')
                    time.sleep(3)
                else:
                    break

            for row in select_uc:
                while True:
                    try:
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
                    except peewee.OperationalError:
                        print('OperationalError')
                        time.sleep(3)
                    else:
                        break

                added_id = add_to_watching_crl.ID
                # self.ui.label_24.setText('Добавляем в список скачивания')
                # download(self, file_url, file_name, file_type, file_id, dc=0):
                self._download_crl = MainDownloader('MainDownloader_single_2', 'single',
                                               url_crl,
                                               config['Folders']['crls'] + '/' + keyid + '.crl',
                                               'current',
                                               added_id)
                self._download_crl.done.connect(
                    lambda: self.ui.label_24.setText('CRL Скачан и добавлен в список скачивания'))
                self._download_crl.done_err.connect(
                    lambda: self.ui.label_24.setText('CRL добавлен в список скачивания но не смог скачаться'))
                self._download_crl.start()
        else:
            logs('Info: add_watch_current_crl::crl_exist:' + keyid, 'info', '7')
            self.ui.label_24.setText('CRL ' + keyid + ' уже находится в списке отслеживания')

    def add_watch_custom_crl(self, url_crl):
        while True:
            try:
                count = WatchingCustomCRL.select().where(WatchingCustomCRL.UrlCRL.contains(url_crl)).count()
            except peewee.OperationalError:
                print('OperationalError')
                time.sleep(3)
            else:
                break

        if count < 1:
            while True:
                try:
                    WatchingCustomCRL(Name='Unknown',
                                      INN='0',
                                      OGRN='0',
                                      KeyId='Unknown',
                                      Stamp='Unknown',
                                      SerialNumber='Unknown',
                                      UrlCRL=url_crl).save()
                except peewee.OperationalError:
                    print('OperationalError')
                    time.sleep(3)
                else:
                    break
            self.counter_added_custom = self.counter_added_custom + 1
            logs('Info: add_watch_custom_crl::crl_added:' + url_crl, 'info', '7')
        else:
            logs('Info: add_watch_custom_crl::crl_exist:' + url_crl, 'info', '7')
            self.counter_added_exist = self.counter_added_exist + 1
        self.on_changed_find_watching_crl('')

    def add_log_to_main_tab(self, msg):
        msg_list = msg.split(';')[1:]
        for msg in msg_list:
            if not msg == 'NaN':
                button_info_log = QPushButton()
                button_info_log.setFixedSize(23, 23)
                button_info_log.setIcon(self.icon_info)
                button_info_log.setFlat(True)
                key_id = msg.split(' : ')[0]
                button_info_log.pressed.connect(lambda id_key=key_id: self.open_sub_window_info_crl(id_key))
                button_info_log.setToolTip('Подробная информация')
                current_row_count = self.ui.tableWidget_9.rowCount()
                self.ui.tableWidget_9.setRowCount(current_row_count + 1)
                self.ui.tableWidget_9.setCellWidget(current_row_count, 0, button_info_log)
                self.ui.tableWidget_9.setItem(current_row_count, 1, QTableWidgetItem(msg.split(' : ')[1]))
                self.ui.tableWidget_9.scrollToBottom()

    def move_watching_to_passed(self, id_var, from_var, idt):
        if from_var == 'current':
            while True:
                try:
                    from_bd = WatchingCRL.select().where(WatchingCRL.ID == id_var)
                except peewee.OperationalError:
                    print('OperationalError')
                    time.sleep(3)
                else:
                    break

            for row in from_bd:
                while True:
                    try:
                        WatchingDeletedCRL(Name=row.Name,
                                           INN=row.INN,
                                           OGRN=row.OGRN,
                                           KeyId=row.KeyId,
                                           Stamp=row.Stamp,
                                           SerialNumber=row.SerialNumber,
                                           UrlCRL=row.UrlCRL,
                                           status=row.status,
                                           download_status=row.download_status,
                                           download_count=row.download_count,
                                           last_download=row.last_download,
                                           last_update=row.last_update,
                                           next_update=row.next_update,
                                           moved_from='current').save()
                    except peewee.OperationalError:
                        print('OperationalError')
                        time.sleep(3)
                    else:
                        break
            while True:
                try:
                    WatchingCRL.delete_by_id(id_var)
                except peewee.OperationalError:
                    print('OperationalError')
                    time.sleep(3)
                else:
                    break
            # self.ui.tableWidget_4.removeRow(idt)
            self.sub_tab_watching_crl('', self.sub_tab_watching_crl_sorting, 'No')
            self.sub_tab_watching_disabled_crl('', self.sub_tab_watching_disabled_crl_sorting, 'No')
            logs('Info: move_watching_to_passed()::moving_success_current:', 'info', '7')
        elif from_var == 'custom':
            while True:
                try:
                    from_bd = WatchingCustomCRL.select().where(WatchingCustomCRL.ID == id_var)
                except peewee.OperationalError:
                    print('OperationalError')
                    time.sleep(3)
                else:
                    break

            for row in from_bd:
                while True:
                    try:
                        WatchingDeletedCRL(Name=row.Name,
                                           INN=row.INN,
                                           OGRN=row.OGRN,
                                           KeyId=row.KeyId,
                                           Stamp=row.Stamp,
                                           SerialNumber=row.SerialNumber,
                                           UrlCRL=row.UrlCRL,
                                           status=row.status,
                                           download_status=row.download_status,
                                           download_count=row.download_count,
                                           last_download=row.last_download,
                                           last_update=row.last_update,
                                           next_update=row.next_update,
                                           moved_from='custom').save()
                    except peewee.OperationalError:
                        print('OperationalError')
                        time.sleep(3)
                    else:
                        break
            while True:
                try:
                    WatchingCustomCRL.delete_by_id(id_var)
                except peewee.OperationalError:
                    print('OperationalError')
                    time.sleep(3)
                else:
                    break
            # self.ui.tableWidget_5.removeRow(idt)
            self.sub_tab_watching_custom_crl('', self.sub_tab_watching_custom_crl_sorting, 'No')
            self.sub_tab_watching_disabled_crl('', self.sub_tab_watching_disabled_crl_sorting, 'No')
            logs('Info: move_watching_to_passed::moving_success_custom:', 'info', '7')
        else:
            logs('Error: move_watching_to_passed::Error_Moving', 'errors', '2')

    def move_passed_to_watching(self, id_var):
        while True:
            try:
                from_bd = WatchingDeletedCRL.select().where(WatchingDeletedCRL.ID == id_var)
            except peewee.OperationalError:
                print('OperationalError')
                time.sleep(3)
            else:
                break

        for row in from_bd:
            if row.moved_from == 'current':
                while True:
                    try:
                        WatchingCRL(Name=row.Name,
                                    INN=row.INN,
                                    OGRN=row.OGRN,
                                    KeyId=row.KeyId,
                                    Stamp=row.Stamp,
                                    SerialNumber=row.SerialNumber,
                                    UrlCRL=row.UrlCRL,
                                    status=row.status,
                                    download_status=row.download_status,
                                    download_count=row.download_count,
                                    last_download=row.last_download,
                                    last_update=row.last_update,
                                    next_update=row.next_update).save()
                    except peewee.OperationalError:
                        print('OperationalError')
                        time.sleep(3)
                    else:
                        break
                while True:
                    try:
                        WatchingDeletedCRL.delete_by_id(id_var)
                    except peewee.OperationalError:
                        print('OperationalError')
                        time.sleep(3)
                    else:
                        break

                self.sub_tab_watching_crl('', self.sub_tab_watching_crl_sorting, 'No')
                self.sub_tab_watching_disabled_crl('', self.sub_tab_watching_disabled_crl_sorting, 'No')
                logs('Info: move_passed_to_watching()::moving_success_current:', 'info', '7')
            elif row.moved_from == 'custom':
                while True:
                    try:
                        WatchingCustomCRL(Name=row.Name,
                                          INN=row.INN,
                                          OGRN=row.OGRN,
                                          KeyId=row.KeyId,
                                          Stamp=row.Stamp,
                                          SerialNumber=row.SerialNumber,
                                          UrlCRL=row.UrlCRL,
                                          status=row.status,
                                          download_status=row.download_status,
                                          download_count=row.download_count,
                                          last_download=row.last_download,
                                          last_update=row.last_update,
                                          next_update=row.next_update).save()
                    except peewee.OperationalError:
                        print('OperationalError')
                        time.sleep(3)
                    else:
                        break
                while True:
                    try:
                        WatchingDeletedCRL.delete_by_id(id_var)
                    except peewee.OperationalError:
                        print('OperationalError')
                        time.sleep(3)
                    else:
                        break

                self.sub_tab_watching_custom_crl('', self.sub_tab_watching_custom_crl_sorting, 'No')
                self.sub_tab_watching_disabled_crl('', self.sub_tab_watching_disabled_crl_sorting, 'No')
                logs('Info: move_passed_to_watching::moving_success_custom:', 'info', '7')
            else:
                logs('Error: move_passed_to_watching::error_moving', 'errors', '2')

    def xml_check(self, ver_from_tsl):
        while True:
            try:
                query_get_settings = Settings.select()
            except peewee.OperationalError:
                print('OperationalError')
                time.sleep(3)
            else:
                break
        ver = 0
        for settings in query_get_settings:
            ver = settings.value
            break
        if int(ver) == int(ver_from_tsl):
            logs('Info: Update not need', 'info', '6')
            self.ui.label_7.setText('Загрузка завершена, обновление не требуется')
        else:
            logs('Info: Need update, new version ' + ver_from_tsl + ', old ' + ver, 'info', '6')
            self.ui.label_7.setText('Загрузка завершена, требуются обновления Базы УЦ и сертификатов. Новая версия '
                                    + ver_from_tsl + ' текущая версия ' + ver)
            if config['Schedule']['allowupdatetslbystart'] == 'Yes' and \
                    config['Schedule']['allowupdatecrlbystart'] == 'Yes':
                self.xml_init()

    def import_crl_list(self, file_name='crl_list.txt'):
        path = os.path.realpath(file_name)
        if os.path.exists(path):
            crl_list = open(file_name, 'r')
            crl_lists = crl_list.readlines()
            for crl_url in crl_lists:
                crl_url = crl_url.replace("\n", "")
                print(crl_url)
                while True:
                    try:
                        count = CRL.select().where(CRL.UrlCRL.contains(crl_url)).count()
                    except peewee.OperationalError:
                        print('OperationalError')
                        time.sleep(3)
                    else:
                        break
                while True:
                    try:
                        data = CRL.select().where(CRL.UrlCRL.contains(crl_url))
                    except peewee.OperationalError:
                        print('OperationalError')
                        time.sleep(3)
                    else:
                        break

                if count > 0:
                    for row in data:
                        print(row.Registration_Number)
                        self.add_watch_current_crl(row.Registration_Number, row.KeyId, row.Stamp, row.SerialNumber,
                                                   row.UrlCRL)
                else:
                    print('add to custom')
                    self.add_watch_custom_crl(crl_url)
                # self.on_changed_find_watching_crl('')
            print(self.counter_added, self.counter_added_custom, self.counter_added_exist)
        else:
            logs('Info: Not found crl_list.txt', 'info', '5')

    def export_crl(self):
        self.ui.label_7.setText('Генерируем файл')
        export_all_watching_crl()
        self.ui.label_7.setText('Файл сгенерирован')

    def xml_init(self):
        if not self._init_xml.isRunning():
            self.ui.progressBar_2.setMaximum(100)
            self.ui.pushButton_2.setEnabled(False)
            self.ui.pushButton.setEnabled(False)
            self._init_xml.start()

    def xml_download(self):
        if not self._download.isRunning():
            self.ui.label_7.setText('Скачиваем список.')
            self.ui.label_7.adjustSize()
            self.ui.pushButton.setEnabled(False)
            self.ui.pushButton_2.setEnabled(False)
            self._download.start()

    def downloader(self):
        if not self._down.isRunning():
            self.ui.pushButton_3.setDisabled(True)
            self.ui.pushButton_4.setDisabled(True)
            self.ui.pushButton_5.setDisabled(True)
            self._down.start()

    def down_mon(self):
        if not self._down_mon.isRunning():
            self.ui.pushButton_3.setDisabled(True)
            self.ui.pushButton_4.setDisabled(True)
            self.ui.pushButton_5.setDisabled(True)
            self._down_mon.start()

    def checker(self):
        if not self._checker.isRunning():
            self.ui.pushButton_3.setDisabled(True)
            self.ui.pushButton_4.setDisabled(True)
            self.ui.pushButton_5.setDisabled(True)
            self._checker.start()

    def watchdog(self):
        if not self._woof.isRunning():
            self._woof.start()

    def main_worker_stop(self):
        self._squirrel.stop()

    def main_worker(self):
        if not self._squirrel.isRunning():
            self._squirrel.start()

    def download_file(self, file_url, file_name, folder, file_type='', file_id='', set_dd='No'):
        file_path = folder + '/' + file_name
        self._down_single = MainDownloader('MainDownloader_single_3', 'single', file_url, file_path, file_type, file_id)
        self._down_single.start()

    def copy_crl_to_uc(self, rki, url):
        if os.path.exists(config['Folders']['crls'] + '/' + rki + '.crl'):
            shutil.copy2(config['Folders']['crls'] + '/' + rki + '.crl', config['Folders']['to_uc'] + '/' + rki + '.crl')
            logs('Info: found ' + config['Folders']['crls'] + '/' + rki + '.crl', 'info', '5')
        else:
            logs('Info: Not found ' + config['Folders']['crls'] + '/' + rki + '.crl', 'info', '5')
            self.download_file(url, rki + '.crl', config['Folders']['to_uc'])
    # def db_query(self, table, query, operator, where, group_by, order):
    #     _db_query = DBQuerying()
    #     _db_query.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle(config['Style']['window'])
    main_app = MainWindow()
    main_app.show()
    if config['Schedule']['allowupdatetslbystart'] == 'Yes':
        main_app.xml_download()
    if config['Schedule']['allowmonitoringcrlbystart'] == 'Yes':
        main_app.main_worker()
    main_app.watchdog()
    sys.exit(app.exec_())
