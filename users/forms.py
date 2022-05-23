from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms
from bootstrap_datepicker_plus.widgets import DatePickerInput
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django_countries.widgets import CountrySelectWidget


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email',)
        help_texts = {
            'username': None,
            'email': None,
            'password1': None,
        }


class CustomUserChangeForm(UserChangeForm):
    password = None
    phone_number = PhoneNumberField(widget=PhoneNumberPrefixWidget(initial='AUS'))

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'dob', 'location', 'phone_number']
        # exclude = ['phone_number']

        widgets = {'dob': DatePickerInput(), 'location': CountrySelectWidget(layout='{widget}'
                                                                                    '<img class="country-select-flag"'
                                                                                    ' id="{flag_id}" style="margin: 6px'
                                                                                    ' 4px 0" src="{country.flag}">'), }
        # 'phone_number': forms.TextInput(attrs={'class': 'form-control'})}
