#oding = utf-8
# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from browser.browser import Browser

class BrowserType(object):
  ie = "ie"
  chrome = "chrome"
  firefox = "firefox"

class BrowserFactory(object):
    @staticmethod
    def openBrowser(browerType, driverPath = None):
        if browerType.lower() == BrowserType.ie: #"IEDriverServer.exe PATH"
            return Browser(webdriver.Ie(driverPath))
        elif browerType.lower() == BrowserType.chrome: # "chromedriver.exe PATH"
            return Browser(webdriver.Chrome(driverPath))
        elif browerType.lower() == BrowserType.firefox:
            return Browser(webdriver.Firefox("C:\\Program Files\\Mozilla Firefox\\firefox.exe"))