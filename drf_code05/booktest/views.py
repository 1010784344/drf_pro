# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django import http
from booktest.models import BookInfo
import json
from serializers import BookModelSerializer


#1, 序列化器和APIView实现列表视图
class BookListView(APIView):

    def get(self, request):
        #1,查询所有的书籍
        books = BookInfo.objects.all()

        #2,将对象列表转成字典列表
        serializer = BookModelSerializer(instance=books, many=True)

        #3,返回响应
        return Response(serializer.data)

    def post(self, request):
        #1,获取参数
        data_dict = request.data

        #2,创建序列化器
        serializer = BookModelSerializer(data=data_dict)

        #3,校验，数据入库
        serializer.is_valid(raise_exception=True)
        serializer.save()

        #4,返回响应
        return Response(serializer.data, status=status.HTTP_201_CREATED)


#2, 序列化器和APIView实现详情视图
class BookDetailView(APIView):
    # 这里的传参 book_id 是用来接收动态 url 的
    def get(self, request, book_id):

        #1,获取书籍
        book = BookInfo.objects.get(id=book_id)

        #2,创建序列化器对象
        serializer = BookModelSerializer(instance=book)

        #3,返回响应
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, book_id):

        #1,获取数据,获取对象
        data_dict = request.data
        book = BookInfo.objects.get(id=book_id)

        # 2,创建序列化器对象
        serializer = BookModelSerializer(instance=book, data=data_dict)

        # 3,校验和入库
        serializer.is_valid(raise_exception=True)
        serializer.save()

        #4,返回响应
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self,request,book_id):

        #1,删除书籍
        BookInfo.objects.get(id=book_id).delete()

        #2,返回响应
        return Response(status.HTTP_204_NO_CONTENT)








