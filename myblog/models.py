from django.db import models

# Create your models here.

"""
常用命令

生成迁移文件
manage.py makemigrations [app名称]

数据库迁移
manage.py migrate

查看sql语句
manage.py sqlmigrate myblog 0001
"""


class Article(models.Model):
    """如果不手动设置主键，则会自动设置一个名为id的自增主键"""
    title = models.CharField(max_length=32, default='Title')
    content = models.TextField(null=True)

    def __str__(self):
        """
        修改在django后台的默认显示名称，使之不再显示为Article object
        :return: title内容
        """
        return self.title
