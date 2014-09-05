#coding=utf-8
from django.contrib import admin
from resume.models import Resume

# Register your models here.
def moveToProductCategory(modeladmin, request, queryset):
    queryset.update(type='3')
moveToProductCategory.short_description = "移动到--产品类"
def moveToTechnologyCategory(modeladmin, request, queryset):
    queryset.update(type='2')
moveToTechnologyCategory.short_description = "移动到--技术类"
def makmoveToFunctionCategory(modeladmin, request, queryset):
    queryset.update(type='4')
makmoveToFunctionCategory.short_description = "移动到--职能类"
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('name', 'sex','type')
    actions = [moveToProductCategory,moveToTechnologyCategory,makmoveToFunctionCategory]
admin.site.register(Resume, ResumeAdmin)