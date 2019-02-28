
第一天：
	今日概要：
		1、restful 规范（建议）
		2、django rest framework框架

	内容回顾：
		1、开发模式
			- 普通开发方式-模板
			- 前后端分离
		2、后端开发
			- 为前端提供Api/接口
			- 永远返回HttpResponse json

		3、Django 
		FBV  function base view

		CBV  class base view
		
		4、列表生成式
		
		l = [x for x in range(10)]

		class Bar:
			pass


		class Foo:
			pass

		列表推导式
		l = [f() for f in [Bar,Foo]]
		
		普通的for循环
		for f in [Bar,Foo]
			Bar()	
			Foo()

		5、面向对象
			封装：
				- 把相同的功能方法封装类中 
				class FileHelp(object):
						'''关于文件'''

						def open(self,filename)
					
							pass

						def write(self,content)
							pass

				class DBHelp(object):
						'''关于数据库的'''

						def  openDB(self):
								pass

				- 把属性或对象封装到对象当中					
				class Dog(object):
					def __init__(self,name,age)
						self.name = name	
						self.age = age



				dog = Dog('二哈',10)		

				class Dog(object):
					def __init__(self,obj)
						self.obj = obj


				class Cat(object):
					pass

				cat = Cat()
				dog = Dog('二哈',10,cat)	




			继承
				- 子类继承父类
				- 实现代码复用

				新式类和经典类

				py3  继承写不写object都无所谓
				py2  写object 和不写object 差距可就大了


				class A()
					def show(self):
						pass

				class B(A)
					pass


				class C(A)
					pass


				class D(B,C)
					pass



				class F(D)
					pass


				f = F()
				f.show()


				广度查找 F-D---B---C--A
				深度查找 F--D---B--A-C

				py3 一般广大查找

			多态	：python动态语言。
					-  鸭子类型 只要会呱呱叫 就是鸭子

					class Msg():
						def send(self)
							pass

					class Email():
						def send(self):
							pass

					def shwo(obj):
						obj.send()



			------------

			class Request(object):
				def __init__(self,obj)
					self.obj = obj

				@property
				def user(self):
					self.obj.authticate()
						

			class Auth(objec):
				def __init__(self,name,age)
					self.name = name
					self.age = age

				def authticate(self):
					print(self.name)	


			class ApiView(object)

				def dispath(self)
					self.f2()

				def f2(self):
					#创建一个auth对象
					auth = Auth('laowang',18)
					#把auth对象封装到request对象当中
					request = Request(auth)

					# print(request.obj)
					request.user


			apiview = ApiView()
			apiview.dispath()							


		6、反射
			在运行中，可以通过getattr setattr给类设置属性或方法和获取属性和方法


 		7、错误码
 			2xx
 			3xx 
 			4xx
 			5xx
 		8、Http 基于Socket TCP 
 			面向连接的
 			三次握手
 			四次挥手	
	FBV


	CBV 
	View----->as_view()--->dispath(通过反射 找对对应的Get/POST/PUT/DELETE)



	如果是基于函数的 想取消掉CSRF
	from django.views.decorators.csrf import csrf_exempt
	@csrf_exempt

	如果基于类的视图 想取消掉CSRF
	@csrf_exempt
    def dispatch(self, request, *args, **kwargs):
    	pass


   @method_decorator(csrf_exempt, name='dispatch')
   class UserView(View): 
		pass	



	添加验证
	@csrf_protect 添加csrf验证

	@method_decorator(csrf_protect, name='dispatch')
	   class UserView(View): 
			pass	
	面试题
	csrf基于什么实现的
	csrf写在view里面

	基于中间件 

	中间件可以重写多少个方法？

	process_request

	process_view

	process_response

	process_exception

	process_templete_response



	django正常请求流程

	浏览器-->路由-->view--->model-->template---->response


	你基于中间件做过什么？

	 - 验证登录
	 - 黑名单



restFul的规范

	增删改查

	http://127.0.0.1:8000/add/
	http://127.0.0.1:8000/delete/
	http://127.0.0.1:8000/update/
	http://127.0.0.1:8000/get/

	用请求方法来代替增删改查


	http://127.0.0.1:8000/apple/

	GET PUT POST DELETE


	7.0


	6.0  

	老王的信息

	http://127.0.0.1:8000/user/1

	{
	'name':'laowang'
	'group':http://127.0.0.1:8000/group/1
	}

	访问这个组哪些人

	http://127.0.0.1:8000/group/1


	今晚的作业：
	1、面向对象
	2、CBV原理
	3、restful规范  
	4、中间件 csrf实现原理
	 













第二天：

	1、谈谈你对面向对象的理解
	2、Django生命的周期
	3、中间件最多写多少个方法
	4、csrf的原理
	5、CBV原理 
	6、restful规范




http://127.0.0.1:8000/apple/

获取一个苹果信息
http://127.0.0.1:8000/apple/1

	[{"id":'1',
	"name":'红富士'
	"detail":'http://127.0.0.1:8000/apple/1'},
	{"id":'2',
	"name":'国光'}]




{"code":1000,"msg":'支付成功'}
{"code":-1,"msg":'支付失败'}
{"code":-2,"msg":'支付取消'}




django_restframework 框架

	大概有10个组件
	1、安装
		pip install djangorestframework==3.9.0

		pip uninstall djangorestframework

	2、认证	

		- 有些接口只有登录了才能返回正确的信息
		- 先登录一下
			- 返回一个加密的字符串
			 	- 返回个人详情页 只要带上加密字符串我是不是就可以认为你是登录的用户



	3、
	    '''
	    1、User表
	        account
	        password
	        
	    把账号和密码通过get方式发送过来，然后进行账号和密码认证
	    
	    2、中间件不懂的是不是要看看笔记 去网上查查资料了
	    '''

	作业：
		- 把认证的逻辑给理清
		- 以前的面试题
		- 这个认证的代码要自己能独立敲下来    


第三天：
	一般我们认证只有一个

	1、认证的原理
	2、全局认证和局部认证
	3、内部认证类(了解)



	红球+篮球   红球33个 篮球16个

	开奖 6+1


	查询你现在选择的双色球 是否以前中国奖


	寒假作业：
		1、把笑话网站写出来（模板）数据通过爬虫爬取
		2、把所有双色球数据爬下来(http://kaijiang.500.com/ssq.shtml)，存到mysql
		写一个页面 然后写一个红球输入框和篮球输入库。随便输入6个红球 一个篮球 检查输入的双色球中奖没
		(防的http://china-ssq.com/#filterResult)
		3、年前3天的东西别忘记了
		4、预习一下权限和节流

		#取所有期数
		//span[@class='iSelectBox']/div/a



这个月课程：前端后分离  api

后端：django_restframework框架

1、认证

如果有接口需要登录访问，我就让他访问的时候带一个
token进来。然后咱们验证token是否存在。

常用的请求方式：
get  获取数据
post 提交数据
delete 删除数据
put   更新数据

restFul的规范：10条
对数据的操作：增删改查

苹果：
增  add/
删  delete/
改  change/
查  find/

apple/ 根据请求方式来对应不同的操作

前端：用cookie存东西


前端：jq操作Dom  
前后端分离：Vue框架



vue :组件化 - 单页面

vue:看下文档

mvc  
mvt django  
mv    vm 







