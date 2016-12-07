#oding = utf-8
# -*- coding:utf-8 -*-
from log.log import LogConfig
from brower.brower import BrowserFactory
from brower.brower import BrowserType
from web.webparser import WebParser
from web.webparser import WebParserMethodType

import logging

if __name__ == '__main__':
    brower = BrowserFactory.createBrowser(BrowserType.firefox, "")
    try:
        LogConfig()
        logging.debug(u"xxx12344")
        url = "https://www.baidu.com/"
        brower.get(url)
        element = WebParser.getElement(brower, WebParserMethodType.id, "kw")
        element.send_keys("11111")
        element.submit()
    except Exception,e:
        print  Exception,":",e
