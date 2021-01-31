from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse


# Create your views here.

def index(request):
    return render(request, 'index.html')


def test(request):

    return HttpResponse('test')


def menus(request):
    if request.method == 'GET':
        data = {
            "data": [
                {
                    "id": 100,
                    "authName": "用户管理",
                    "path": "users",
                    "order": 1,
                    "icon": "el-icon-user-solid",
                    "children": [
                        {
                            "id": 101,
                            "authName": "用户列表",
                            "path": "users",
                            "children": []
                        }
                    ]
                },
                {
                    "id": 110,
                    "authName": "权限管理",
                    "path": "rights",
                    "order": 2,
                    "icon": "el-icon-s-check",
                    "children": [
                        {
                            "id": 111,
                            "authName": "角色列表",
                            "path": "roles",
                            "children": []
                        },
                        {
                            "id": 112,
                            "authName": "权限列表",
                            "path": "rights",
                            "children": []
                        }
                    ]
                },
                {
                    "id": 120,
                    "authName": "商品管理",
                    "path": "goods",
                    "order": 3,
                    "icon": "el-icon-s-shop",
                    "children": [
                        {
                            "id": 121,
                            "authName": "商品列表",
                            "path": "goods1",
                            "children": []
                        },
                        {
                            "id": 122,
                            "authName": "商品参数",
                            "path": "goods2",
                            "children": []
                        },
                        {
                            "id": 123,
                            "authName": "商品分类",
                            "path": "goods3",
                            "children": []
                        }
                    ]
                },
                {
                    "id": 130,
                    "authName": "数据统计",
                    "path": "report",
                    "order": 4,
                    "icon": "el-icon-s-data",
                    "children": [
                        {
                            "id": 131,
                            "authName": "数据列表",
                            "path": "report",
                            "children": []
                        }
                    ]
                }
            ],
            "mata": {
                "msg": "获取菜单列表成功",
                "status": 200
            }
        }
        print(data)
        return JsonResponse(data)
    else:
        return ''


def login(request):
    # return HttpResponse('index')  # 返回一个字符串
    if request.method == 'POST':
        user = request.POST.get('username')
        pwd = request.POST.get('password')
        print(user, pwd)
        # orm 数据库相关
        from app01 import models
        ret = models.User.objects.filter(username=user, password=pwd)
        if ret:
            print('登录成功')
            return JsonResponse(
                {
                    'code': 200,
                    'result': 'success',
                    'message': '登录成功',
                    'token': 'token_123'
                }
            )
        else:
            print('登录失败')
            return JsonResponse(
                {
                    'code': 200,
                    'result': 'fail',
                    'message': '登录失败',
                    'data': {'token': 'null'}
                }
            )

    else:
        return render(request, 'login.html')  # 返回一个页面
