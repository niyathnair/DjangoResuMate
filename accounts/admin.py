from django.contrib import admin
from .models import CustomUser
from django.contrib.admin.sites import site

# Register your models here.
admin.site.register(CustomUser)