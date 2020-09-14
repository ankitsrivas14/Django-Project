from django import forms
from django.core import validators

# ------ Form validations ------
def name_validation(value):
    if value[0] != 'Z':
        raise forms.ValidationError('Name must start with Z')

# ------ Form Input Fields ------
class FormName(forms.Form):
    name = forms.CharField(label="Name: ",validators=[name_validation])
    email = forms.EmailField(label="Email: ")
    verify_email = forms.EmailField(label="Enter Email Again: ")
    text = forms.CharField(label="Enter message: ",widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vemail = all_clean_data['verify_email']

        if email != vemail:
            raise forms.ValidationError('Email mismatch')
