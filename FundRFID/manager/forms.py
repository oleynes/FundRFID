from django import forms
from .models import Member
from crispy_forms.helper import FormHelper


class MemberForm(forms.ModelForm):
    helper = FormHelper()

    class Meta:
        model = Member
        fields = ['name', 'email', 'PAWS_ID', 'class_year']


class LookupForm(forms.Form):
    paws_id = forms.CharField(label='PAWS ID', max_length=6)
