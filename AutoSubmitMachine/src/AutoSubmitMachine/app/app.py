#oding = utf-8
# -*- coding:utf-8 -*-
from util.xmlutil import XmlUtil
from brower.seleniumbrowser import SeleniumBrowser
from brower.seleniumbrowserfactory import  SeleniumBrowserFactory

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
        if self.type.lower() == ActionType.url:
            brower.load(self.url)
        elif self.type.lower() == ActionType.element:
            oElement = brower.find_element(self.by, self.value)
            oElement.clear()
            oElement.send_keys(self.key)
            oElement.submit()

class App(object):
    def __init__(self, file):
        doc = XmlUtil.load(file)
        root = doc.getroot()
        self.BrowserConfig = BrowserConfig(XmlUtil.getSubElement(root, "browserconfig"))
        self.Actions = []
        ActionsNode = XmlUtil.getSubElement(root, "actions")
        for actionNode in ActionsNode:
            self.Actions.append(Action(actionNode))

    def excute(self):
        browser = SeleniumBrowserFactory.openBrowser(self.BrowserConfig.name, self.BrowserConfig.driverpath)
        for action in self.Actions:
            try:
                action.excute(browser)
            except Exception,e:
                print  Exception,":",e