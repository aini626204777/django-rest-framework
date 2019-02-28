from django.db import models


# Create your models here.
class UserInfo(models.Model):
    """
    用户表
    """
    types = (
        (1, '普通用户'),
        (2, 'vip'),
        (3, 'svip'),
    )
    user_type = models.IntegerField(choices=types)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)


class UserToken(models.Model):
    """
    token
    """
    user = models.OneToOneField(to=UserInfo)
    token = models.CharField(max_length=64)
