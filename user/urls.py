from django.urls import path

from user.views import TestView, JwtTestView, LoginView

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),  # 登录
    path('test', TestView.as_view(), name='test'),  # 测试
    path('jwt_test', JwtTestView.as_view(), name='jwt_test'),  # jwt测试

]
