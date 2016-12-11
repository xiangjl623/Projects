#oding = utf-8
# -*- coding:utf-8 -*-
from app import App
from log.log import LogConfig
import logging

LogConfig()
logging.debug(u"start work")

appDataConfig = App("config//AppDataConfig.xml")
appDataConfig.excute()