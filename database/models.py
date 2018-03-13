from django.db import models

# Create your models here.


class Quotes(models.Model):
    serial = models.IntegerField()
    project_num = models.IntegerField()
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


class Orders(models.Model):
    project_name = models.ForeignKey(Quotes,
                                     on_delete=models.CASCADE)
    amount = models.IntegerField(blank=True,
                                 null=True,
                                 verbose_name='工程量')
