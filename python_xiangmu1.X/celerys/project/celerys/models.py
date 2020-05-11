from django.db import models

# Create your models here.
class Test1(models.Model):
    test1 = models.CharField(max_length=200)
    test2 = models.CharField(max_length=200)
    test3 = models.CharField(max_length=200,default='')