from django.db import models

# Create your models here.
class Goods(models.Model):
    goods_name = models.CharField('商品名称',max_length=30)
    goods_number = models.IntegerField('数量')
    goods_price = models.FloatField('价格')
    goods_sales = models.IntegerField('销量', default=0)
    class Meta:
        verbose_name_plural = "商品管理"
        verbose_name = "商品"
    def __str__(self):
       return self.goods_name

    def sales_volume(self):
        return self.goods_sales * self.goods_price

    sales_volume.short_description = '销售额'
    goods_amount = property(sales_volume)