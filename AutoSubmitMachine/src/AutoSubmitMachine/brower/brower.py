#oding = utf-8
# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from enum import Enum

class BrowserType(Enum):
    ie = 1
    chrome = 2
    firefox = 3

class BrowserFactory(object):
    @staticmethod
    def createBrowser(browerType, driverPath):
        if browerType == BrowserType.ie:
            #"IEDriverServer.exe PATH"
            return webdriver.Ie(driverPath)
        elif browerType ==  BrowserType.chrome:
            # "hromedriver.exe PATH"
            return webdriver.Chrome(driverPath)
        elif browerType == BrowserType.firefox:
            return webdriver.Firefox()