#oding = utf-8
# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

class BrowerFactory:
    @staticmethod
    def createBrower(type, driverPath):
        if type.lower() == "ie":
            #oschromedriver = "C:\Program Files\Internet Explorer\IEDriverServer.exe"
            os.environ["brower.ie.brower"] = driverPath
            return webdriver.Ie(driverPath)
        elif type.lower() == "chrome":
            #chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
            os.environ["brower.chrome.brower"] = driverPath
            return webdriver.Chrome(driverPath)
        elif type.lower() == "firefox":
            return webdriver.Firefox()





#