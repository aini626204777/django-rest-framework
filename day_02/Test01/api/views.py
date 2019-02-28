from django.shortcuts import render
from rest_framework.views import APIView
from .models import UserInfo, UserToken
from django.http import JsonResponse
import hashlib
from rest_framework.exceptions import AuthenticationFailed
import time


# Create your views here.
def createToken(username):
    '''
    laowang   ------ 64

    :param username:
    :return:
    '''
    md5 = hashlib.md5()

    md5.update(bytes(username + str(time.time()), encoding='utf-8'))

    token = md5.hexdigest()

    return token


class AuthView(APIView):

    def post(self, reuqest, *args, **kwargs):

        ret = {"code": '1000', 'msg': None}
        try:
            username = reuqest._request.POST.get('username')
            password = reuqest._request.POST.get('password')

            user = UserInfo.objects.filter(username=username, password=password).first()

            if user:
                # 生成token
                token = createToken(username)
                # 存token

                # usertoken = UserToken()
                # usertoken.token = token
                # usertoken.user = user
                # usertoken.save()
                UserToken.objects.update_or_create(user=user, defaults={'token': token})
                ret['token'] = token
                return JsonResponse(ret)
            else:
                ret['code'] = -1
                ret['msg'] = '账号或密码错误'
                return JsonResponse(ret)
        except Exception:
            ret['code'] = -1
            ret['msg'] = '服务器泡妞去了'
            return JsonResponse(ret)


ORDER_LIST = {
    1: {
        "name": "猪肉",
        "price": 12,
    },
    2: {
        "name": "媳妇",
        "price": 18,
    }
}


class MyAuthtication(object):
    def authenticate(self, request):
        token = request._request.GET.get('token')
        if not token:
            raise AuthenticationFailed('验证失败')
        else:
            usertoken = UserToken.objects.filter(token=token).first()
            if usertoken:
                return (usertoken.user, token)
            else:
                raise AuthenticationFailed('验证失败')

    def authenticate_header(self, request):
        pass


class OrderView(APIView):
    authentication_classes = [MyAuthtication]

    def get(self, request, *args, **kwargs):
        ret = {"code": '1000', 'msg': None}
        try:
            ret['data'] = ORDER_LIST
            return JsonResponse(ret)
        except Exception:
            ret['code'] = -1
            ret['msg'] = '服务器泡妞去了'
            return JsonResponse(ret)


class UserInfoView(APIView):
    authentication_classes = [MyAuthtication]

    def get(self, reuqest, *args, **kwargs):
        return JsonResponse({"name": "laowang"})


'''
１、只有认证通过才能访问
'''
#　权限
class Svippermissions(object):
    def has_permission(self,request,views):
        if request.user.user_type == 3:
            return True
        else:
            return False
class TeacherView(APIView):
    authentication_classes = [MyAuthtication]
    permission_classes = [Svippermissions]
    def get(self,request,*args,**kwargs):
        if request.user.user_type == 3:
            return JsonResponse({'msg':'恭喜您访问进来了'})



# 节流
Throttle_history = {}
class MyThrottle(object):
    def allow_request(self,request,view):
        ip = request.META.get('REMOTE_ADDR')
        if ip not in Throttle_history:
            ctime = time.time()
            Throttle_history['ip'] = [ctime,]
            return True
        history = Throttle_history.get('ip')

        ctime = time.time()
        while history and history[-1] < ctime - 60:
            history.pop()
        if len(history) < 10:
            ctime = time.time()
            Throttle_history.get('ip').insert(0,ctime)
            return True
    def wait(self):
        pass
class StudentView(APIView):
    permission_classes = []
    def get(self,request,*args,**kwargs):
        ip = request.META.get('REMOTE_ADDR')
        return JsonResponse({'ip':ip})

