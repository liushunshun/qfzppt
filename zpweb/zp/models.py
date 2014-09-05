#coding=utf-8
from django.db import models
             
class User(models.Model):
             
    username = models.CharField('名称',max_length = 30)
    password = models.CharField('密  码',max_length = 100)
             
    def __unicode__(self):
        return self.username