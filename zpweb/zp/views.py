#coding=utf-8
from django.shortcuts import render_to_response
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from zp.models import User

class UserForm(forms.Form):
    email = forms.CharField()
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)
    passwordConfirm = forms.CharField(widget = forms.PasswordInput)
class loginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)
def register(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            email = uf.cleaned_data['email']
            passwordConfirm = uf.cleaned_data['passwordConfirm']
            if passwordConfirm == password:
                User.objects.create(username = username, password = password,email = email)
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
                return HttpResponseRedirect('/resume/')
            else:
                return render_to_response('login.html', {'zt': 1})
    else:
        uf = loginForm()
    return render_to_response('login.html', {'uf': uf})
