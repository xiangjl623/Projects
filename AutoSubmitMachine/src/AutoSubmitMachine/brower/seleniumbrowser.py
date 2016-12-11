#oding = utf-8
# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class SeleniumBrowser(object):
   def __init__(self, driver):
       self.driver = driver

   def getDriver(self):
       return self.driver

   def quit(self):
       self.driver.quit()

   def load(self, url):
        self.driver.get(url)

   def excuteScript(self, script, *args):
       self.driver.execute_script(script, args)

   def getUrl(self):
        return self.driver.getCurrentUrl()

   def refresh(self):
        self.driver.navigate().refresh()

   def getWindowHandel(self, index):
       return self.driver.window_handles[index]

   def switchToWindow(self, handle):
       self.driver.switch_to.window(handle)

    # ID = "id"
    # XPATH = "xpath"
    # LINK_TEXT = "link text"
    # PARTIAL_LINK_TEXT = "partial link text"
    # NAME = "name"
    # TAG_NAME = "tag name"
    # CLASS_NAME = "class name"
    # CSS_SELECTOR = "css selector"
   def find_element(self, by=By.ID, value=None):
        if by == By.ID:
            return self.driver.find_element_by_id(value)
        elif by == By.XPATH:
            return self.driver.find_element_by_xpath(value)
        elif by  == By.LINK_TEXT:
            return self.driver.find_element_by_link_text(value)
        elif by  == By.PARTIAL_LINK_TEXT:
            return self.driver.find_element_by_partial_link_text(value)
        elif by  == By.NAME:
            return self.driver.find_element_by_name(value)
        elif by  == By.TAG_NAME:
            return self.driver.find_element_by_tag_name(value)
        elif by  == By.CSS_SELECTOR:
            return self.driver.find_element_by_css_selector(value)
        elif by  == By.CLASS_NAME:
            return self.driver.find_element_by_class_name(value)