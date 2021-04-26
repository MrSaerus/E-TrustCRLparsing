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
    config['Folders'] = {'certs': 'certs/',
                         'crls': 'crls/',
                         'tmp': 'temp/',
                         'logs': 'logs/',
                         'to_uc': 'to_uc/',
                         'uc': 'uc/'}
    config['MainWindow'] = {'width ': '1100',
                            'height ': '650',
                            'saveWidth': 'No',
                            'AllowResize': 'Yes'}
    config['Bd'] = {'type': 'sqlite3',
                    'name': 'cert_crl.db'}
    config['Socket'] = {'timeout ': 'No'}
    config['Listing'] = {'uc': '500',
                         'crl': '500',
                         'cert': '500',
                         'watch': '500'}
    # windowsvista, Windows, Fusion
    config['Style'] = {'window': 'Fusion',
                       'extendetColorInfo': 'No'}
    config['Proxy'] = {'proxyOn': 'No',
                       'ip': '',
                       'port': '',
                       'login': '',
                       'password': ''}
    config['Update'] = {'priority': 'custom',
                        'advancedChecking': 'Yes',
                        'viewingCRLlastNextUpdate': 'Yes',
                        'allowupdatecrlbystart': 'No',
                        'allowupdatetslbystart': 'No',
                        'deltaupdateinday': '10',
                        'timebeforeupdate': '20',
                        'main_uc_ogrn': '1047702026701',
                        'self_uc_ogrn': '1020203227263'}
    config['Backup'] = {'backUPbyStart': 'Yes'}
    config['Tabs'] = {'ucLimit': '500',
                      'ucAllowDelete': 'No',
                      'crlLimit': '500',
                      'crlAllowDelete': 'No',
                      'certLimit': '500',
                      'certAllowDelete': 'No',
                      'wcLimit': '500',
                      'wcAllowDelete': 'No',
                      'wccLimit': '500',
                      'wccAllowDelete': 'No',
                      'wcdLimit': '500',
                      'wcdAllowDelete': 'No'}
    config['Schedule'] = {'allowschedule': 'No',
                          'weekupdate': 'All',
                          'timeupdate': '1M',
                          'periodUpdate': '9:00; 12:00; 16:00',
                          'allowUpdateTSLbyStart': 'No',
                          'allowUpdateCRLbyStart': 'No',
                          'allowmonitoringcrlbystart': 'No',
                          'rangeUpdateCRL': '5day'}
    config['Sec'] = {'allowImportCRL': 'No',
                     'allowExportCRL': 'No',
                     'allowDeleteWatchingCRL': 'No',
                     'allowDownloadButtonCRL': 'Yes',
                     'allowCheckButtonCRL': 'Yes'}
    config['Logs'] = {'dividelogsbyday': 'Yes',
                      'dividelogsbysize': '1024',
                      'loglevel': '9'}
    config['XMPP'] = {'server': '',
                      'login': '',
                      'password': '',
                      'tosend': '',
                      'sendinfoerr': 'No',
                      'sendinfonewcrl': 'No',
                      'sendinfonewtsl': 'No'}
    config['Custom'] = {'main_uc_ogrn': '1047702026701',
                        'self_uc_ogrn': '1020203227263'}
    with open('settings.ini', 'w') as configfile:
        config.write(configfile)

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
