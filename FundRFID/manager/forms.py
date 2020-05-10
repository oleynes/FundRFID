from django import forms
from .models import Member
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .validators import validate_pawsid


class MemberForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MemberForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Member
        fields = ['name', 'email', 'PAWS_ID', 'class_year']


class LookupForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(LookupForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.add_input(Submit('submit', 'Submit'))

    paws_id = forms.IntegerField(label='PAWS ID', validators=[validate_pawsid])
