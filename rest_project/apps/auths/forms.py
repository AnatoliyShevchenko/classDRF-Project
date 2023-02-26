# Django
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import (
    UserChangeForm,
    UserCreationForm
)

# Local
from auths.models import Client
from auths.services import check_symbols_in_password


class ClientCreationForm(UserCreationForm):

    class Meta:
        model = Client
        fields = (
            'email',
        )


class ClientChangeForm(UserChangeForm):

    class Meta:
        model = Client
        fields = (
            'email',
        )


class ClientForm(forms.ModelForm):
    """Client Form."""
    
    email = forms.EmailField(
        label='Почта'
    )
    password = forms.CharField(
        widget=forms.PasswordInput,
        label='Пароль'
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput,
        label='Пароль2'
    )

    class Meta:
        model = Client
        fields = (
            'email',
            'password',
            'password2'
        )

    def clean(self):
        POST_SERVICES = (
            'gmail.com',
            'yandex.kz',
            'yandex.ru',
            'outlook.com',
            'mail.ru',
        )
        email = self.cleaned_data['email']
        temp_mail = email.split('@')
        i: str
        count: int = 0
        for i in temp_mail[0]:
            if i.isdigit():
                count += 1
        if temp_mail[0][0].isdigit() == True:
            raise ValidationError(
                'cannot register user with first symbol is number'
            )
        elif count > 1:
            raise ValidationError(
                'cannot register user with many symbols is numbers'
            )
        elif 'root' in email:
            raise ValidationError('cannot create user with root mail')
        elif temp_mail[1] not in POST_SERVICES:
            raise ValidationError(
                'cannot create user with unknown mail'
            )
        elif len(email) < 10 and len(email) > 50:
            raise ValidationError('too short or too long mail')
        password = self.cleaned_data['password']
        if len(password) < 12 and len(password) > 24:
            raise ValidationError('too short or too long password')
        accept_password = check_symbols_in_password(password)
        if not accept_password:
            raise ValidationError('password must contain letters, \
                numbers and special characters')
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise ValidationError('Пароли не совпадают')

