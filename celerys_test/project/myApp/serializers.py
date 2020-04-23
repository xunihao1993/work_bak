# -*- coding: utf-8 -*-

from rest_framework import serializers
from myApp.models import Student
class TestSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        # 输出所有对象
        fields ='__all__'
        # fields = ("id", "test1", "test2", "test3")
