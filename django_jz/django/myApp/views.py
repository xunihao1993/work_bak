from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.cache import cache
from myApp.task import longIO
# Create your views here.
import time
from celery.result import AsyncResult
# from myApp.models import
# from myApp.serializers import TestSerializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.utils.six import BytesIO
from io import BytesIO as BytesIO2


def index(request):
    # 缓存的应用
    # for i in range(100):
    #     cache.set('a'+str(i),'������'+str(i),60*60)
    # cache.set("aa",{"c":{'e':"c"},'d':'2'},60*60)
    # a = cache.get('aa').get('c')
    print('qweq')
    # return HttpResponseRedirect('/rsfTest1')
    return HttpResponse('哈哈哈')


def celery_test(request):
    # 缓存的应用
    a = longIO.delay(['1', '2', '3', '4'], ["haha", "cc"])
    # print('同步请求结束')
    # for i in a:
    #     print(i)
    print(a.id)
    # print(AsyncResult(a.id).get())
    # print(a.get(timeout=1))
    print('任务完成状态', a.ready())
    print('休眠10秒')
    time.sleep(10)
    print('任务完成状态', a.ready())
    print(a.state)
    print(a.status)
    print(a.successful)
    print(a.backend)
    print(AsyncResult(a.id).get())

    return HttpResponse(a)


def rsfTest1(request):
    # test1 = Test1.objects.get(pk=1)
    # print(test1.test2)
    # serializer = TestSerializers()
    # print(serializer)
    # serializer = TestSerializers(test1)
    # print(serializer.data)
    # content = JSONRenderer().render(serializer.data)
    # stream = BytesIO(content)
    # stream1 = BytesIO2(content)
    # print('字节流',content)
    # print('XXXXXXX222',stream)
    # print('XXXXXXX333', stream1)
    # stu = JSONParser().parse(stream1)
    # print('反序列化：',stu)
    # stu['test2']='测试1111'
    # print(stu)
    # serializer= TestSerializers(test1,data=stu)
    # print(serializer.is_valid()) #调save时必须判断
    # print(serializer.validated_data)
    # serializer.save()
    # serializer= TestSerializers(data=stu)
    # print(serializer.is_valid())
    # serializer.save()
    # # print(serializer.save())
    # # print(content.decode('gbk').encode('utf-8'))
    # # test2 = Test1.objects.all()
    # test2 = Student.objects.get(pk=5)
    # test2.delete()
    # print(test2)
    return HttpResponse('删除成功')
    # serializer=TestSerializers(test2,many=True) #用查询集
    # serializer=TestSerializers(test2)
    # return JsonResponse(serializer.data,safe=False) #返回多个需设置safe
    # return JsonResponse(serializer.data) #返回多个需设置safe
