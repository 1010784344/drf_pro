# -*- coding: utf-8 -*-
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









