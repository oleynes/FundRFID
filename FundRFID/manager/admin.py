from django.contrib import admin

# Register your models here.
from .models import Member


class MemberAdmin(admin.ModelAdmin):
	fieldsets = [
		('Member Information', {'fields': ['name, email, img, PAWS_ID']}),
		('Tag Info', {'fields': ['tag_UID']}),
		('Score Info', {'fields': ['score']}),
	]


admin.site.register(Member, MemberAdmin)