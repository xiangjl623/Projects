#oding = utf-8
# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from seleniumbrowser import SeleniumBrowser

class BrowserType(object):
    ie = "ie"
    chrome = "chrome"
    firefox = "firefox"

class SeleniumBrowserFactory(object):
    @staticmethod
    def openBrowser(browerType, driverPath = None):
        if browerType.lower() == BrowserType.ie: #"IEDriverServer.exe PATH"
            return SeleniumBrowser(webdriver.Ie(driverPath))
        elif browerType.lower() == BrowserType.chrome: # "chromedriver.exe PATH"
            return SeleniumBrowser(webdriver.Chrome(driverPath))
        elif browerType.lower() == BrowserType.firefox:
            return SeleniumBrowser(webdriver.Firefox())