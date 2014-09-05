#coding=utf-8
from django.shortcuts import render_to_response
from django.shortcuts import render
from resume.models import Resume
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
#简历暂时不支持多个学历填写和多个项目经验填写
class ResumeForm(forms.Form):
	#姓名
    name = forms.CharField()
	#性别
    sex = forms.CharField()
	#图片上传本地已经实现，因为BAE上接口有点问题，暂时停用
    #headImg = forms.FileField(required=False)
	#邮箱
    email = forms.CharField()
	#电话
    tel = forms.CharField()
	#学历
    education = forms.CharField(required=False)
	#教育经历-开始时间
    edu_strdate = forms.CharField(required=False)
	#结束时间
    edu_enddate = forms.CharField(required=False)
	#学校
    school = forms.CharField(required=False)
	#专业
    major = forms.CharField(required=False)
	#学历
    cureducation = forms.CharField(required=False)
	#主修课程
    course = forms.CharField(required=False)
	#工作经历-开始时间
    work_strdate = forms.CharField(required=False)
	#结束时间
    work_enddate = forms.CharField(required=False)
	#公司
    company = forms.CharField(required=False)
	#职位
    position = forms.CharField(required=False)
	#薪水
    salary = forms.CharField(required=False)
	#工作描述
    workdisc = forms.CharField(required=False)
	#项目名称
    projectname = forms.CharField(required=False)
	#项目开始时间
    project_strdate = forms.CharField(required=False)
	#结束时间
    project_enddate = forms.CharField(required=False)
	#工作内容
    job = forms.CharField(required=False)
	#项目描述
    projectdisc = forms.CharField(required=False)
	#项目职责
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
            #保存数据
            resu.save()
			#zt=1表示投递简历成功
            return render_to_response('resume.html', {'zt': 1})
    else:
        rf = ResumeForm() 
	#从session中获得当前登录用户名返回
    username = req.session['username']
    return render_to_response('resume.html', {'rf':rf,'username':username})