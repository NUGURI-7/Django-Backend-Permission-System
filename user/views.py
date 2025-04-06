from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from user.models import SysUser

# Create your views here.
class TestView(View):

    def get(self, request):
        userList_obj = SysUser.objects.all()
        userList_dict = userList_obj.values() #转为字典
        userList = list(userList_dict)  #字典转为list
        return JsonResponse({'code':200, 'info':'测试！','data':userList})