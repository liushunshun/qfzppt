#coding=utf-8
from django.shortcuts import render_to_response
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from zp.models import User

class UserForm(forms.Form):
	#邮箱
    email = forms.CharField()
	#用户名
    username = forms.CharField()
	#密码
    password = forms.CharField(widget = forms.PasswordInput)
	#确认密码
    passwordConfirm = forms.CharField(widget = forms.PasswordInput)
class loginForm(forms.Form):
	#用户名
    username = forms.CharField()
	#密码
    password = forms.CharField(widget = forms.PasswordInput)
def register(req):
	#如果是POST提交
    if req.method == 'POST':
		#接收校验绑定
        uf = UserForm(req.POST)
        if uf.is_valid():
			#取出表单提交的数据
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            email = uf.cleaned_data['email']
            passwordConfirm = uf.cleaned_data['passwordConfirm']
            if passwordConfirm == password:
				#保存数据
                User.objects.create(username = username, password = password,email = email)
				#注册成功从定向到登录页面
                return HttpResponseRedirect('/login/')
    else:
        uf = UserForm()
    return render_to_response('register.html', {'uf': uf})

def login(req):
    if req.method == 'POST':
        uf = loginForm(req.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            user = User.objects.filter(username__exact = username, password__exact = password)
            if user:
				#登录成功保存用户名到session
                req.session['username'] = username
				#跳转到投简历页面
                return HttpResponseRedirect('/resume/')
            else:
				#登录失败回到登录页面zt=1表示用户名或密码错误
                return render_to_response('login.html', {'zt': 1})
    else:
        uf = loginForm()
    return render_to_response('login.html', {'uf': uf})
