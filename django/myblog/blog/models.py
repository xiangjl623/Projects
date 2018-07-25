from django.db import models
from django.contrib.auth.models import User  # 使用Django自带的用户模型
from django.db.models import Q  # 帮助完成查询条件设置
from django.views.generic import ListView, DetailView
# Create your models here.

class Category(models.Model):  # 文章类别
    id = models.IntegerField(primary_key=True)
    name = models.CharField('类别', max_length=20, unique=True)

    class Meta:
        verbose_name_plural = verbose_name = '类别'

    def __str__(self):
        return self.name

class Tag(models.Model):  # 文章标签
    name = models.CharField('标签', max_length=20, unique=True)

    class Meta:
        verbose_name_plural = verbose_name = '标签'

    def __str__(self):
        return self.name

class Article(models.Model):  # 文章
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='作者')  #第2个关键字参数则是指定当外键指向的数据对象被删除“on_delete”时，如何进行处理，这里的值为“models.DO_NOTHING”，即不做任何处理；
    title = models.CharField('标题', max_length=50)
    content = models.TextField('内容')
    pub_time = models.DateField('日期', auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=1, verbose_name='类别')
    tag = models.ManyToManyField(Tag, verbose_name='标签')

    class Meta:
        verbose_name_plural = verbose_name = '文章'

    def __str__(self):
        return self.title

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('昵称', max_length=20)
    email = models.EmailField('邮箱')
    content = models.TextField('内容')
    publish = models.DateField('时间', auto_now=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='文章')
    reply = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name='回复')

    class Meta:
        verbose_name_plural = verbose_name = '评论'

    def __str__(self):
        return self.content

class Search(ListView):
    model = Article
    template_name = 'search.html'
    paginate_by = 5

    def get_queryset(self):
        key = self.request.GET['key']  # 获取查询关键字
        if key:
            return Article.objects.filter(Q(title__icontains=key) | Q(content__icontains=key)).order_by('-id')
            # 查询标题或者内容包含关键字的数据对象
        else:
            return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = self.request.GET['key']  # 获取关键字存入传入模板的数据中
        return context
