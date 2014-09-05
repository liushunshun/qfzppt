from django.contrib import admin
from zp.models import User
           
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')
           
admin.site.register(User, UserAdmin)
