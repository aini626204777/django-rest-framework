from django.db import models


# Create your models here.
class UserGroup(models.Model):
    title = models.CharField(max_length=32, verbose_name='用户组名')


class Role(models.Model):
    title = models.CharField(max_length=32, verbose_name="角色")


class UserInfo(models.Model):
    user_type_choices = (
        (1, "普通用户"),
        (2, "VIP"),
        (3, "SVIP")
    )
    user_type = models.IntegerField(choices=user_type_choices, verbose_name="用户类型")
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=256)
    group = models.ForeignKey(UserGroup, verbose_name="用户类型")
    roles = models.ManyToManyField(Role)


class UserToken(models.Model):
    user = models.OneToOneField(UserInfo)
    token = models.CharField(max_length=256)
