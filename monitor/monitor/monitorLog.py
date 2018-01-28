# -*- coding: utf-8 -*-
import logging
import logging.handlers

MAX_LOGFILE_BYTE = 10 * 1024 * 1024
MAX_LOG_COUNT = 10

def set_log_level(level, loggername='luhya'):
    logger = logging.getLogger(loggername)
    if level == 'error':
        logger.setLevel(logging.ERROR)
    elif level == 'warning':
        logger.setLevel(logging.WARNING)
    elif level == 'info':
        logger.setLevel(logging.INFO)

def init_log(logfile, loggername='luhya'):
    logger = logging.getLogger(loggername)
    if len(logger.handlers) == 0:
        ch = logging.handlers.RotatingFileHandler(logfile, maxBytes=MAX_LOGFILE_BYTE, backupCount=MAX_LOG_COUNT)
        formatter = logging.Formatter('<%(asctime)s> <%(levelname)s> <%(module)s:%(lineno)d>\t%(message)s', datefmt='%F %T')
        ch.setFormatter(formatter)
        logger.addHandler(ch)
        logger.setLevel(logging.ERROR)
    return logger

WEB_LOG_FILE  = '/var/log/cloudmonitor/monitor.log'

def getMonitorLogger():
    my_logger = init_log(WEB_LOG_FILE)
    return my_logger
