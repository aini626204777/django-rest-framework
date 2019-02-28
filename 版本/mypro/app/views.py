from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView
from rest_framework.request import Request
from app import models
from rest_framework.versioning import QueryParameterVersioning, BaseVersioning, URLPathVersioning
import json


#   ---------------------------------版本相关内容------------------------------------------------------
class ParamVersions(object):
    def determine_version(self, request, *args, **kwargs):
        version = request._request.GET.get("version")
        # version = request.query_params.get('version')
        # version = request.GET.get("version")
        return version


class UsersView(APIView):
    """
    版本
    """
    versioning_class = URLPathVersioning

    def get(self, request, *args, **kwargs):
        # version = request.GET.get("version")
        version = request.version
        # 反向生成url
        u1 = request.versioning_scheme.reverse(viewname='user', request=request)
        # 基于Django
        # u1 = request.versioning_scheme.reverse(viewname="user",kwargs={'version':request.version})
        print(u1)
        return JsonResponse({'version': version})


#   ---------------------------------解释器相关内容------------------------------------------------------

class DjangoView(APIView):
    """
    解释器,现在用的是DRF框架的解释器
    """

    def post(self, request, *args, **kwargs):
        ret = request.data['name']
        print(ret)
        return JsonResponse({'ret': ret})


#   ---------------------------------序列化相关内容------------------------------------------------------

class RolesView(APIView):
    """
    序列化
    """

    # def get(self, request, *args, **kwargs):
    #     roles = models.Role.objects.all().values('id','title')
    #     return HttpResponse(roles)
    def get(self, request, *args, **kwargs):
        roles = models.Role.objects.all()
        ser = RolesSerializer(roles, many=True)

        return HttpResponse(json.dumps(ser.data))


from rest_framework import serializers


class RolesSerializer(serializers.Serializer):
    id = serializers.CharField()
    title = serializers.CharField()


class UserInfoSerializer(serializers.Serializer):
    """
    序列化组件
    """
    user_type = serializers.IntegerField()
    vip = serializers.CharField(source="get_user_type_display")
    username = serializers.CharField()
    password = serializers.CharField()

    group = serializers.CharField(source='group.title')

    rls = serializers.SerializerMethodField()  # 自定义显示内容

    def get_rls(self, user):  # 当前这一行的模型对象
        rls_list = user.roles.all()
        ret = []
        for item in rls_list:
            ret.append({
                "id": item.id,
                "title": item.title
            })
        return ret


class UserInfoSerializer2(serializers.ModelSerializer):
    """
    序列化组件
    """
    vip = serializers.CharField(source="get_user_type_display")
    group = serializers.CharField(source='group.title')

    class Meta:
        model = models.UserInfo
        fields = '__all__'

    rls = serializers.SerializerMethodField()  # 自定义显示内容

    def get_rls(self, user):  # 当前这一行的模型对象
        rls_list = user.roles.all()
        ret = []
        for item in rls_list:
            ret.append({
                "id": item.id,
                "title": item.title
            })
        return ret


class UserInfoSerializer3(serializers.ModelSerializer):
    class Meta:
        model = models.UserInfo
        fields = "__all__"
        depth = 1


