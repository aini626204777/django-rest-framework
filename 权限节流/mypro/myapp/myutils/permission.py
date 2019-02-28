# coding: utf-8
__author__ = "wengwenyu"

from rest_framework.permissions import BasePermission


class SVIPPermission(BasePermission):
    """
    权限
    """
    message = "无权访问"

    def has_permission(self, request, view):
        if request.user.user_type != 3:
            return False
        return True
