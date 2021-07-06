from django.contrib import admin
from .models import cookies

@admin.register(cookies)
class CookieAdmin(admin.ModelAdmin):
    list_display = ['name']
