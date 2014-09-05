#coding=utf-8
from django.db import models
             
class User(models.Model):
             
    username = models.CharField('用户名',max_length = 30)
    password = models.CharField('密  码',max_length = 100)
    email = models.CharField("邮箱",max_length=100)        
    def __unicode__(self):
        return self.username
    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'    