from main_models import CERT, WatchingCRL, WatchingCustomCRL, db
from main_settings import config
from main_log_system import logs
from lxml import etree
import configparser
import datetime
import shutil
import base64
import os
import peewee
import time


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


def save_cert(key_id, folder):
    for certs in CERT.select().where(CERT.KeyId == key_id):
        with open(folder + "/" + certs.KeyId + ".cer", "wb") as file:
            file.write(base64.decodebytes(certs.Data.encode()))
        if folder == config['Folders']['certs']:
            os.startfile(os.path.realpath(config['Folders']['certs']))
            print(os.path.realpath(config['Folders']['certs']))
        elif folder == config['Folders']['to_uc']:
            os.startfile(os.path.realpath(config['Folders']['to_uc']))
            print(os.path.realpath(config['Folders']['to_uc']))


def copy_crl_to_uc(rki):
    if os.path.exists(config['Folders']['crls'] + '/' + rki + '.crl'):
        shutil.copy2(config['Folders']['crls'] + '/' + rki + '.crl', config['Folders']['to_uc'] + '/' + rki + '.crl')
        print('Found ' + config['Folders']['crls'] + '/' + rki + '.crl, copy.')
    else:
        print('Not found ' + config['Folders']['crls'] + '/' + rki + '.crl')
        logs('Info: Not found ' + config['Folders']['crls'] + '/' + rki + '.crl', 'info', '5')


def open_file(file_name, file_type, url='None'):
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
            save_cert(file_name, config['Folders']['certs'])
        # elif file_type == 'crl':
        #     download_file(url, file_name + '.crl', config['Folders']['crls'])
    else:
        open_crl = run_dll + "  " + path
        os.system(open_crl)


def download_update(set_dd, type_download, w_id, dc=0):
    current_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    current_datetime = datetime.datetime.strptime(current_datetime, '%Y-%m-%d %H:%M:%S')
    dc = int(dc)
    if dc == 10:
        next_update = current_datetime + datetime.timedelta(days=1)
    #if type_download == 'current':
    #    with db.transaction('exclusive'):
    #        (WatchingCRL
    #         .update(last_download=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    #         .where(WatchingCRL.ID == w_id).execute())

    #elif type_download == 'custom':
    #    with db.transaction('exclusive'):
    #        (WatchingCustomCRL
    #         .update(last_download=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    #         .where(WatchingCustomCRL.ID == w_id).execute())

    if set_dd == 'Yes':
        if dc < 10:
            if type_download == 'current':
                while True:
                    try:
                        with db.transaction('exclusive'):
                            (WatchingCRL.update(download_status='Info: Download successfully',
                                                download_count=dc,
                                                last_download=datetime.datetime.now()
                                                .strftime('%Y-%m-%d %H:%M:%S'))
                             .where(WatchingCRL.ID == w_id)
                             .execute())
                    except peewee.OperationalError:
                        print('OperationalError')
                        time.sleep(1)
                    else:
                        break

            elif type_download == 'custom':
                while True:
                    try:
                        with db.transaction('exclusive'):
                            (WatchingCustomCRL.update(download_status='Info: Download successfully',
                                                      download_count=dc,
                                                      last_download=datetime.datetime.now()
                                                      .strftime('%Y-%m-%d %H:%M:%S'))
                             .where(WatchingCustomCRL.ID == w_id)
                             .execute())
                    except peewee.OperationalError:
                        print('OperationalError')
                        time.sleep(1)
                    else:
                        break

        else:
            if type_download == 'current':
                while True:
                    try:
                        with db.transaction('exclusive'):
                            (WatchingCRL.update(download_status='Info: Download successfully',
                                                download_count=dc,
                                                next_update=next_update,
                                                last_download=datetime.datetime.now()
                                                .strftime('%Y-%m-%d %H:%M:%S'))
                             .where(WatchingCRL.ID == w_id)
                             .execute())
                    except peewee.OperationalError:
                        print('OperationalError')
                        time.sleep(1)
                    else:
                        break

            elif type_download == 'custom':
                while True:
                    try:
                        with db.transaction('exclusive'):
                            (WatchingCustomCRL.update(download_status='Info: Download successfully',
                                                      download_count=dc,
                                                      next_update=next_update,
                                                      last_download=datetime.datetime.now()
                                                      .strftime('%Y-%m-%d %H:%M:%S'))
                             .where(WatchingCustomCRL.ID == w_id)
                             .execute())
                    except peewee.OperationalError:
                        print('OperationalError')
                        time.sleep(1)
                    else:
                        break

    else:
        if type_download == 'current':
            while True:
                try:
                    with db.transaction('exclusive'):
                        (WatchingCRL.update(download_status='Error: Download failed',
                                            download_count=dc)
                         .where(WatchingCRL.ID == w_id)
                         .execute())
                except peewee.OperationalError:
                    print('OperationalError')
                    time.sleep(1)
                else:
                    break

        elif type_download == 'custom':
            while True:
                try:
                    with db.transaction('exclusive'):
                        (WatchingCustomCRL.update(download_status='Error: Download failed',
                                                  download_count=dc)
                         .where(WatchingCustomCRL.ID == w_id)
                         .execute())
                except peewee.OperationalError:
                    print('OperationalError')
                    time.sleep(1)
                else:
                    break


def download_loop_guard(download_count, last_download, next_update):
    current_datetimes = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    current_datetime = datetime.datetime.strptime(current_datetimes, '%Y-%m-%d %H:%M:%S')
    minuts = int(config['Update']['timebeforeupdate'])
    days = int(config['Update']['deltaupdateinday'])
    current_datetime = current_datetime + datetime.timedelta(minutes=minuts)

    delta_day = next_update + datetime.timedelta(days=1)
    delta_week = next_update + datetime.timedelta(days=7)
    delta_month = next_update + datetime.timedelta(days=30)

    if last_download > next_update:
        download_count += 1
    if current_datetime > next_update and download_count == 10:
        download_count = 0
    if download_count > 3:
        # print(current_datetime, next_update, delta_day, delta_week)
        if current_datetime > delta_day < delta_week:
            download_count = 10
    return download_count


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


# def exist_crl_in_custom_watch():
#     query = WatchingCRL.select()
#     for row in query:
#         if WatchingCustomCRL.select().where(WatchingCustomCRL.KeyId == row.KeyId).count() > 0:
#             print(row.KeyId, ' exist')


def set_value_in_property_file(file_path, section, key, value):
    set_config = configparser.ConfigParser()
    set_config.read(file_path)
    set_config.set(section, key, value)
    config_file = open(file_path, 'w')
    set_config.write(config_file, space_around_delimiters=False)
    config_file.close()
