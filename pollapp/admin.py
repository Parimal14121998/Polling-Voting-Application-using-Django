from django.contrib import admin

# Register your models here.

from .models import pollmodel

admin.site.register(pollmodel)