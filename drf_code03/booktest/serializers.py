# -*- coding: utf-8 -*-

from rest_framework import serializers
from .models import BookInfo


# 自定义校验方法
def check_bpub_date(value):
    # value 代表的是传参 bpub_date
    if value.year < 2018:
        raise serializers.ValidationError('书籍的年份要大于 2018年')
    return value


# ========定义书籍序列化器========
class BookInfoSerializer(serializers.Serializer):
    # 与模型类保持一致
    # label 就相当于一个注释说明
    id = serializers.IntegerField(label='id', read_only=True)
    btitle = serializers.CharField(max_length=20, label='名称')
    bpub_date = serializers.DateField(label='发布日期', validators=[check_bpub_date])
    bread = serializers.IntegerField(default=0, label='阅读量')
    bcomment = serializers.IntegerField(default=0, label='评论量')
    is_delete = serializers.BooleanField(default=False, label='逻辑删除')
    # 关联英雄主键，一本书里会有那些英雄
    # heroinfo_set = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    # heroinfo_set = serializers.StringRelatedField(read_only=True, many=True)

    # 单字段校验（反）
    def validate_btitle(self, value):
        # 校验 value 中的内容
        if not 'book' in value:
            raise serializers.ValidationError('书籍名不包含 ')
        return value

    # 多字段校验（反）
    def validate(self, attrs):
        read = attrs['bread']
        comment = attrs['bcomment']
        if comment > read:
            raise serializers.ValidationError('评论量大于了阅读量')
        return attrs

    def create(self, validated_data):
        # validated_data：校验成功之后的数据

        # 创建 book 对象，设置属性，入库
        book = BookInfo(**validated_data)

        return book

    def update(self, instance, validated_data):
        # instance 外界传入的 book 对象
        # validated_data 校验成功之后的 book_dict 数据

        # 更新数据
        instance.btitle = validated_data['btitle']
        instance.bpub_date = validated_data['bpub_date']
        instance.bread = validated_data['bread']
        instance.bcomment = validated_data['bcomment']
        # 入库
        instance.save()
        # 返回
        return instance




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

















