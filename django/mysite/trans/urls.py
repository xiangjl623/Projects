#oding = utf-8
# -*- coding:utf-8 -*-

from django.urls import path

from . import views

urlpatterns = [
    path('', views.translate),
]