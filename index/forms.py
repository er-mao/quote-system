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
        error_messages={'required': u'请输入用户名'},
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': u'用户名',
            }
        )
    )

    password = forms.CharField(
        required=True,
        label=u'密码',
        error_messages={'required': u'请输入密码'},
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': u'密码',
            }
        )
    )
