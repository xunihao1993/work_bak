# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path,include,re_path
from fileDown import views

urlpatterns = [
    path('', views.index)

]
