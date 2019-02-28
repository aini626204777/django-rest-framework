from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from myapp.myutils.auth import MyAuthtication
from myapp.myutils.permission import SVIPPermission
from myapp.myutils.myThrottle import MyThrottle,MyThrottle2,UserThrottle
from myapp import models
from rest_framework.throttling import SimpleRateThrottle

ORDER_DICT = {
    1: {
        "name": "张三",
        "age": 18,
        "gender": "男",
        "orders": [{
            "name": "娃娃",
            "price": 1000
        }]
    },
    2: {
        "name": "李四",
        "age": 20,
        "gender": "女",
        "orders": [{
            "name": "你猜",
            "price": 1200
        }]
    },

}


def md5(user):
    """生成随机字符串"""
    import hashlib
    import time

    ctime = str(time.time())
    m = hashlib.md5(bytes(user, encoding="utf-8"))
    m.update(bytes(ctime, encoding="utf-8"))
    return m.hexdigest()




class AuthView(APIView):
    """登陆页面"""
    authentication_classes = []
    permission_classes = []
    throttle_classes = [MyThrottle2]
    def post(self, request, *args, **kwargs):
        ret = {"state_code": 1000, "msg": None}
        try:
            username = request._request.POST.get("username")
            password = request._request.POST.get("password")
            obj = models.UserInfo.objects.filter(username=username, password=password).first()
            if not obj:
                ret["state_code"] = 1001
                ret["msg"] = "用户名或者密码错误"
            # 为登陆用户创建一个token
            token = md5(username)
            # 存到数据库 存在就更新,不存在就创建
            models.UserToken.objects.update_or_create(user=obj, defaults={"token": token})
            ret["token"] = token
            ret["msg"] = "请求成功"
        except Exception as e:
            ret["state_code"] = 1002
            ret["msg"] = "请求异常"
        return JsonResponse(ret)


class OrderView(APIView):
    """
    订单相关业务
    """
    authentication_classes = [MyAuthtication, ]
    permission_classes = [SVIPPermission, ]
    throttle_classes = [UserThrottle]

    def get(self, request, *args, **kwargs):

        # token = request._request.GET.get("token")
        # if not token:
        #     return HttpResponse("用户未登录!")

        ret = {"state_code": 1000, "msg": None, "data": None}
        # if request.user.user_type != 3:
        #     ret = {"state_code": 1001, "msg": "无权限", "data": []}
        # else:
        try:
            ret['data'] = ORDER_DICT
        except Exception as e:
            pass
        return JsonResponse(ret)


class UserInfoView(APIView):

    def get(self, request, *args, **kwargs):
        print(request.user)
        return JsonResponse({"user": request.user})



