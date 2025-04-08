from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from rest_framework_jwt.settings import api_settings

from menu.models import SysMenu, SysMenuSerializer
from role.models import SysRole
from user.models import SysUser, SysUserSerializer


class LoginView(View):

    def buildTreeMenu(self, sysMenuList):
        resultMenuList: list[SysMenu] = list()
        for menu in sysMenuList:
            # 寻找子节点
            for e in sysMenuList:
                if e.parent_id == menu.id:
                    if not hasattr(menu, "children"):
                        menu.children = list()
                    menu.children.append(e)
            # 判断父节点，添加到集合
            if menu.parent_id == 0:
                resultMenuList.append(menu)
        return resultMenuList

    def post(self, request):
        username = request.GET.get("username")
        password = request.GET.get("password")
        try:
            user = SysUser.objects.get(username=username, password=password)
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
            # 将用户对象传递进去，获取到该对象的属性值
            payload = jwt_payload_handler(user)
            # 将属性值编码成jwt格式的字符串
            token = jwt_encode_handler(payload)

            roleList = SysRole.objects.raw(
                "SELECT id ,NAME FROM sys_role WHERE id IN (SELECT role_id FROM sys_user_role WHERE user_id=" + str(
                    user.id) + ")")
            print(roleList)
            menuSet: set[SysMenu] = set()
            for row in roleList:
                print(row.id, row.name)
                menuList = SysMenu.objects.raw(
                    "SELECT * FROM sys_menu WHERE id IN (SELECT menu_id FROM sys_role_menu WHERE role_id=" + str(
                        row.id) + ")")
                for row2 in menuList:
                    print(row2.id, row2.name)
                    menuSet.add(row2)
            print(menuSet)
            menuList: list[SysMenu] = list(menuSet)  # set转list
            sorted_menuList = sorted(menuList)  # 根据order_num排序
            print(sorted_menuList)
            # 构造菜单树
            sysMenuList: list[SysMenu] = self.buildTreeMenu(sorted_menuList)
            print(sysMenuList)
            serializerMenuList = list()
            for sysMenu in sysMenuList:
                serializerMenuList.append(SysMenuSerializer(sysMenu).data)

        except Exception as e:
            print(e)
            return JsonResponse({'code': 500, 'info': '用户名或者密码错误！'})
        return JsonResponse({'code': 200, 'token': token, 'user': SysUserSerializer(user).data, 'info': '登录成功',
                             'menuList': serializerMenuList})


# Create your views here.
class TestView(View):

    def get(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')
        if token != None and token != '':
            userList_obj = SysUser.objects.all()
            print(userList_obj, type(userList_obj))
            userList_dict = userList_obj.values()  # 转存字典
            print(userList_dict, type(userList_dict))
            userList = list(userList_dict)  # 把外层的容器转存List
            print(userList, type(userList))
            return JsonResponse({'code': 200, 'info': '测试！', 'data': userList})
        else:
            return JsonResponse({'code': 401, 'info': '没有访问权限！'})


class JwtTestView(View):

    def get(self, request):
        user = SysUser.objects.get(username='python222', password='123456')
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        # 将用户对象传递进去，获取到该对象的属性值
        payload = jwt_payload_handler(user)
        # 将属性值编码成jwt格式的字符串
        token = jwt_encode_handler(payload)
        return JsonResponse({'code': 200, 'token': token})
