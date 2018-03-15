from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Order(models.Model):
    order_name = models.CharField(max_length=20,
                                    verbose_name="订单名称",)
    order_time = models.DateTimeField(verbose_name="订单时间")
    create_time = models.DateField(auto_now=True,
                                   verbose_name='创建日期')
    deadline = models.DateField(blank=True,
                                null=True,
                                verbose_name='截至日期')
    def __str__(self):
        return self.order_name
    class Meta:
        verbose_name = "订单"
        verbose_name_plural = "订单"

class Project(models.Model):
    """
    项目
    """
    order_of_project = models.ForeignKey(Order, 
                                        on_delete=models.CASCADE, 
                                        verbose_name="所属项目")
    project_index = models.IntegerField(unique=True,
                                        verbose_name='序号')
    project_num = models.IntegerField(primary_key=True,
                                      verbose_name='项目编号')
    project_name = models.CharField(max_length=200,
                                    verbose_name='项目名称')
    project_description = models.TextField(verbose_name='项目特征描述')
    project_unit = models.CharField(max_length=200,
                                    verbose_name='计量单位')
    project_amount = models.IntegerField(default=1,
                                        verbose_name='工程量')
    project_note = models.CharField(max_length=200,
                                    blank=True,
                                    verbose_name='备注')
    def __str__(self):
        return self.project_description
    class Meta:
        verbose_name = "项目"
        verbose_name_plural = "项目"

class Provider(models.Model):
    """
    供应商报价
    """
    provider_name = models.ForeignKey(User, 
                                        on_delete=models.CASCADE)
    provider_order = models.ForeignKey(Order, 
                                        on_delete=models.CASCADE)
    provider_price = models.CharField(max_length=20)
    created_time = models.DateTimeField(auto_now=False,
                                        verbose_name='报价时间')
    modified_time = models.DateTimeField(auto_now=False,
                                        verbose_name='修改时间')
    unit_price = models.IntegerField(verbose_name='单价')
    def __str__(self):
        return self.provider_name
    class Meta:
        verbose_name = "供应商报价"
        verbose_name_plural = "供应商报价"