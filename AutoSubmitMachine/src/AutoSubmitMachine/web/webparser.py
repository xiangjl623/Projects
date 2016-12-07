#oding = utf-8
# -*- coding:utf-8 -*-
from enum import Enum

class WebParserMethodType(Enum):
    id = 1
    name = 2
    xpath = 3
    tag_name = 4
    class_name = 5
    css = 6
    link_text = 7

class WebParser(object):
    @staticmethod
    def getElement(browser, webParserMethodType, key):
        if webParserMethodType == WebParserMethodType.id:
            return browser.find_element_by_id(key)
        elif webParserMethodType == WebParserMethodType.name:
            return browser.find_element_by_name(key)
        elif webParserMethodType == WebParserMethodType.xpath:
            return browser.find_element_by_xpath(key),
        elif webParserMethodType == WebParserMethodType.tag_name:
            return browser.find_element_by_tag_name(key)
        elif webParserMethodType == WebParserMethodType.class_name:
            return browser.find_element_by_class_name(key)
        elif webParserMethodType == WebParserMethodType.css:
            return browser.find_element_by_css_selector(key)
        elif webParserMethodType == WebParserMethodType.link_text:
            return browser.find_element_by_link_text(key)