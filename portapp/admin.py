from django.contrib import admin
from .models import Portfolio
from django.contrib.admin.sites import site
# Register your models here.
admin.site.register(Portfolio)