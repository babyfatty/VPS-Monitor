#coding=utf8

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    username=forms.CharField(label=u"用户名",max_length=12,error_messages={'required': '用户名不能为空'})
    password=forms.CharField(label=u"密码",max_length=16,widget=forms.PasswordInput(),error_messages={'required': '密码不能为空'})

    def clean_username(self):
        username = self.cleaned_data['username']
        users = User.objects.filter(username=username)
        if not users:
            raise forms.ValidationError("用户名不存在")
        return username

    def clean_password(self):
        password = self.cleaned_data['password']
        user = authenticate(username=self.cleaned_data.get('username'), password=password)
        if user is None:
            raise forms.ValidationError("用户名密码不匹配")
        return password
