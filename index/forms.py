# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    """
    登录表单
    """
    username = forms.CharField(
        required=True,
        label=u'用户名',
        error_messages={'required': '请输入用户名'},
        widget=forms.TextInput(
            attrs={
                'placeholder': u'用户名',
            }
        )
    )

    password = forms.CharField(
        required=True,
        label=u'密码',
        error_messages={'required': '请输入密码'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder': u'密码',
            }
        )
    )
