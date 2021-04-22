from main_settings import config, datetime_day
import datetime


def logs(body, kind='', log_level=''):
    if int(log_level) <= int(config['Logs']['loglevel']):
        if kind == 'errors':
            with open(config['Folders']['logs'] + "/error" + datetime_day + ".log", "a") as file:
                file.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '    ' + body + '\n')
            file.close()
        elif kind == 'download':
            with open(config['Folders']['logs'] + "/download" + datetime_day + ".log", "a") as file:
                file.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '    ' + body + '\n')
            file.close()
        else:
            with open(config['Folders']['logs'] + "/log" + datetime_day + ".log", "a") as file:
                file.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '    ' + body + '\n')
            file.close()
