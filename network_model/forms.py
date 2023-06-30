from django import forms
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField
from .models import User
from django.contrib.auth import login, authenticate, get_user

class LoginForm(forms.Form):

    username = UsernameField(
        widget=forms.TextInput(attrs={
            "autofocus": True, 
            'placeholder': 'Username', 
            'class': 'typefield',
            'label': ''
        }),
    )

    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={
            "autocomplete": "current-password",
            'placeholder': 'Password', 
            'class': 'typefield',
            'label': ''
        }),
    )

    error_messages = 'Please enter a correct %(username)s and password.'

    def is_valid(self) -> bool:
        return True

    def clean(self) -> None:
        username = self.request.get("username")
        password = self.request.get("password")

        if username is not None and password:
            self.user_cache = authenticate(
                self.request, username=username, password=password
            )

    
    def get_user(self) -> User:
        return self.user_cache
    
    class Meta:
        model = User
        fields = ['username', 'password']

    class Media:
        css = {
            'all': ('css/auth.css',),
        }

    def __init__(self, request = None, *args, **kwargs):

        self.request = request

        super(LoginForm, self).__init__(*args, **kwargs)

class RegistrationForm(forms.Form):

    username = UsernameField(
        widget=forms.TextInput(attrs={
            "autofocus": True, 
            'placeholder': 'Username', 
            'class': 'typefield',
            'label': ''
        }),
    )

    password1 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={
            "autocomplete": "current-password",
            'placeholder': 'Password', 
            'class': 'typefield',
            'label': ''
        }),
    )

    password2 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={
            "autocomplete": "current-password",
            'placeholder': 'Confirm password', 
            'class': 'typefield',
            'label': ''
        }),
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    class Media:
        css = {
            'all': ('css/auth.css',),
        }

    def is_valid(self) -> bool:
        return True

    def save(self):
        username = self.request.get("username")
        password1 = self.request.get("password1")
        password2 = self.request.get("password2")

        if password1 == password2:
            user = User(username=username)
            user.set_password(password1)
            user.save()
            self.user_cache = user

    def get_user(self) -> User:
        return self.user_cache

    def __init__(self, request = None, *args, **kwargs):

        self.request = request

        super(RegistrationForm, self).__init__(*args, **kwargs)


