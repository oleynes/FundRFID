from django.contrib import admin
from .models import Event, Announcement, EboardMember
# Register your models here.


class EventAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Event Information', {'fields': ['name', 'dt', 'location']}),
        ('Event Details', {'fields': ['description', 'img']}),
    ]


class AnnouncementAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Announcement Information', {'fields': ['name']}),
        ('Announcement Details', {'fields': ['description', 'img']})
    ]


class EboardMemberAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Personal Info', {'fields': ['first_name', 'last_name', 'email']}),
        ('Extra Info', {'fields': ['profile', 'position', 'class_year']}),
    ]


admin.site.register(Event, EventAdmin)
admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(EboardMember, EboardMemberAdmin)
