# coding: utf-8
__author__ = "wengwenyu"
from myapp import models
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions


class MyAuthtication(BaseAuthentication):
    """
    认证
    """
    def authenticate(self, request):
        token = request._request.GET.get("token")
        token_obj = models.UserToken.objects.filter(token=token).first()
        # 认证失败
        if not token_obj:
            raise exceptions.AuthenticationFailed("用户认证失败")
        # 在 rest framework内部 会将这两个字段赋值给request,以供后续操作使用
        return (token_obj.user, token)




class MyAuthtication_None(BaseAuthentication):
    def authenticate(self, request):
        pass
