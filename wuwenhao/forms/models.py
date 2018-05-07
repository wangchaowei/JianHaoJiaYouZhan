# coding:utf-8
from __future__ import unicode_literals

from django.db import models
from datetime import datetime


class Table(models.Model):
    order_number = models.CharField(max_length=50, verbose_name=u'订单号', default='')
    user_name = models.CharField(max_length=50, verbose_name=u'联系人', default='')
    tel = models.CharField(max_length=50, verbose_name=u'电话', default='')
    add = models.CharField(max_length=50, verbose_name=u'地址', default='')
    oil = models.CharField(max_length=50, verbose_name=u'油品', default='')
    liter = models.IntegerField(default=0, verbose_name=u'升数')
    total_price = models.IntegerField(default=0, verbose_name=u'总价')
    arrived_time = models.DateTimeField(default=datetime.now, verbose_name=u'最晚送达时间')
    remark = models.TextField(default='', verbose_name=u'备注')

    class Meta:
        verbose_name = '表单'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.order_number

