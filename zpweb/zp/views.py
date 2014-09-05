#coding=utf-8
from django.shortcuts import render_to_response
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from zp.models import User

class UserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)
    passwordConfirm = forms.CharField(widget = forms.PasswordInput)
class loginForm(forms.Form):
    username = forms.CharField(label='用户名')
    password = forms.CharField(label='密  码',widget = forms.PasswordInput)
def register(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            passwordConfirm = uf.cleaned_data['passwordConfirm']
            if passwordConfirm == password:
                User.objects.create(username = username, password = password)
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
                req.session['username'] = username
                return HttpResponseRedirect('/index/')
            else:
                return HttpResponseRedirect('/login/')
    else:
        uf = loginForm()
    return render_to_response('login.html', {'uf': uf})
def index(req):
    return render_to_response('index.html', {})