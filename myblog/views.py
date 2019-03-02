from django.shortcuts import render
from django.http import HttpResponse
from . import models


# Create your views here.


def root_page(request):
    # 直接返回
    return HttpResponse('Hello django')


def template_demo(request):
    # 返回渲染模板

    # render支持3个参数，第三个为参数接受一个字典，用于后台传递传递参数到模板
    args_dict = {'name': 'bob',
                 'article': models.Article.objects.all()}
    return render(request, 'index.html', args_dict)

    # 注意：django会按照INSTALLED_APPS中的顺序在各app中的templates文件夹下查找html文档，如果各app中的模板同名，会直接使用第一个
    # 解决方法，可以在templates目录下再建一个不同名的次级目录，在这里面存放模板


def article_d(request, aid):
    args_dict = {
        'article': models.Article.objects.get(pk=aid)
    }
    return render(request, 'detail.html', args_dict)
