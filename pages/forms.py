
from django.forms import ModelForm
from .models import *


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['firstname', 'lastname', 'email',
                  'tel', 'message']
