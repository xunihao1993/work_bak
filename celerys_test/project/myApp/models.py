from django.db import models

# Create your models here.
from django.db import models
# 定义模型
class Student(models.Model):
    name = models.CharField(max_length=20)
    sex = models.BooleanField()
    contend = models.CharField(max_length=20)
    age = models.IntegerField()
    isDelete = models.BooleanField(default=False)
