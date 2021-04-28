from peewee import Model, CharField, SqliteDatabase, DateTimeField, IntegerField, DateField
from main_log_system import logs
from main_settings import *
import datetime
import shutil
import os
import sqlite3

sqlite3.connect(config['Bd']['name'])
db = SqliteDatabase(config['Bd']['name'])


bd_backup_name = str('cert_crl.db_') + datetime.datetime.now().strftime('%Y%m%d') + '.bkp'
if os.path.isfile(bd_backup_name):
    logs('Info: ' + bd_backup_name + ' exist', 'info', '7')
else:
    shutil.copy2('cert_crl.db', bd_backup_name)
    logs('Info: ' + bd_backup_name + ' created', 'info', '6')


class UC(Model):
    ID = IntegerField(primary_key=True)
    Registration_Number = IntegerField()
    INN = IntegerField()
    OGRN = IntegerField()
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
    Name = CharField()
    KeyId = CharField()
    Stamp = CharField()
    SerialNumber = CharField()
    Data = CharField()

    class Meta:
        database = db


class CRL(Model):
    ID = IntegerField(primary_key=True)
    Registration_Number = IntegerField()
    Name = CharField()
    KeyId = CharField()
    Stamp = CharField()
    SerialNumber = CharField()
    UrlCRL = CharField()

    class Meta:
        database = db


class WatchingCRL(Model):
    ID = IntegerField(primary_key=True)
    Name = CharField()
    INN = IntegerField()
    OGRN = IntegerField()
    KeyId = CharField()
    Stamp = CharField()
    SerialNumber = CharField()
    UrlCRL = CharField()
    status = CharField()
    download_status = CharField()
    download_count = CharField()
    last_download = DateTimeField()
    last_update = DateTimeField()
    next_update = DateTimeField()

    class Meta:
        database = db


class WatchingCustomCRL(Model):
    ID = IntegerField(primary_key=True)
    Name = CharField()
    INN = IntegerField()
    OGRN = IntegerField()
    KeyId = CharField()
    Stamp = CharField()
    SerialNumber = CharField()
    UrlCRL = CharField()
    status = CharField()
    download_status = CharField()
    download_count = CharField()
    last_download = DateTimeField()
    last_update = DateTimeField()
    next_update = DateTimeField()

    class Meta:
        database = db


class WatchingDeletedCRL(Model):
    ID = IntegerField(primary_key=True)
    Name = CharField()
    INN = IntegerField()
    OGRN = IntegerField()
    KeyId = CharField()
    Stamp = CharField()
    SerialNumber = CharField()
    UrlCRL = CharField()
    status = CharField()
    download_status = CharField()
    download_count = CharField()
    last_download = DateTimeField()
    last_update = DateField()
    next_update = DateField()
    moved_from = CharField()

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
    Settings(name='ver', value=0).save()
    Settings(name='data_update', value='1970-01-01 00:00:00').save()
if not WatchingCRL.table_exists():
    WatchingCRL.create_table()
if not WatchingCustomCRL.table_exists():
    WatchingCustomCRL.create_table()
if not WatchingDeletedCRL.table_exists():
    WatchingDeletedCRL.create_table()
