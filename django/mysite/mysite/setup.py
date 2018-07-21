#oding = utf-8
# -*- coding:utf-8 -*-
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")  # 关联默认设置
django.setup()  # 装载Django