from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreateAccountForm(UserCreationForm):
    first_name = forms.CharField(label="First Name")
    last_name = forms.CharField(label="Last Name")
    email = forms.EmailField(label="Email")

    def save(self, commit=True):
        user = super(CreateAccountForm, self).save(commit=False)
        first_name = forms.cleaned_data['first_name']
        last_name = forms.cleaned_data['last_name']
        username = f'{first_name.capitalize()}{last_name.capitalize()}'
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name")