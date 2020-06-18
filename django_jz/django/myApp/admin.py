from django.contrib import admin
from myApp.models import BasisInfo, LogDownInfo, DeviceInfo
# Register your models here.
import time


# 定时下载log信息表注册类
class LogDwonInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'deviceIp', 'logSavePath',)


# 设备信息维护表
class DeviceInfoAadmin(admin.ModelAdmin):
    list_display = ('deviceIp', 'deviceCatena', 'sdkName', 'sdkPass', 'sdkPost',)


# 基础配置信息表
class BasisInfoAdmin(admin.ModelAdmin):
    list_display = ('projectName', 'appName', 'key', 'value',)


# models
admin.site.register(LogDownInfo, LogDwonInfoAdmin)
admin.site.register(DeviceInfo, DeviceInfoAadmin)
admin.site.site_title = "测试定制组后台管理"
admin.site.site_header = "测试定制组"
