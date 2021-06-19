from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(models.Message)
admin.site.register(models.Teacher)
admin.site.register(models.User,UserAdmin)