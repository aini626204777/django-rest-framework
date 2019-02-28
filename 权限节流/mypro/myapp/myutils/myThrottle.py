from rest_framework.throttling import BaseThrottle, SimpleRateThrottle
import time

HISTORY_DICT = {}


class MyThrottle(BaseThrottle):
    """
    继承 from rest_framework.throttling import BaseThrottle
    节流、限制频率
    """
    def __init__(self):
        self.history = None

    def allow_request(self, request, view):
        """
        逻辑　1、 ip 2、判断
        :param request:
        :param view:
        :return:
        """
        ip_addr = request._request.META['REMOTE_ADDR']
        # 获取当前时间
        ctime = time.time()
        # 每分钟限制三次
        if ip_addr not in HISTORY_DICT:
            HISTORY_DICT[ip_addr] = [ctime, ]

            return True
        history = HISTORY_DICT[ip_addr]
        self.history = history
        while history and history[-1] < ctime - 60:
            history.pop()
        if len(history) < 3:
            ctime = time.time()
            history.insert(0, ctime)
            return True

        # 如果访问返回True表示可以继续往下走，Fales被限制访问
        return False

    def wait(self):
        """
        Optionally, return a recommended number of seconds to wait before
        the next request.
        """
        ctime = time.time()

        return 60 - (ctime - self.history[-1])


class MyThrottle2(SimpleRateThrottle):
    scope = "scope"

    # 缓存配置
    def get_cache_key(self, request, view):
        return self.get_ident(request)

class UserThrottle(SimpleRateThrottle):
    scope = 'user_scope'
