from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm


class LoginForm(forms.Form):
    """ Base class for authenticating users. Extend this to get a form that accepts
    username/password logins. """
    username = UsernameField(
        label='Логин',
        max_length=254,
        widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}),
    )
    password = forms.CharField(
        label='Пароль',
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

class RegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})