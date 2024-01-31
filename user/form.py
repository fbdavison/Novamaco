from django import forms
from django.contrib.auth import authenticate
from user.models import Users


class AccountAuthenticationForm(forms.ModelForm):

    email = forms.CharField(label='email', widget=forms.EmailInput(
        attrs={
            'id': 'Email-4',
            'class': 'a-account-text-field w-input',
            'maxlength': '256',
            'name': 'Email-4',
            'data - name': 'Email 4',
            'type': 'email'
        }
    ))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={
            'class': 'a-account-text-field w-input',
            'maxlength': '256',
            'name': 'Password-4',
            'data-name': 'Password 4',
            'type': 'password',
            'id': 'Password-4'
        }
    ))

    class Meta:
        model = Users
        fields = ('email', 'password')

    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        if not authenticate(email=email, password=password):
            raise forms.ValidationError('Invalid email or password')
