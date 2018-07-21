#oding = utf-8
# -*- coding:utf-8 -*-

from django.shortcuts import render  # 创建应用时自动导入的模块

def index(request):  # 定义站点首页视图函数
    return render(request, 'index.html')  # 调用模板返回页面内容

def news_list(request, news_type):  # 定义新闻列表视图
    news_dict = {'economic': '经济', 'sport': '体育'}  # 创建参数字典
    return render(request, 'news_list.html', {'news_type': news_dict[news_type]})  # 整合数据并返回页面内容