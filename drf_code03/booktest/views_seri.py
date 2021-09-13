# -*- coding: utf-8 -*-

# 这个文件主要是用来暂时保存在 python manage.py shell 中要执行的代码，到时候将这些代码直接拷贝到终端就可以去执行了

from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

# ==========序列化单个书籍对象=========

from booktest.serializers import BookInfoSerializer
from booktest.models import BookInfo
# 获取书籍对象
book = BookInfo.objects.get(id=1)
# 创建序列化器，instance 表示要序列化的对象
serializer = BookInfoSerializer(instance=book)
# 转换数据
print serializer.data


# ============序列化多个书籍对象============
from booktest.serializers import BookInfoSerializer
from booktest.models import BookInfo
# 获取书籍对象
books = BookInfo.objects.all()
# 创建序列化器，instance 表示要序列化的对象
serializer = BookInfoSerializer(instance=books, many=True)
# 转换数据
print serializer.data


# ==========序列化单个英雄对象=========
from booktest.serializers import HeroInfoSerializer
from booktest.models import HeroInfo
# 获取英雄对象
hero = HeroInfo.objects.get(id=1)
# 创建序列化器，instance 表示要序列化的对象
serializer = HeroInfoSerializer(instance=hero)
# 转换数据
print serializer.data


# ==========序列化器 反序列化 书籍对象=========
from booktest.serializers import BookInfoSerializer

# 准备数据
book_dict = {
    "btitle": u"金瓶book",
    "bpub_date": "1990-1-1",
    "bread": 10,
    "bcomment": 15
}

# 创建序列化器校验
serializer = BookInfoSerializer(data=book_dict)

serializer.is_valid(raise_exception=True)
# 转换数据
print serializer.data


# ==========序列化器 反序列化 create 保存数据=========
from booktest.serializers import BookInfoSerializer

# 准备数据
book_dict = {
    "btitle": u"金瓶book",
    "bpub_date": "2018-1-1",
    "bread": 10,
    "bcomment": 5
}

# 创建序列化器校验
serializer = BookInfoSerializer(data=book_dict)

serializer.is_valid(raise_exception=True)
# 保存数据
serializer.save()


# ==========序列化器 反序列化 update 更新数据=========
from booktest.serializers import BookInfoSerializer
from booktest.models import BookInfo
# 准备数据
book_dict = {
    "btitle": u"金瓶bookx1",
    "bpub_date": "2018-1-1",
    "bread": 10,
    "bcomment": 5
}

book = BookInfo.objects.get(id=1)
# 创建序列化器校验
serializer = BookInfoSerializer(instance=book, data=book_dict)

serializer.is_valid(raise_exception=True)
# 保存数据
serializer.save()




