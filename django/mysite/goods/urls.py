from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('all/', views.searchall),
    path('search_name/', views.searchname),
    path('search_price/', views.searchprice),
    path('search_sort/', views.searchsort)
]