class UserInfoView(APIView):
    """
    视图类
    接受请求，返回响应
    """

    def get(self, request, *args, **kwargs):
        """
        先从数据库去数据
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        users = models.UserInfo.objects.all()
        ser = UserInfoSerializer3(users, many=True)
        return HttpResponse(json.dumps(ser.data))


class UserGroupSerializer(serializers.Serializer):
    title = serializers.CharField(error_messages={"required": "标题不能为空"})


class UserGroupView(APIView):
    def post(self, request, *args, **kwargs):
        print(request.data)
        # 我现在不是用数据库里面的数据,是用户提交的数据
        ser = UserGroupSerializer(data=request.data)
        if ser.is_valid():
            print(ser.validated_data)
        else:
            print(ser.errors)

        return HttpResponse('提交数据')


#   ---------------------------------分页相关内容------------------------------------------------------

from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.pagination import CursorPagination


class PagerSerializer(serializers.ModelSerializer):
    """序列化组件"""

    class Meta:
        model = models.Role
        fields = "__all__"


# 自定义分页类
class MyPageNumberPagination(PageNumberPagination):
    # 每页显示多少个
    page_size = 4
    # 默认每页显示3个,可以通过传入pager1/?page=2&size=4,改变默认每页显示的个数
    page_size_query_param = "size"
    # 最大页数不超过10
    max_page_size = 10
    # 获取页码数的
    page_query_param = "page"


class PagerView1(APIView):
    def get(self, request, *args, **kwargs):
        # 从数据库里面取数据
        roles = models.Role.objects.all()
        # # 序列化
        # ser = PagerSerializer(instance=roles, many=True)
        # 我现在要先分页　将分页完了以后的数据进行序列化
        # 实例化一个分页对象
        pg = MyPageNumberPagination()
        roles_list = pg.paginate_queryset(queryset=roles, request=request, view=self)
        # 对数据进行序列化
        ser = PagerSerializer(instance=roles_list, many=True)
        return Response(ser.data)


# 自定义分页类2
class MyLimitOffsetPagination(LimitOffsetPagination):
    # 默认显示的个数
    default_limit = 5
    # 当前的位置
    offset_query_param = "offset"
    # 通过limit改变默认显示的个数
    limit_query_param = "limit"
    # 一页最多显示的个数
    max_limit = 10


class PagerView2(APIView):
    def get(self, request, *args, **kwargs):
        # 从数据库里面取数据
        roles = models.Role.objects.all()
        # # 序列化
        # ser = PagerSerializer(instance=roles, many=True)
        # 我现在要先分页　将分页完了以后的数据进行序列化
        # 实例化一个分页对象
        pg = MyLimitOffsetPagination()
        roles_list = pg.paginate_queryset(queryset=roles, request=request, view=self)
        # 对数据进行序列化
        ser = PagerSerializer(instance=roles_list, many=True)
        return Response(ser.data)


# 自定义分页类3 (加密分页)
class MyCursorPagination(CursorPagination):
    cursor_query_param = "cursor"
    page_size = 6
    # 每页显示2个数据
    ordering = 'id'
    # 排序
    page_size_query_param = None
    max_page_size = None


class PagerView3(APIView):
    def get(self, request, *args, **kwargs):
        # 从数据库里面取数据
        roles = models.Role.objects.all()
        # # 序列化
        # ser = PagerSerializer(instance=roles, many=True)
        # 我现在要先分页　将分页完了以后的数据进行序列化
        # 实例化一个分页对象
        pg = MyCursorPagination()
        roles_list = pg.paginate_queryset(queryset=roles, request=request, view=self)
        # 对数据进行序列化
        ser = PagerSerializer(instance=roles_list, many=True)
        return pg.get_paginated_response(ser.data)


#   ---------------------------------视图相关内容------------------------------------------------------

from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import ListModelMixin, DestroyModelMixin,CreateModelMixin


class MyView1(GenericAPIView):
    queryset = models.Role.objects.all()
    serializer_class = PagerSerializer
    pagination_class = MyPageNumberPagination

    def get(self, request, *args, **kwargs):
        # 取数据
        roles = self.get_queryset()
        # 分页
        roles_list = self.paginate_queryset(queryset=roles)
        # 序列化
        ser = self.get_serializer(instance=roles_list, many=True)
        return Response(ser.data)


class MyView2(GenericViewSet):
    queryset = models.Role.objects.all()
    serializer_class = PagerSerializer
    pagination_class = MyPageNumberPagination

    def list(self, request, *args, **kwargs):
        # 取数据
        roles = self.get_queryset()
        # 分页
        roles_list = self.paginate_queryset(queryset=roles)
        # 序列化
        ser = self.get_serializer(instance=roles_list, many=True)
        return Response(ser.data)

class MyView3(ListModelMixin,GenericViewSet):
    queryset = models.Role.objects.all()
    serializer_class = PagerSerializer
    pagination_class = MyPageNumberPagination




class MyView4(ModelViewSet):
    queryset = models.Role.objects.all()
    serializer_class = PagerSerializer
    pagination_class = MyPageNumberPagination
