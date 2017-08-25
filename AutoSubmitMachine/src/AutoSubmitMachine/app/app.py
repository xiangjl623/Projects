#oding = utf-8
# -*- coding:utf-8 -*-
from utils.xmlutil import XmlUtil
from browser.browser import Browser
from browser.browserfactory import BrowserFactory
from log.log import LogConfig
import time

class ActionType(object):
    url = "url"
    element = "element"

#property Name DriverPath
class BrowserConfig(object):
    def __init__(self, xmlnode):
        for child in xmlnode:
           setattr(self, child.tag.lower(), child.text)

##property ActionType
class Action(object):
    def __init__(self, xmlnode):
        for child in xmlnode:
           setattr(self, child.tag.lower(), child.text)
    def excute(self, brower):
        try:
            if self.type.lower() == ActionType.url:
                brower.load(self.url)
            elif self.type.lower() == ActionType.element:
                oElement = brower.find_element(self.by, self.value)
                #print dir(self)
                if hasattr(self, "child_by") and hasattr(self, "child_value"):
                    oElement = oElement.find_elemnt(self.child_by, self.child_value)
                if hasattr(self, "clear"):
                    oElement.clear()
                if hasattr(self, "key"):
                    oElement.send_keys(self.key)
                if hasattr(self, "click"):
                    oElement.click()
                if hasattr(self, "submit"):
                    oElement.submit()
                if hasattr(self, "delaytime"):
                    time.sleep(int(self.delaytime))
        except Exception as e:
            print(Exception + ":" + e)

class App(object):
    def __init__(self, file):
        doc = XmlUtil.load(file)
        root = doc.getroot()
        if XmlUtil.getSubElement(root, "log") != None:
            LogConfig()
        self.BrowserConfig = BrowserConfig(XmlUtil.getSubElement(root, "browser"))
        self.Actions = []
        ActionsNode = XmlUtil.getSubElement(root, "actions")
        for actionNode in ActionsNode:
            self.Actions.append(Action(actionNode))

    def excute(self):
        browser = BrowserFactory.openBrowser(self.BrowserConfig.name, self.BrowserConfig.driverpath)
        for action in self.Actions:
            try:
                action.excute(browser)
            except Exception as e:
                print(Exception + ":" + e)