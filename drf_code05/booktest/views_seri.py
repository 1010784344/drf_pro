# -*- coding: utf-8 -*-

# 这个文件主要是用来暂时保存在 python manage.py shell 中要执行的序列化代码，到时候将这些代码直接拷贝到终端就可以去执行了

from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

# ==========使用模型类序列化器，测试序列化=========

from booktest.serializers import BookModelSerializer
from booktest.models import BookInfo
# 获取书籍对象
book = BookInfo.objects.get(id=1)
# 创建序列化器，instance 表示要序列化的对象
serializer = BookModelSerializer(instance=book)
# 转换数据
print serializer.data


# ==========使用模型类序列化器 测试反序列化 入库操作 =========
from booktest.serializers import BookModelSerializer

# 准备数据
book_dict = {
    "btitle": u"鹿鼎记",
    "bpub_date": "2018-1-1",
    "bread": 10,
    "bcomment": 5
}

# 创建序列化器校验
serializer = BookModelSerializer(data=book_dict)

serializer.is_valid(raise_exception=True)
# 保存数据
serializer.save()

# ==========使用模型类序列化器 测试反序列化 更新操作 =========
from booktest.serializers import BookModelSerializer
from booktest.models import BookInfo

book = BookInfo.objects.get(id=5)

# 准备数据
book_dict = {
    "btitle": u"鹿鼎记x1",
    "bpub_date": "2018-1-1",
    "bread": 100,
    "bcomment": 5
}

# 创建序列化器校验
serializer = BookModelSerializer(instance=book, data=book_dict)

serializer.is_valid(raise_exception=True)
# 保存数据
serializer.save()




