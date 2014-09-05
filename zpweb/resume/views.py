#coding=utf-8
from django.shortcuts import render_to_response
from django.shortcuts import render
from resume.models import Resume
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
class ResumeForm(forms.Form):
    name = forms.CharField()
    sex = forms.CharField()
    #headImg = forms.FileField(required=False)
    email = forms.CharField()
    tel = forms.CharField()
    education = forms.CharField(required=False)
    edu_strdate = forms.CharField(required=False)
    edu_enddate = forms.CharField(required=False)
    school = forms.CharField(required=False)
    major = forms.CharField(required=False)
    cureducation = forms.CharField(required=False)
    course = forms.CharField(required=False)
    work_strdate = forms.CharField(required=False)
    work_enddate = forms.CharField(required=False)
    company = forms.CharField(required=False)
    position = forms.CharField(required=False)
    salary = forms.CharField(required=False)
    workdisc = forms.CharField(required=False)
    projectname = forms.CharField(required=False)
    project_strdate = forms.CharField(required=False)
    project_enddate = forms.CharField(required=False)
    job = forms.CharField(required=False)
    projectdisc = forms.CharField(required=False)
    projectresp = forms.CharField(required=False)
    #resumeFile = forms.FileField(required=False)
def resume(req):
    if req.method == 'POST':
        rf= ResumeForm(req.POST,req.FILES)
        if rf.is_valid():
            resu = Resume()
            resu.name = rf.cleaned_data['name']
            resu.sex = rf.cleaned_data['sex']
            #headImg = rf.cleaned_data['headImg']
            #if headImg != None:
                #imgPath = 'd:/upload/'+headImg.name;
                #fp = file(imgPath,'wb')
                #s = headImg.read()
                #fp.write(s)
                #fp.close()
                #resu.headImg = imgPath
            resu.email = rf.cleaned_data['email']
            resu.tel = rf.cleaned_data['tel']
            resu.education = rf.cleaned_data['education']
            resu.edu_strdate = rf.cleaned_data['edu_strdate']
            resu.edu_enddate = rf.cleaned_data['edu_enddate']
            resu.school = rf.cleaned_data['school']
            resu.major = rf.cleaned_data['major']
            resu.cureducation = rf.cleaned_data['cureducation']
            resu.course = rf.cleaned_data['course']
            resu.work_strdate = rf.cleaned_data['work_strdate']
            resu.work_enddate = rf.cleaned_data['work_enddate']
            resu.company = rf.cleaned_data['company']
            resu.position = rf.cleaned_data['position']
            resu.salary = rf.cleaned_data['salary']
            resu.workdisc = rf.cleaned_data['workdisc']
            resu.projectname = rf.cleaned_data['projectname']
            resu.project_strdate = rf.cleaned_data['project_strdate']
            resu.project_enddate = rf.cleaned_data['project_enddate']
            resu.job = rf.cleaned_data['job']
            resu.projectdisc = rf.cleaned_data['projectdisc']
            resu.projectresp = rf.cleaned_data['projectresp']
            #resumeFile = rf.cleaned_data['resumeFile']
            #if resumeFile != None:
                #filePath = 'd:/upload/'+resumeFile.name;
                #refile = file(filePath,'wb')
                #ss = resumeFile.read()
                #refile.write(ss)
                #refile.close()
                #resu.resumeFile = filePath
            
            resu.save()
			#zt=1表示投递简历成功
            return render_to_response('resume.html', {'zt': 1})
    else:
        rf = ResumeForm() 
	#从session中获得当前登录用户名返回
    username = req.session['username']
    return render_to_response('resume.html', {'rf':rf,'username':username})