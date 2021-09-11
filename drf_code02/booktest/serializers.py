# -*- coding: utf-8 -*-

from rest_framework import serializers


# ========定义书籍序列化器========
class BookInfoSerializer(serializers.Serializer):
    # 与模型类保持一致
    # label 就相当于一个注释说明
    id = serializers.IntegerField(label='id', read_only=True)
    btitle = serializers.CharField(max_length=20, label='名称')
    bpub_date = serializers.DateField(label='发布日期')
    bread = serializers.IntegerField(default=0, label='阅读量')
    bcomment = serializers.IntegerField(default=0, label='评论量')
    is_delete = serializers.BooleanField(default=False, label='逻辑删除')
    # 关联英雄主键，一本书里会有那些英雄
    # heroinfo_set = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    heroinfo_set = serializers.StringRelatedField(read_only=True, many=True)


# 定义英雄序列化器
class HeroInfoSerializer(serializers.Serializer):
    GENDER_CHOICES = (
        (0, 'female'),
        (1, 'male')

    )
    id = serializers.IntegerField(label='ID ', read_only=True)
    hname = serializers.CharField(max_length=20, label='名称')
    hgender = serializers.ChoiceField(choices=GENDER_CHOICES, label='性别')
    hcomment = serializers.CharField(max_length=200, allow_null=True, label='描述信息')
    
    # hbook = serializers.PrimaryKeyRelatedField(read_only=True)
    # hbook = serializers.StringRelatedField(read_only=True)
    hbook = BookInfoSerializer()

















