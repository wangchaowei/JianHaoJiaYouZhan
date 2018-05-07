# -*- coding: utf-8 -*-
# __author__ = 'WangChaoWei'
# __date__ = '2018/5/7 18:36'
import xadmin
from xadmin import views
from .models import Table


class TableSetting(object):
    enable_themes = True
    use_bootswatch = True


class TableAdmin(object):
    list_display = ['order_number', 'user_name', 'tel', 'add', 'oil', 'liter', 'total_price', 'arrived_time', 'remark']


xadmin.site.register(Table, TableAdmin)