from django.forms import ModelForm
from .models import Member


class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'email', 'PAWS_ID', 'class_year']
