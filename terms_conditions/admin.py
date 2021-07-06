from django.contrib import admin
from .models import term_cond

@admin.register(term_cond)
class TermsAdmin(admin.ModelAdmin):
    list_display = ['cond']
