from PyQt5.QtCore import pyqtSignal, QThread
from main_models import WatchingCRL, WatchingCustomCRL
from main_settings import config
from main_moduls import download_loop_guard, download_update
from urllib import request
import datetime
import shutil
import os
import threading


class MainDownloader(QThread):
    print(threading.get_ident(), "MainDownloader")
    main_progress_total = pyqtSignal(int)
    main_progress_current = pyqtSignal(int)
    stage_progress_total = pyqtSignal(int)
    stage_progress_current = pyqtSignal(int)
    done = pyqtSignal(str)
    done_err = pyqtSignal(str)
    current_message = pyqtSignal(str)
    download_message = pyqtSignal(str)

    def __init__(self, modes, url='', path='', type_download='', id=''):
        QThread.__init__(self)
        self._init = False
        self.modeWork = modes
        self.FileURL = url
        self.FilePath = path
        self.FileType = type_download
        self.FileID = id

    def run(self):
        print(threading.get_ident(), "MainDownloader run")
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
            print('Download ' + file_url)
            self.download(file_url, folder + '/' + file_name, 'current', wc.ID)

        for wcc in query_2:
            counter_watching_custom_crl = counter_watching_custom_crl + 1
            file_url = wcc.UrlCRL
            file_name = wcc.KeyId + '.crl'
            self.current_message.emit(
                str(counter_watching_custom_crl) + ' из ' + str(watching_custom_crl_all) + ' Загружаем: ' + str(
                    wcc.Name) + ' ' + str(wcc.KeyId))
            print('Download ' + file_url)
            self.download(file_url, folder + '/' + file_name, 'custom', wcc.ID)
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
        for wc in query_1:
            download_counter = download_loop_guard(int(wc.download_count), wc.last_download, wc.next_update)
            if current_datetime > wc.next_update > before_current_date:
                file_path = config['Folders']['crls'] + '/' + wc.KeyId + '.crl'
                file_path_2 = config['Folders']['to_uc'] + '/' + 'current_' + wc.KeyId + '.crl'
                self.current_message.emit('Скачиваем и проверяем ' + wc.Name + ' ' + wc.KeyId)
                if self.download(wc.UrlCRL, file_path, 'current', wc.ID, download_counter) == 'down_success':
                    print('Downloaded ' + wc.UrlCRL)
                    shutil.copy2(file_path, file_path_2)
                    return_list_msg = return_list_msg + ';' + wc.KeyId + ' : ' + wc.Name
                    count = count + 1
        for wcc in query_2:
            download_counter = download_loop_guard(int(wcc.download_count), wcc.last_download, wcc.next_update)
            if current_datetime > wcc.next_update > before_current_date:
                file_path = config['Folders']['crls'] + '/' + wcc.KeyId + '.crl'
                file_path_2 = config['Folders']['to_uc'] + '/' + 'custom_' + wcc.KeyId + '.crl'
                self.current_message.emit('Скачиваем и проверяем ' + wcc.Name + ' ' + wcc.KeyId)
                if self.download(wcc.UrlCRL, file_path, 'custom', wcc.ID, download_counter) == 'down_success':
                    print('Downloaded ' + wcc.UrlCRL)
                    shutil.copy2(file_path, file_path_2)
                    return_list_msg = return_list_msg + ';' + wcc.KeyId + ' : ' + wcc.Name
                    count = count + 1
        self.current_message.emit('Готово')
        self.done.emit('Загрузка завершена')
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
            size_tls = os.path.getsize(file_name)
            self.stage_progress_total.emit(size_tls)
            self.stage_progress_current.emit(size_tls)
            self.stage_progress_total.emit(-1)
            self.done.emit('Загрузка завершена')
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
    _downloader = MainDownloader('single', file_url, file_path, file_type, file_id)
    _downloader.start()
