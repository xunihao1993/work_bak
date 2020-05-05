# -*- coding: utf-8 -*-
import time
from celery import shared_task
from django.db import transaction

@shared_task
def test1():
    print("这是队列任务1")
    # 1/0
    return '这是队列1'

@shared_task
def test2(a):
    print("这是队列任务2:",a)
    return '这是队列2'

@shared_task
def longIO(list=0,list2=0):
    print("定时任务开始开始耗时操作")
    test1.delay()
    test2.delay("变量2")
    time.sleep(20)
    print("定时任务结束耗时操作")
    list3=list+list2
    print(list3)
    return list3