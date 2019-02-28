from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'login/$',views.AuthView.as_view()),
    url(r'teacher/$',views.TeacherView.as_view()),
    url(r'student/$',views.StudentView.as_view()),


]