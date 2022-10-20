from django import forms
from django.contrib.auth.models import User

INVALID_USERNAMES = ['admin','adminstrator', 'root']

# login form
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username__iexact=username)
        if not qs.exists():
            raise forms.ValidationError("Inavalid Credentials")
        return username


# register form
class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.CharField(help_text='Enter a valid email address')
    password1 = forms.CharField(widget=forms.PasswordInput, label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Password')

def clean_username(self):
    username = self.cleaned_data.get('username')
    qs = User.objects.filter(username_iexact=username)
    if qs.exists():
        raise forms.ValidationError("Username is not available")
    if username.lower() in INVALID_USERNAMES:
        raise forms.ValidationError("Username is invalid")
    return username

def clean_email(self):
    email = self.cleaned_data.get('email')
    qs = User.objects.filter(email_iexact=email)
    if qs.exists():
        raise forms.ValidationError("Email is already exists")
    return email