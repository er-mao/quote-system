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
    return render(request, 'index.html')


def login(request):
    """
    登录界面
    """
    nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    if request.method == 'GET':
        loginform = LoginForm()
        return render(request, 'login.html', {'loginform': loginform})
    else:
        loginform = LoginForm(request.POST)
        if loginform.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                # return render(request, 'login.html')
                if user.is_superuser:
                    return HttpResponseRedirect('/orders')
                else:
                    return HttpResponseRedirect('/users')
            else:
                return render(request, 'login.html', {'loginform': loginform, 'nowtime': nowtime, 'password_is_wrong': True, })
        else:
            return render(request, 'login.html', {'loginform': loginform, 'nowtime': nowtime, })
