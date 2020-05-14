from django.contrib import admin
from .models import FormLink
# Register your models here.


class FormLinkAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Link', {'fields': ['link']}),
        ('Info', {'fields': ['title', 'description']}),
    ]


admin.site.register(FormLink, FormLinkAdmin)
