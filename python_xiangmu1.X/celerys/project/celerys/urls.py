# -*- coding: utf-8 -*-
from django.conf.urls import url
from celerys import views
from djcelery.views import is_task_successful

urlpatterns = [
    url(r'^index/$',views.index),
    url(r'^celerytest/$',views.celery_test),
    url(r'^rsfTest1/$', views.rsfTest1),

]
