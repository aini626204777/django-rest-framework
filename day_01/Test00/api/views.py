from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from django.views import View
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
class BaseView(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        print('1111')

        ret = super().dispatch(request, *args, **kwargs)
        print('2222')

        return ret


class TeacherView(BaseView, View):
    def get(self, *args, **kwargs):
        ctx = {'name': 'guobi'}
        return HttpResponse(json.dumps(ctx), content_type='application/json')

    def post(self, *args, **kwargs):
        ctx = {'name': 'POST'}
        return HttpResponse(json.dumps(ctx), content_type='application/json')

    def delete(self, *args, **kwargs):
        ctx = {'name': 'delete'}
        return HttpResponse(json.dumps(ctx), content_type='application/json')


from rest_framework.authentication import BaseAuthentication
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed


class MyAuthtication(object):
    def authenticate(self, request):
        token = request._request.GET.get('token')
        if not token:
            raise AuthenticationFailed('认证失败')
        else:
            return ('老王', None)

    def authenticate_header(self, request):
        pass


class Order(APIView):
    authentication_classes = [MyAuthtication]

    def get(self, request, *args, **kwargs):
        self.dispatch
        return HttpResponse('获取')

    def post(self, request, *args, **kwargs):
        self.dispatch
        return HttpResponse('添加')

    def put(self, request, *args, **kwargs):
        return HttpResponse('修改')

    def delete(self, request, *args, **kwargs):
        return HttpResponse('删除')
