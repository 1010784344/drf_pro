# -*- coding: utf-8 -*-

from rest_framework import serializers
from .models import BookInfo


# ========定义书籍模型类序列化器========
class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        # 参考模型类生成字段
        model = BookInfo
        # 生成所有字段
        # fields = "__all__"

        # 生成指定的字段
        fields = ['id', 'btitle', 'bpub_date']

        # 设置只读字段
        read_only_fields = ['btitle', 'bpub_date']

        # 给生成的字段添加额外的约束
        extra_kwargs = {

            'bread': {
                'max_value': 999,
                'min_value': 0

            },
            'bcomment': {
                'max_value': 888,
                'min_value': 0
            }

        }



















