#oding = utf-8
# -*- coding:utf-8 -*-
from brower.brower import BrowerFactory

if __name__ == '__main__':
    brower = BrowerFactory.createBrower("firefox", "")
    try:
        url = "https://www.baidu.com/"
        brower.get(url)
    except Exception,e:
        print  Exception,":",e
