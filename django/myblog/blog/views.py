from django.shortcuts import render
from django.views.generic import ListView
from .models import *



# Create your views here.
class Index(ListView):
    model = Article
    template_name = 'index.html'
    queryset = Article.objects.all().order_by('-id')  # 获取到全部文章并按编号降序排列。
    paginate_by = 5  # 设置分页时每页的文章数量

class CategoryList(ListView):
    model = Article
    template_name = 'category.html'
    paginate_by = 5

    def get_queryset(self):  # 定义通过分类查询的QuerySet
        return Article.objects.filter(category=self.kwargs['category']).order_by('-id')  # 按参数传入的分类id进行查询并按文章编号降序排序

    def get_context_data(self, **kwargs):  # 增加额外要传递给模板的数据
        context = super().get_context_data(**kwargs)
        category = Category.objects.get(id=self.kwargs['category'])  # 通过分类id查询分类对象
        context['category'] = category.name  # 将分类对象的名称存入传递给模板的数据中
        return context