from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from users.models import UserProfileInfo


class NewUserForm(ModelForm):
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


class NewUserProfileForm(ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')


class SignInForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
