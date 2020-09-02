from django import forms
from django.contrib.auth.models import User
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name', 'mail', 'birth_date', 'gender', 'location')


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name', 'mail', 'birth_date', 'gender', 'location')
        widgets = {
            'birth_date': forms.DateTimeInput(attrs={'class': 'datetime-input'})
        }


class UserSearchForm(forms.Form):
    username = forms.CharField(max_length=100)
    # fields = 'username'
