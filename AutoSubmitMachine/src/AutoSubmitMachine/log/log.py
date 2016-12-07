#oding = utf-8
# -*- coding:utf-8 -*-
import os,sys
import logging
import time,datetime

class LogConfig(object):
    def __init__(self):
        AppPath = os.path.abspath(sys.argv[0])
        self.AppDir = os.path.dirname(AppPath) + "//"
        datetimeNow = datetime.datetime.now().strftime("%Y%m%d_%H_%M_%S")
        fileName = self.AppDir + "logFile//" + datetimeNow + ".log"
        logging.basicConfig(level=logging.DEBUG,
                 format = "%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s",
                 datefmt = "%Y%m%d_%H:%M:%S",
                 filename = fileName,
                 filemode = "w")
        #################################################################################################
        #定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
        console = logging.StreamHandler()
        formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
        console.setFormatter(formatter)
        logging.getLogger('').addHandler(console)
        #################################################################################################
        # DEBUG：详细的信息,通常只出现在诊断问题上
        # INFO:确认一切按预期运行
        # WARNING:一个迹象表明,一些意想不到的事情发生了,或表明一些问题在不久的将来(例如。磁盘空间低”)。这个软件还能按预期工作。
        # ERROR:个更严重的问题,软件没能执行一些功能
        # CRITICAL:一个严重的错误,这表明程序本身可能无法继续运行
        # logging.debug('This is debug message')
        # logging.info('This is info message')
        # logging.warning('This is warning message')
        # logging.error('This is warning message')