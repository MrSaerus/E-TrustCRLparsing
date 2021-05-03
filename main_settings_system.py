def check_settings_file(config):
    if not config.has_option('Folders', 'certs'):
        set_value_in_property_file('settings.ini', 'Folders', 'certs', 'certs/', config)
    if not config.has_option('Folders', 'crls'):
        set_value_in_property_file('settings.ini', 'Folders', 'crls', 'crls/', config)
    if not config.has_option('Folders', 'tmp'):
        set_value_in_property_file('settings.ini', 'Folders', 'tmp', 'temp/', config)
    if not config.has_option('Folders', 'logs'):
        set_value_in_property_file('settings.ini', 'Folders', 'logs', 'logs/', config)
    if not config.has_option('Folders', 'to_uc'):
        set_value_in_property_file('settings.ini', 'Folders', 'to_uc', 'to_uc/', config)
    if not config.has_option('Folders', 'uc'):
        set_value_in_property_file('settings.ini', 'Folders', 'uc', 'uc/', config)

    if not config.has_option('MainWindow', 'width'):
        set_value_in_property_file('settings.ini', 'MainWindow', 'width', '1100', config)
    if not config.has_option('MainWindow', 'height'):
        set_value_in_property_file('settings.ini', 'MainWindow', 'height', '650', config)
    if not config.has_option('MainWindow', 'saveWidth'):
        set_value_in_property_file('settings.ini', 'MainWindow', 'saveWidth', 'No', config)
    if not config.has_option('MainWindow', 'AllowResize'):
        set_value_in_property_file('settings.ini', 'MainWindow', 'AllowResize', 'Yes', config)

    if not config.has_option('Bd', 'type'):
        set_value_in_property_file('settings.ini', 'Bd', 'type', 'sqlite3', config)
    if not config.has_option('Bd', 'name'):
        set_value_in_property_file('settings.ini', 'Bd', 'name', 'cert_crl.db', config)

    if not config.has_option('Socket', 'timeout'):
        set_value_in_property_file('settings.ini', 'Socket', 'timeout', 'No', config)

    if not config.has_option('Listing', 'uc'):
        set_value_in_property_file('settings.ini', 'Listing', 'uc', '500', config)
    if not config.has_option('Listing', 'crl'):
        set_value_in_property_file('settings.ini', 'Listing', 'crl', '500', config)
    if not config.has_option('Listing', 'cert'):
        set_value_in_property_file('settings.ini', 'Listing', 'cert', '500', config)
    if not config.has_option('Listing', 'watch'):
        set_value_in_property_file('settings.ini', 'Listing', 'watch', '500', config)

    if not config.has_option('Style', 'window'):
        set_value_in_property_file('settings.ini', 'Style', 'window', 'Fusion', config)
    if not config.has_option('Style', 'extendetColorInfo'):
        set_value_in_property_file('settings.ini', 'Style', 'extendetColorInfo', 'No', config)

    if not config.has_option('Proxy', 'proxyOn'):
        set_value_in_property_file('settings.ini', 'Proxy', 'proxyOn', 'No', config)
    if not config.has_option('Proxy', 'ip'):
        set_value_in_property_file('settings.ini', 'Proxy', 'ip', '', config)
    if not config.has_option('Proxy', 'port'):
        set_value_in_property_file('settings.ini', 'Proxy', 'port', '', config)
    if not config.has_option('Proxy', 'login'):
        set_value_in_property_file('settings.ini', 'Proxy', 'login', '', config)
    if not config.has_option('Proxy', 'password'):
        set_value_in_property_file('settings.ini', 'Proxy', 'password', '', config)

    if not config.has_option('Update', 'priority'):
        set_value_in_property_file('settings.ini', 'Update', 'priority', 'custom', config)
    if not config.has_option('Update', 'advancedChecking'):
        set_value_in_property_file('settings.ini', 'Update', 'advancedChecking', 'Yes', config)
    if not config.has_option('Update', 'viewingCRLlastNextUpdate'):
        set_value_in_property_file('settings.ini', 'Update', 'viewingCRLlastNextUpdate', 'Yes', config)
    if not config.has_option('Update', 'allowupdatecrlbystart'):
        set_value_in_property_file('settings.ini', 'Update', 'allowupdatecrlbystart', 'No', config)
    if not config.has_option('Update', 'allowupdatetslbystart'):
        set_value_in_property_file('settings.ini', 'Update', 'allowupdatetslbystart', 'No', config)
    if not config.has_option('Update', 'deltaupdateinday'):
        set_value_in_property_file('settings.ini', 'Update', 'deltaupdateinday', '10', config)
    if not config.has_option('Update', 'timebeforeupdate'):
        set_value_in_property_file('settings.ini', 'Update', 'timebeforeupdate', '20', config)
    if not config.has_option('Update', 'main_uc_ogrn'):
        set_value_in_property_file('settings.ini', 'Update', 'main_uc_ogrn', '1047702026701', config)
    if not config.has_option('Update', 'self_uc_ogrn'):
        set_value_in_property_file('settings.ini', 'Update', 'self_uc_ogrn', '1020203227263', config)

    if not config.has_option('Backup', 'backUPbyStart'):
        set_value_in_property_file('settings.ini', 'Backup', 'backUPbyStart', 'Yes', config)

    if not config.has_option('Tabs', 'ucLimit'):
        set_value_in_property_file('settings.ini', 'Tabs', 'ucLimit', '500', config)
    if not config.has_option('Tabs', 'ucAllowDelete'):
        set_value_in_property_file('settings.ini', 'Tabs', 'ucAllowDelete', 'No', config)
    if not config.has_option('Tabs', 'crlLimit'):
        set_value_in_property_file('settings.ini', 'Tabs', 'crlLimit', '500', config)
    if not config.has_option('Tabs', 'crlAllowDelete'):
        set_value_in_property_file('settings.ini', 'Tabs', 'crlAllowDelete', 'No', config)
    if not config.has_option('Tabs', 'certLimit'):
        set_value_in_property_file('settings.ini', 'Tabs', 'certLimit', '500', config)
    if not config.has_option('Tabs', 'certAllowDelete'):
        set_value_in_property_file('settings.ini', 'Tabs', 'certAllowDelete', 'No', config)
    if not config.has_option('Tabs', 'wcLimit'):
        set_value_in_property_file('settings.ini', 'Tabs', 'wcLimit', '500', config)
    if not config.has_option('Tabs', 'wcAllowDelete'):
        set_value_in_property_file('settings.ini', 'Tabs', 'wcAllowDelete', 'No', config)
    if not config.has_option('Tabs', 'wccLimit'):
        set_value_in_property_file('settings.ini', 'Tabs', 'wccLimit', '500', config)
    if not config.has_option('Tabs', 'wccAllowDelete'):
        set_value_in_property_file('settings.ini', 'Tabs', 'wccAllowDelete', 'No', config)
    if not config.has_option('Tabs', 'wcdLimit'):
        set_value_in_property_file('settings.ini', 'Tabs', 'wcdLimit', '500', config)
    if not config.has_option('Tabs', 'wcdAllowDelete'):
        set_value_in_property_file('settings.ini', 'Tabs', 'wcdAllowDelete', 'No', config)

    if not config.has_option('Schedule', 'allowschedule'):
        set_value_in_property_file('settings.ini', 'Schedule', 'allowschedule', 'No', config)
    if not config.has_option('Schedule', 'weekupdate'):
        set_value_in_property_file('settings.ini', 'Schedule', 'weekupdate', 'All', config)
    if not config.has_option('Schedule', 'timeupdate'):
        set_value_in_property_file('settings.ini', 'Schedule', 'timeupdate', '1M', config)
    if not config.has_option('Schedule', 'periodUpdate'):
        set_value_in_property_file('settings.ini', 'Schedule', 'periodupdate',
                                   '8h:20m:5m:5;24h:60m:10m:5;7d:6h:1h:10', config)
    if not config.has_option('Schedule', 'allowUpdateTSLbyStart'):
        set_value_in_property_file('settings.ini', 'Schedule', 'allowUpdateTSLbyStart', 'No', config)
    if not config.has_option('Schedule', 'allowUpdateCRLbyStart'):
        set_value_in_property_file('settings.ini', 'Schedule', 'allowUpdateCRLbyStart', 'No', config)
    if not config.has_option('Schedule', 'allowmonitoringcrlbystart'):
        set_value_in_property_file('settings.ini', 'Schedule', 'allowmonitoringcrlbystart', 'No', config)
    if not config.has_option('Schedule', 'rangeUpdateCRL'):
        set_value_in_property_file('settings.ini', 'Schedule', 'rangeUpdateCRL', '5day', config)

    if not config.has_option('Sec', 'allowImportCRL'):
        set_value_in_property_file('settings.ini', 'Sec', 'allowImportCRL', 'No', config)
    if not config.has_option('Sec', 'allowExportCRL'):
        set_value_in_property_file('settings.ini', 'Sec', 'allowExportCRL', 'No', config)
    if not config.has_option('Sec', 'allowDeleteWatchingCRL'):
        set_value_in_property_file('settings.ini', 'Sec', 'allowDeleteWatchingCRL', 'No', config)
    if not config.has_option('Sec', 'allowDownloadButtonCRL'):
        set_value_in_property_file('settings.ini', 'Sec', 'allowDownloadButtonCRL', 'Yes', config)
    if not config.has_option('Sec', 'allowCheckButtonCRL'):
        set_value_in_property_file('settings.ini', 'Sec', 'allowCheckButtonCRL', 'Yes', config)

    if not config.has_option('Logs', 'dividelogsbyday'):
        set_value_in_property_file('settings.ini', 'Logs', 'dividelogsbyday', 'Yes', config)
    if not config.has_option('Logs', 'dividelogsbysize'):
        set_value_in_property_file('settings.ini', 'Logs', 'dividelogsbysize', '1024', config)
    if not config.has_option('Logs', 'loglevel'):
        set_value_in_property_file('settings.ini', 'Logs', 'loglevel', '9', config)

    if not config.has_option('XMPP', 'server'):
        set_value_in_property_file('settings.ini', 'XMPP', 'server', '', config)
    if not config.has_option('XMPP', 'login'):
        set_value_in_property_file('settings.ini', 'XMPP', 'login', '', config)
    if not config.has_option('XMPP', 'password'):
        set_value_in_property_file('settings.ini', 'XMPP', 'password', '', config)
    if not config.has_option('XMPP', 'tosend'):
        set_value_in_property_file('settings.ini', 'XMPP', 'tosend', '', config)
    if not config.has_option('XMPP', 'sendinfoerr'):
        set_value_in_property_file('settings.ini', 'XMPP', 'sendinfoerr', 'No', config)
    if not config.has_option('XMPP', 'sendinfonewcrl'):
        set_value_in_property_file('settings.ini', 'XMPP', 'sendinfonewcrl', 'No', config)
    if not config.has_option('XMPP', 'sendinfonewtsl'):
        set_value_in_property_file('settings.ini', 'XMPP', 'sendinfonewtsl', 'No', config)

    if not config.has_option('Custom', 'main_uc_ogrn'):
        set_value_in_property_file('settings.ini', 'Custom', 'main_uc_ogrn', '1047702026701', config)
    if not config.has_option('Custom', 'self_uc_ogrn'):
        set_value_in_property_file('settings.ini', 'Custom', 'self_uc_ogrn', '1020203227263', config)


def set_value_in_property_file(file_path, section, key, value, config):
    config.read(file_path)
    if not config.has_section(section):
        config.add_section(section)
    config.set(section, key, value)
    config_file = open(file_path, 'w')
    config.write(config_file, space_around_delimiters=False)
    config_file.close()
