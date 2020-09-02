from django import forms
from .models import Page
from Directory.models import Directory


class NewPageForm(forms.ModelForm):
    # def __init(self, *args, **kwargs):
    #     request = kwargs.pop('request' or None)
    #     if request is not None:
    #         user = request.user
    #     else:
    #         user = None
    #     super(NewPageForm, self).__init__(*args, **kwargs)
    #     if user is not None:
    #         self.fields['directory_choices'].queryset = Directory.objects.filter(user=user)
    #         # self.directory_choices = forms.ModelChoiceField(queryset=None, widget=forms.Select, required=True)

    # directory_choices = forms.ModelChoiceField(queryset=None, widget=forms.Select, required=False)

    class Meta:
        model = Page
        fields = ['title', 'comments', 'link']


class UserSearchForm(forms.Form):
    username = forms.CharField(max_length=100)
    # fields = 'username'
