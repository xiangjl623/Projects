#oding = utf-8
# -*- coding:utf-8 -*-
import os
import django
import sys
sys.path.append("F:\\09 Python\django\\test\\mysite");   # 项目位置 易错点
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")  # 关联默认设置
django.setup()  # 装载Django

from goods.models import Goods

with open('data.txt', 'r', encoding='utf-8') as file:  # 打开文件创建文件对象（注意编码）
    for line in file:  # 读取每一行
       lst = line.strip().split(',')  # 将每一行中的商品信息转换为列表
       state = Goods.objects.create(goods_name=lst[0], goods_number=lst[1], goods_price=lst[2])  # 添加数据到数据库
       print(state)  # 显示输出添加数据的结果

print(Goods.objects.all());

print(Goods.objects.values());