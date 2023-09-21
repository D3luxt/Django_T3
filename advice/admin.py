from django.contrib import admin
from .models import *
# Register your models here.

class usernotebookadmin(admin.ModelAdmin):
    list_display = ['gender','phone','accountlink']
    search_fields = ['gender']

class ProAddAdmin(admin.ModelAdmin):
    list_display = ['pro_id','pro_name','brand','amount','price',]

admin.site.register(usernotebook, usernotebookadmin)
admin.site.register(productitem, ProAddAdmin)