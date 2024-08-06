from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.core.exceptions import ValidationError

from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('Имя', 'Телефон')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Записаться'))

    def clean_Телефон(self):
        phone_number = self.cleaned_data.get('Телефон')

        if phone_number.startswith('+7'):
            if len(phone_number) != 12:
                raise ValidationError('Номер телефона должен содержать 12 символов, если он начинается с +7.')
        else:
            if len(phone_number) != 11:
                raise ValidationError('Номер телефона должен содержать 11 символов, если он не начинается с +7.')

        return phone_number
