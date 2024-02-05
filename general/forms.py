from django.contrib.auth.forms import UserCreationForm
from django.forms import forms, CharField, DecimalField, ChoiceField, BooleanField, EmailField, TextInput, PasswordInput
from flowershop.models import CustomUser
from django.contrib.auth.forms import AuthenticationForm


class CustomAuthenticationForm(AuthenticationForm):
    username = CharField(label='Login', widget=TextInput(attrs={'class': 'form-control'}))
    password = CharField(label='Password', widget=PasswordInput(attrs={'class': 'form-control'}))


class RegistrationForm(UserCreationForm):
    first_name = CharField(max_length=30, required=True, help_text='Обязательное поле.')
    last_name = CharField(max_length=30, required=True, help_text='Обязательное поле.')
    patronymic = CharField(max_length=30, required=True, help_text='Обязательное поле.')
    email = EmailField(required=True, help_text='Введите действительный email адрес.')
    rules = BooleanField(required=True, help_text='Примите правила использования сайта.')

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'patronymic', 'username', 'email', 'password1', 'password2', 'rules']


class ProductFilterForm(forms.Form):
    country = CharField(required=False)
    name = CharField(required=False)
    price_min = DecimalField(required=False, min_value=0)
    price_max = DecimalField(required=False, min_value=0)
    category_choices = [('', '---'), ('Цветы', 'Цветы'), ('Упаковка', 'Упаковка'), ('Дополнительно', 'Дополнительно')]
    category = ChoiceField(choices=category_choices, required=False)
