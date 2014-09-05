#coding=utf-8
from django.db import models
sex_choices = (
    ('1','男'),
    ('2','女'),
)    
salary_choices = (
    ('1','保密'),
    ('2','1000-5000'),
    ('3','5000-8000'),
    ('4','8000-10000'),
    ('5','10000-20000'),
    ('6','20000+'),
) 
edu_choices = (
    ('1','本科'),
    ('2','硕士'),
    ('3','博士'),
    ('4','博士以上'),
    ('5','专科及以下'),
) 
type_choices = (
    ('1','未分类'),
    ('2','技术类'),
    ('3','产品类'),
    ('4','职能类'),
)  
class Resume(models.Model):
    name = models.CharField('姓名',max_length=30)
    sex = models.CharField('性别',max_length=10,choices=sex_choices)
    type = models.CharField('分类',max_length=2,choices=type_choices)
    headImg = models.FileField(upload_to='./upload/',blank=True)
    email = models.CharField('邮件',max_length=100)
    tel = models.CharField('电话',max_length=20)
    education = models.CharField('学历',max_length=1,choices=edu_choices,blank=True)
    edu_strdate = models.CharField('开始时间',max_length=10,blank=True)
    edu_enddate = models.CharField('结束时间',max_length=10,blank=True)
    school = models.CharField('学校',max_length=100,blank=True)
    major = models.CharField('专业',max_length=100,blank=True)
    cureducation = models.CharField('学历',max_length=100,choices=edu_choices,blank=True)
    course = models.CharField('主修课程',max_length=100,blank=True)
    work_strdate = models.CharField('工作开始时间',max_length=10,blank=True)
    work_enddate = models.CharField('工作结束时间',max_length=10,blank=True)
    company = models.CharField('公司',max_length=100,blank=True)
    position = models.CharField('职位',max_length=100,blank=True)
    salary = models.CharField('薪水',max_length=1,choices=salary_choices,blank=True)
    workdisc = models.CharField('工作描述',max_length=1,blank=True)
    projectname = models.CharField('项目名称',max_length=1,blank=True)
    project_strdate = models.CharField('项目开始时间',max_length=1,blank=True)
    project_enddate = models.CharField('项目结束时间',max_length=1,blank=True)
    job = models.CharField('主要工作',max_length=1,blank=True)
    projectdisc = models.CharField('项目描述',max_length=1,blank=True)
    projectresp = models.CharField('工作职责',max_length=1,blank=True)
    resumeFile = models.FileField('附件',upload_to='./upload/',blank=True)
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = '简历'
        verbose_name_plural = '简历'