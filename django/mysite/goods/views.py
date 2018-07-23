from django.shortcuts import render
from django.db.models import Q
from goods.models import Goods

# Create your views here.
def index(request):
    return render(request, 'goods_index.html')

def searchall(request):
    goods_list = Goods.objects.all()
    return render(request, 'search_result.html', {'goods_list': goods_list})

def searchname(request):
    goods_name = request.GET['goods_name']
    goods_list = Goods.objects.filter(goods_name=goods_name)  # 完全匹配搜索关键字
    # goods_list = Goods.objects.get(goods_name=goods_name)# 查询满足条件的一个结果（查询到多个结果时异常）
    # goods_list = Goods.objects.filter(goods_name__contains=goods_name)  # 模糊匹配搜索关键字
    return render(request, 'search_result.html', {'goods_list': goods_list})

def searchprice(request):
    min_price = request.GET['min_price']
    max_price = request.GET['max_price']
    goods_list = Goods.objects.filter(goods_price__gt=min_price, goods_price__lt=max_price)  # 满足全部多个条件
    # goods_list = Goods.objects.filter(Q(goods_price=0.5) | Q(goods_price=2.4)) # 满足任何一个条件
    return render(request, 'search_result.html', {'goods_list': goods_list})

def searchsort(request):
    sort = {'all_asc': Goods.objects.order_by('goods_price'),  # 查询全部结果后升序排列
            'all_desc': Goods.objects.order_by('-goods_price'),  # 查询全部结果后降序排列
            'result_asc': Goods.objects.filter(goods_price__lt='5').order_by('goods_price')  # 对某一查询结果排序
            }
    return render(request, 'search_result.html', {'goods_list': sort[request.GET['sort']]})
