from django.contrib import admin


# Register your models here.
from myblog.models import Article


# 注册模型(数据表)
admin.site.register(Article)
