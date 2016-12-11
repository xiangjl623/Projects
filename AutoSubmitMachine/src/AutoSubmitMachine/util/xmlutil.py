#oding = utf-8
# -*- coding:utf-8 -*-
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element

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
           #print dir(parent.iter(tag))
           return parent.iter(tag).next()
        except:
           return None

    @staticmethod
    def getSubElementText(parent, tag):
        try:
           return parent.iter(tag).next().text
        except:
           return None