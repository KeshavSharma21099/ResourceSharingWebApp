from django import forms
from .models import Directory


class DirectoryModelForm(forms.ModelForm):
    class Meta:
        model = Directory
        fields = ['name', 'subject']


class ShareDirectoryForm(forms.Form):
    user_name = forms.CharField(max_length=150)

    class Meta:
        fields = ['user_name']


class UserSearchForm(forms.Form):
    username = forms.CharField(max_length=100)
