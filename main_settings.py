from main_settings_system import check_settings_file
import configparser
import datetime
import os


tab_uc_sorting = 'asc'
tab_cert_sorting = 'asc'
tab_crl_sorting = 'asc'
sub_tab_watching_crl_sorting = 'asc'
sub_tab_watching_custom_crl_sorting = 'asc'
sub_tab_watching_disabled_crl_sorting = 'asc'


config = configparser.ConfigParser()
if os.path.isfile('settings.ini'):
    config.read('settings.ini')
else:
    open('settings.ini', 'w').close()

check_settings_file(config)

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
    os.makedirs(config['Folders']['uc'])
except OSError:
    pass
try:
    os.makedirs(config['Folders']['logs'])
except OSError:
    pass

if config['Logs']['dividelogsbyday'] == 'Yes':
    datetime_day = '_' + datetime.datetime.now().strftime('%Y%m%d')
else:
    datetime_day = ''

open(config['Folders']['logs'] + "/error" + datetime_day + ".log", "a").write('')
open(config['Folders']['logs'] + "/log" + datetime_day + ".log", "a").write('')
open(config['Folders']['logs'] + "/download" + datetime_day + ".log", "a").write('')
