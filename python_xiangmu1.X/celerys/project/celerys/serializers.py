# -*- coding: utf-8 -*-

from rest_framework import serializers
from celerys.models import Test1

class TestSerializers(serializers.ModelSerializer):
    class Meta:
        model = Test1
        # 输出所有对象
        fields ='__all__'
        # fields = ("id", "test1", "test2", "test3")
