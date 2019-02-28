from django.db import models


# Create your models here.
class ShuangSeQiu(models.Model):

    #红球属性 01,02,03,04,05,06
    red = models.CharField(max_length=20)
    #篮球输入 16
    blue = models.CharField(max_length=20)
    #开奖日期
    date = models.CharField(max_length=30)
