from PyQt5.QtCore import pyqtSignal, QThread
from main_models import WatchingCRL, WatchingCustomCRL
from main_settings import config
from main_moduls import download_loop_guard, download_update, delta_checker
from class_main_cheker import check_custom_crl, check_current_crl
from main_log_system import logs
from urllib import request
import datetime
import shutil
import os


class MainDownloader(QThread):
    main_progress_total = pyqtSignal(int)
    main_progress_current = pyqtSignal(int)
    stage_progress_total = pyqtSignal(int)
    stage_progress_current = pyqtSignal(int)
    done = pyqtSignal(str)
    done_err = pyqtSignal(str)
    current_message = pyqtSignal(str)
    download_message = pyqtSignal(str)

    def __init__(self, name, modes, url='', path='', type_download='', id=''):
        QThread.__init__(self)
        self.name = name
        self._init = False
        self.modeWork = modes
        self.FileURL = url
        self.FilePath = path
        self.FileType = type_download
        self.FileID = id

    def run(self):
        if self.modeWork == 'all':
            print('mode all')
        elif self.modeWork == 'all_mon':
            self.all_mon()
        elif self.modeWork == 'mon':
            self.mon()
        elif self.modeWork == 'current':
            print('mode all')
        elif self.modeWork == 'custom':
            print('mode all')
        elif self.modeWork == 'single':
            self.download(self.FileURL, self.FilePath, self.FileType, self.FileID)
            self.done.emit('Загрузка завершена')
        else:
            print('else')

    def all_mon(self):
        query_1 = WatchingCRL.select()
        query_2 = WatchingCustomCRL.select()
        counter_watching_crl_all = WatchingCRL.select().count()
        watching_custom_crl_all = WatchingCustomCRL.select().count()
        counter_watching_crl = 0
        counter_watching_custom_crl = 0
        self.current_message.emit('Загрузка началась')
        folder = config['Folders']['crls']
        for wc in query_1:
            counter_watching_crl = counter_watching_crl + 1
            file_url = wc.UrlCRL
            file_name = wc.KeyId + '.crl'
            self.current_message.emit(
                str(counter_watching_crl) + ' из ' + str(counter_watching_crl_all) + ' Загружаем: ' + str(
                    wc.Name) + ' ' + str(wc.KeyId))

            if self.download(file_url, folder + '/' + file_name, 'current', wc.ID) == 'down_success':
                logs('Info: Downloaded: ' + wc.Name + ' ' + wc.UrlCRL, 'download', '5')
            else:
                logs('Warn: Download error: ' + wc.Name + ' ' + wc.UrlCRL, 'download', '4')

        for wcc in query_2:
            counter_watching_custom_crl = counter_watching_custom_crl + 1
            file_url = wcc.UrlCRL
            file_name = wcc.KeyId + '.crl'
            self.current_message.emit(
                str(counter_watching_custom_crl) + ' из ' + str(watching_custom_crl_all) + ' Загружаем: ' + str(
                    wcc.Name) + ' ' + str(wcc.KeyId))
            if self.download(file_url, folder + '/' + file_name, 'custom', wcc.ID) == 'down_success':
                logs('Info: Downloaded: ' + wcc.Name + ' ' + wcc.UrlCRL, 'download', '5')
            else:
                logs('Warn: Download error: ' + wcc.Name + ' ' + wcc.UrlCRL, 'download', '4')
        self.current_message.emit('Загрузка закончена')
        self.done.emit('Загрузка завершена')

    def mon(self):
        current_datetimes = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        current_datetime = datetime.datetime.strptime(current_datetimes, '%Y-%m-%d %H:%M:%S')
        minuts = int(config['Update']['timebeforeupdate'])
        days = int(config['Update']['deltaupdateinday'])
        current_datetime = current_datetime + datetime.timedelta(minutes=minuts)
        before_current_date = datetime.datetime.now() - datetime.timedelta(days=days)
        query_1 = WatchingCRL.select()
        query_2 = WatchingCustomCRL.select()
        count = 0
        return_list_msg = ''
        self.current_message.emit('Загрузка началась')
        print('down start')
        for wc in query_1:
            # if current_datetime > wc.next_update > before_current_date:
            if delta_checker(wc.Name, wc.KeyId, wc.last_download, wc.last_update, wc.next_update, wc.download_count):
                download_counter = download_loop_guard(int(wc.download_count), wc.last_download, wc.last_update,
                                                       wc.next_update)
                if not download_counter == 'Timeout':
                    file_path = config['Folders']['crls'] + '/' + wc.KeyId + '.crl'
                    file_path_2 = config['Folders']['to_uc'] + '/' + 'current_' + wc.KeyId + '.crl'
                    self.current_message.emit('Скачиваем и проверяем ' + wc.Name + ' ' + wc.KeyId)
                    if self.download(wc.UrlCRL, file_path, 'current', wc.ID, download_counter) == 'down_success':
                        print('current_datetime', current_datetime,
                              '\nlast_update', wc.last_update,
                              '\nnext_update', wc.next_update,
                              '\nbefore_current_date', before_current_date,
                              '\nlast_download', wc.last_download)
                        logs('Info: Downloaded: ' + wc.Name + ' ' + wc.UrlCRL, 'download', '5')
                        shutil.copy2(file_path, file_path_2)
                        return_list_msg = return_list_msg + ';' + wc.KeyId + ' : ' + wc.Name
                        count = count + 1
                    else:
                        logs('Warn: Download error: ' + wc.Name + ' ' + wc.UrlCRL, 'download', '4')
        for wcc in query_2:
            # if current_datetime > wcc.next_update > before_current_date:
            if delta_checker(wcc.Name, wcc.KeyId, wcc.last_download, wcc.last_update, wcc.next_update, wcc.download_count):
                download_counter = download_loop_guard(int(wcc.download_count), wcc.last_download, wcc.last_update,
                                                       wcc.next_update)
                if not download_counter == 'Timeout':
                    file_path = config['Folders']['crls'] + '/' + wcc.KeyId + '.crl'
                    file_path_2 = config['Folders']['to_uc'] + '/' + 'custom_' + wcc.KeyId + '.crl'
                    self.current_message.emit('Скачиваем и проверяем ' + wcc.Name + ' ' + wcc.KeyId)

                    if self.download(wcc.UrlCRL, file_path, 'custom', wcc.ID, download_counter) == 'down_success':
                        print('current_datetime', current_datetime,
                              '\nlast_update', wcc.last_update,
                              '\nnext_update', wcc.next_update,
                              '\nbefore_current_date', before_current_date,
                              '\nlast_download', wcc.last_download)
                        logs('Info: Downloaded: ' + wcc.Name + ' ' + wcc.UrlCRL, 'download', '5')
                        shutil.copy2(file_path, file_path_2)
                        return_list_msg = return_list_msg + ';' + wcc.KeyId + ' : ' + wcc.Name
                        count = count + 1
                    else:
                        logs('Warn: Download error: ' + wcc.Name + ' ' + wcc.UrlCRL, 'download', '4')
        self.current_message.emit('Готово')
        self.done.emit('Загрузка завершена')
        print('down stop')
        if count > 0:
            self.download_message.emit(return_list_msg)
            return return_list_msg
        else:
            self.download_message.emit('NaN')
            return 'NaN'

    def download(self, file_url, file_name, file_type, file_id, dc=0):
        try:
            if config['Proxy']['proxyon'] == 'Yes':
                proxy = request.ProxyHandler(
                    {'https': 'https://' + config['Proxy']['ip'] + ':' + config['Proxy']['port'],
                     'http': 'http://' + config['Proxy']['ip'] + ':' + config['Proxy']['port']})
                opener = request.build_opener(proxy)
                request.install_opener(opener)
            request.urlretrieve(file_url, file_name, self._progress)
        except Exception:
            if not file_type == '' and not file_type == '' and not file_id == '':
                download_update('No', file_type, file_id, dc)
            self.done_err.emit('Ошибка загрузки')
            self.stage_progress_total.emit(-1)
            return 'down_error'
        else:
            if not file_type == '' and not file_type == '' and not file_id == '':
                download_update('Yes', file_type, file_id, dc)
            if file_type == 'custom':
                # print(file_id, file_url, file_name.split('/')[-1].split('.')[0])
                check_custom_crl(file_id, file_url, file_name.split('/')[-1].split('.')[0])
            if file_type == 'current':
                check_current_crl(file_id, file_url, file_name.split('/')[-1].split('.')[0])
                # print(file_id, file_url, file_name.split('/')[-1].split('.')[0])
            size_tls = os.path.getsize(file_name)
            self.stage_progress_total.emit(size_tls)
            self.stage_progress_current.emit(size_tls)
            self.stage_progress_total.emit(-1)
            return 'down_success'

    def _progress(self, block_num, block_size, total_size):
        if total_size == -1:
            self.stage_progress_total.emit(0)
            self.stage_progress_current.emit(0)
        else:
            downloaded = block_num * block_size
            if downloaded < total_size:
                self.stage_progress_current.emit(downloaded)
            else:
                self.stage_progress_current.emit(total_size)


def download_file(file_url, file_name, folder, file_type='', file_id='', set_dd='No'):
    file_path = folder + '/' + file_name
    _downloader = MainDownloader('MainDownloader_single_3', 'single', file_url, file_path, file_type, file_id)
    _downloader.start()


def copy_crl_to_uc(rki, url):
    if os.path.exists(config['Folders']['crls'] + '/' + rki + '.crl'):
        shutil.copy2(config['Folders']['crls'] + '/' + rki + '.crl', config['Folders']['to_uc'] + '/' + rki + '.crl')
        logs('Info: found ' + config['Folders']['crls'] + '/' + rki + '.crl', 'info', '5')
    else:
        logs('Info: Not found ' + config['Folders']['crls'] + '/' + rki + '.crl', 'info', '5')
        download_file(url, rki + '.crl', config['Folders']['to_uc'])
