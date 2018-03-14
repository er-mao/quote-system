from django.db import models

# Create your models here.


class Orders(models.Model):
    """
    采购单
    """
    serial = models.IntegerField(unique=True,
                                 verbose_name='序号')
    project_num = models.IntegerField(primary_key=True,
                                      verbose_name='项目编号')
    project_name = models.CharField(max_length=200,
                                    blank=True,
                                    null=True,
                                    verbose_name='项目名称')
    project_describe = models.CharField(max_length=200,
                                        blank=True,
                                        null=True,
                                        verbose_name='项目特征描述')
    unit = models.CharField(max_length=200,
                            blank=True,
                            null=True,
                            verbose_name='计量单位')
    amount = models.IntegerField(blank=True,
                                 null=True,
                                 verbose_name='工程量')
    create_time = models.DateField(auto_now=True,
                                   verbose_name='创建日期')
    deadline = models.DateField(blank=True,
                                null=True,
                                verbose_name='截至日期')
    comment = models.CharField(max_length=200,
                               blank=True,
                               null=True,
                               verbose_name='备注')


class Quotes(models.Model):
    """
    报价
    """
    requirement = models.OneToOneField('Orders',
                                       on_delete=models.CASCADE)
    unit_price = models.IntegerField(verbose_name='单价')
    total_price = models.IntegerField(verbose_name='总价')
