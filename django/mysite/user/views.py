from django.shortcuts import render, HttpResponse
from user.models import Users
import json


# Create your views here.
def reg(request):
    return render(request, 'register.html')


def change(request):
    return render(request, 'change.html')


def check(request):
    user_name = request.GET['user_name']
    user = Users.objects.filter(user_name=user_name)
    if user:
        status = 100  # 返回表示已注册的编号
    else:
        status = 200  # 返回表示未注册的编号
    return HttpResponse(status)


def register(request):
    user_name = request.GET['user_name']
    password = request.GET['password']
    try:
        user = Users(user_name=user_name, password=password)
        user.save()
        status = 200  # 返回注册成功的编号
    except:
        status = 100  # 返回注册失败的编号
    return HttpResponse(json.dumps({'status': status}))


def changepass(request):
    user_name = request.GET['user_name']
    password = request.GET['password']
    user = Users.objects.filter(user_name=user_name)  # 查询已存在用户的数据对象
    try:
        user.update(password=password)  # 通过数据对象更新数据库中的数据
        status = 200
    except:
        status = 100
    return HttpResponse(json.dumps({'status': status}))
