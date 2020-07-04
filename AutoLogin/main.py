from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from xml.etree.ElementTree import ElementTree
import os,sys
import logging
import time,datetime

#driver = webdriver.Firefox()
#driver.get("http://www.aiquanti.com/loginPage")
#user = driver.find_element_by_name("account")
#user.clear()
#user.send_keys("zhangj")
#user.send_keys(Keys.RETURN)
#password = driver.find_element_by_name("password")
#password.send_keys("baizhi13")
#password.send_keys(Keys.RETURN)
#submit = driver.find_element_by_id("login_submit")
#submit.click()
#driver.get("http://www.aiquanti.com/sysConfigItem/selectDetail/1269784")
#driver.close()

class LogConfig(object):
    def __init__(self, level = 0):
        AppPath = os.path.abspath(sys.argv[0])
        self.AppDir = os.path.dirname(AppPath) + "//"
        datetimeNow = datetime.datetime.now().strftime("%Y%m%d_%H_%M_%S")
        fileName = self.AppDir + "run.log"
        logging.basicConfig(level = level,
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

class XmlUtil(object):
    @staticmethod
    def load(file):
        et = ElementTree()
        et.parse(file)
        return et

    @staticmethod
    # xml.etree.ElementTree SubElement需要传入属性 不好用
    def getSubElement(parent, tag):
        try:
             return parent.iter(tag)
        except Exception as e:
             print(Exception, ":", e)
             return  None

    @staticmethod
    def getSubElementText(parent, tag):
        try:
             return parent.iter(tag).text
        except Exception as e:
             print(Exception, ":", e)
             return  None

class Action(object):
    def __init__(self, xmlnode):
        for child in xmlnode:
           setattr(self, child.tag.lower(), child.text)
    def excute(self, brower):
        try:
            if self.type.lower() == "url":
                brower.get(self.url)
            elif self.type.lower() == "value":
                oElement = brower.find_element(self.by, self.value)
                oElement.clear()
                oElement.send_keys(self.key)
                oElement.send_keys(Keys.RETURN)
            elif self.type.lower() == "button":
                oButton = brower.find_element(self.by, self.value)
                oButton.click()
        except Exception as e:
            print(Exception + ":" + e)

LogConfig()
doc = XmlUtil.load("configs//config.xml")
root = doc.getroot()
userNodes = XmlUtil.getSubElement(root, "user")
for userNode in userNodes:
    driver = webdriver.Firefox()
    actionNodes = XmlUtil.getSubElement(userNode, "action")
    for actionNode in actionNodes:
       action = Action(actionNode)
       action.excute(driver)
