#! python3
# coding: utf-8
import logging
from logging import handlers
import os,sys

class Logger:
    level_relations = {
        'debug':logging.DEBUG, #DEBUG
        'info':logging.INFO, #INFO
        'warning':logging.WARNING, #告警
        'error':logging.ERROR, #错误
        'crit':logging.CRITICAL #严重
    }

    def __init__(self, logname="all.log", logpath=None, when='D', backcount=7, fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s'):
        self.logname = logname
        if logpath == None:
            self.logpath = sys.path[0] + '/log'
        else:
            self.logpath = logpath
        self.logfilename = self.logpath + '/' + logname
        self.when = 'D'
        self.backcount = 7
        self.fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'        

    def printconsole(self, level, message):
        self.logger = logging.getLogger('logger')
        format_str = logging.Formatter(self.fmt)#设置日志格式
        self.logger.setLevel(self.level_relations.get(level))#设置日志级别
        sh = logging.StreamHandler()#往屏幕上输出
        sh.setFormatter(format_str) #设置屏幕上显示的格式
        th = handlers.TimedRotatingFileHandler(filename=self.logfilename,when=self.when,backupCount=self.backcount,encoding='utf-8')#往文件里写入#指定间隔时间自动生成文件的处理器
        #实例化TimedRotatingFileHandler
        #interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
        # S 秒
        # M 分
        # H 小时、
        # D 天、
        # W 每星期（interval==0时代表星期一）
        # midnight 每天凌晨
        th.setFormatter(format_str)#设置文件里写入的格式
        self.logger.addHandler(sh) #把对象加到logger里
        self.logger.addHandler(th)
        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        elif level == 'crit':
            self.logger.critical(message)
        self.logger.removeHandler(sh)
        self.logger.removeHandler(th)

    def debug(self,message):
        self.printconsole('debug', message)

    def info(self,message):
        self.printconsole('info', message)

    def warning(self,message):
        self.printconsole('warning', message)

    def error(self,message):
        self.printconsole('error', message)

    def crit(self,message):
        self.printconsole('crit', message)

if __name__ == '__main__':
    log = Logger()
    log.info('info msg1000013333')
    log.debug('debug msg')
    log.warning('warning msg')
    log.error('error msg')