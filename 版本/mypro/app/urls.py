from django.conf.urls import url,include
from .views import UsersView, DjangoView, RolesView, UserInfoView, UserGroupView, PagerView1, PagerView2, PagerView3, \
    MyView1, MyView2, MyView3, MyView4
from app import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'myview', MyView4)
urlpatterns = [
    # url(r'^users/$', UsersView.as_view()),
    # url(r'^(?P<version>[v1|v2]+)/users/$', UsersView.as_view(), name='user'),
    # url(r'^(?P<version>[v1|v2]+)/django/$', DjangoView.as_view(), name='django'),
    # url(r'^(?P<version>[v1|v2]+)/roles/$', RolesView.as_view()),
    # url(r'^(?P<version>[v1|v2]+)/userinfo/$', UserInfoView.as_view()),
    # url(r'^(?P<version>[v1|v2]+)/usergroup/$', UserGroupView.as_view(), name='ugp'),
    # url(r'^(?P<version>[v1|v2]+)/page1/', PagerView1.as_view()),
    # url(r'^(?P<version>[v1|v2]+)/page2/', PagerView2.as_view()),
    # url(r'^(?P<version>[v1|v2]+)/page3/', PagerView3.as_view()),
    # url(r'^(?P<version>[v1|v2]+)/myview1/', MyView1.as_view()),
    # url(r'^(?P<version>[v1|v2]+)/myview2/', MyView2.as_view({'get': 'list'})),
    # url(r'^(?P<version>[v1|v2]+)/myview3/', MyView3.as_view({'get': 'list'})),
    # url(r'^(?P<version>[v1|v2]+)/myview4/', MyView4.as_view({'get': 'list','delete':'destroy','post':'create'})),
    # url(r'^(?P<version>[v1|v2]+)/myview4/(?P<pk>\d+)/',
    #     MyView4.as_view({"get": "retrieve", "delete": "destroy", "put": "update",
    #                      "patch": "partial_update"}))
    url(r'^(?P<version>[v1|v2]+)/', include(router.urls)),
]
