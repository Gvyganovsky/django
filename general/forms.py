from django import forms
from django.contrib.auth.forms import UserCreationForm
from flowershop.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    rules = forms.BooleanField(required=True)

    class Meta:
        model = CustomUser
        fields = ('patronymic', 'email', 'password1', 'password2', 'rules')
