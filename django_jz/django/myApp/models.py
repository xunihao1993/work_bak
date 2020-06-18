from django.db import models

# Create your models here.
from django.db import models


# 定义模型
class Base(models.Model):
    """
    基础表，后续的app中models的定义都继承此表
    """
    creator = models.CharField(verbose_name="创建人用户名", max_length=50, blank=False, null=False, )
    last_mender = models.CharField(verbose_name="最后修改人用户名", max_length=50, blank=False, null=False)
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    last_modified_time = models.DateTimeField(verbose_name="最后修改时间", auto_now=True)

    class Meta:
        abstract = True


# 定义模型


# class Student(Base):
# 	name = models.CharField(max_length=20)
# 	sex = models.BooleanField()
# 	contend = models.CharField(max_length=20)
# 	age = models.IntegerField()
# 	isDelete = models.BooleanField(default=False)


class LogDownInfo(Base):
    deviceIp = models.CharField(max_length=200, verbose_name='设备ip段')
    logSavePath = models.CharField(max_length=200, verbose_name='服务器日志保存路径')

    class Meta:
        db_table = 'LogDownInfo'
        verbose_name = '定时下载日志信息表'
        verbose_name_plural = verbose_name


class DeviceInfo(Base):
    deviceIp = models.CharField(max_length=20, verbose_name='设备ip', primary_key=True)
    deviceCatena = models.CharField(max_length=20, verbose_name='产品系列号', default='C')
    sdkName = models.CharField(max_length=20, verbose_name='sdk用户名')
    sdkPass = models.CharField(max_length=20, verbose_name='sdk密码')
    sdkPost = models.CharField(max_length=20, verbose_name='sdk端口号')
    sshName = models.CharField(max_length=20, verbose_name='ssh用户名', null=True, blank=True)
    sshPass = models.CharField(max_length=20, verbose_name='ssh密码', null=True, blank=True)
    sshPost = models.CharField(max_length=20, verbose_name='ssh端口号', null=True, blank=True)
    sftpName = models.CharField(max_length=20, verbose_name='SFTP用户名', null=True, blank=True)
    sftpPass = models.CharField(max_length=20, verbose_name='SFTP密码', null=True, blank=True)
    sftpPost = models.CharField(max_length=20, verbose_name='SFTP端口号', null=True, blank=True)
    sftpPath = models.CharField(max_length=200, verbose_name='sftp绝对路径', null=True, blank=True)
    deviceLogPath = models.CharField(max_length=200, verbose_name='设备日志路径', null=True, blank=True)
    deviceBakLogPath = models.CharField(max_length=200, verbose_name='设备备份日志路径', null=True, blank=True)

    class Meta:
        db_table = 'DeviceInfo'
        verbose_name = '设备信息维护表'
        verbose_name_plural = verbose_name


class BasisInfo(Base):
    projectName = models.CharField(max_length=20, verbose_name='母业务', default='sdc_dingzhi')
    appName = models.CharField(max_length=20, verbose_name='子业务', default='commissionApp')
    key = models.CharField(max_length=20, verbose_name='配置名')
    value = models.CharField(max_length=200, verbose_name='配置值')

    class Meta:
        db_table = 'BasisInfo'
        verbose_name = '基础配置信息表'
        verbose_name_plural = verbose_name
