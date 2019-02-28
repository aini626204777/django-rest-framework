from django.shortcuts import render
from .models import ShuangSeQiu


# Create your views here.

def index(request):
    if request.method == "GET":
        return render(request, 'index.html')

    else:
        #获取到前端传的红球 01,02,03,04,05,06

        #1,2,3,4,5,6
        #01,02,03,04,05,06
        red = request.POST.get("red")
        #获取篮球 16
        blue = request.POST.get("blue")

        #s =  '1,2,3,4,5,6'
        red_list = red.split(",")
        #["1","2","3","4","5","6"]

        l = []#声明空列表
        for r in red_list:
            if int(r) < 10:
                l.append("0" + str(int(r)))
            else:
                l.append(r)

        #["01","02","03","04","05","06"]
        s = ",".join(l)

        #字符：s= 01,02,03,04,05,06

        try:
            seq = ShuangSeQiu.objects.get(red=s)
            if seq.blue == blue:
                ctx = {
                    "msg": "恭喜中一等奖",
                    "seq": seq
                }
                return render(request, 'index.html', ctx)
            else:
                ctx = {
                    "msg": "恭喜中二等奖",
                    "seq": seq
                }
                return render(request, 'index.html', ctx)
        except ShuangSeQiu.DoesNotExist:
            ctx = {
                "msg": "恭喜没中奖",
            }
            return render(request, 'index.html', ctx)
