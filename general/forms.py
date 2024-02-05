from django.contrib.auth.forms import UserCreationForm
from django.forms import forms, CharField, DecimalField, ChoiceField

from flowershop.models import CustomUser


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser


class ProductFilterForm(forms.Form):
    country = CharField(required=False)
    name = CharField(required=False)
    price_min = DecimalField(required=False, min_value=0)
    price_max = DecimalField(required=False, min_value=0)
    category_choices = [('', '---'), ('Цветы', 'Цветы'), ('Упаковка', 'Упаковка'), ('Дополнительно', 'Дополнительно')]
    category = ChoiceField(choices=category_choices, required=False)
