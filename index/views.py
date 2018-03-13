# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context import RequestContext

from .forms import LoginForm
# Create your views here

import time


def index(request):
    """
    主页
    """
    nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    if request.method == 'GET':
        login_form = LoginForm()
        return render(request, 'index/index.html',
                      {'login_form': login_form})
    else:
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                if user.is_superuser:
                    return HttpResponseRedirect('/orders')
                else:
                    return HttpResponseRedirect('/users')
            else:
                return render(request, 'index/index.html',
                              {'login_form': login_form,
                               'nowtime': nowtime,
                               'login_error': True, })
        else:
            return render(request, 'index/index.html',
                          {'login_form': login_form,
                           'nowtime': nowtime, })


def login(request):
    """
    登录界面
    """
    # nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    # if request.method == 'GET':
    #     login_form = LoginForm()
    #     return render(request, 'index/login.html',
    #                   {'login_form': login_form})
    # else:
    #     login_form = LoginForm(request.POST)
    #     if login_form.is_valid():
    #         username = request.POST.get('username', '')
    #         password = request.POST.get('password', '')
    #         user = auth.authenticate(username=username, password=password)
    #         if user is not None and user.is_active:
    #             auth.login(request, user)
    #             if user.is_superuser:
    #                 return HttpResponseRedirect('/orders')
    #             else:
    #                 return HttpResponseRedirect('/users')
    #         else:
    #             return render(request, 'index/login.html',
    #                           {'login_form': login_form,
    #                            'nowtime': nowtime,
    #                            'password_is_wrong': True, })
    #     else:
    #         return render(request, 'index/login.html',
    #                       {'login_form': login_form,
    #                        'nowtime': nowtime, })
    return HttpResponseRedirect('/')
